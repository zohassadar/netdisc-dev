"""

https://easysnmp.readthedocs.io/en/latest/
sudo apt-get install libsnmp-dev snmp-mibs-downloader
sudo apt-get install gcc python-dev

pip install easysnmp
"""
import dataclasses
import logging
import typing
import os
import easysnmp
import easysnmp.exceptions

from netdisc.tools import helpers
from netdisc.snmp import engine

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


EASY_AUTHS = ("MD5", "SHA")
EASY_PRIVS = ("AES", "DES", "3DES")


EASY_DEBUG_OUTPUT = os.getenv("EASY_DEBUG_OUTPUT")


class EasySNMPEngine(engine.SNMPEngine):
    __doc__ = engine.SNMPEngine.__doc__

    def __init__(self, *args, **kwargs):
        self._kwargs = {}
        super().__init__(*args, **kwargs)
        self.debug_dumper = helpers.SNMPEngDebugDumper(EASY_DEBUG_OUTPUT)

    def setup(self):
        logger.debug("%s starting setting up", type(self))
        self._kwargs["hostname"] = self.host
        self._kwargs["remote_port"] = self.port
        community = self._kwargs.get("community")
        if self.cisco_vlan and community:
            self._kwargs["community"] = f"{community}@{self.cisco_vlan}"
        elif self.cisco_vlan:
            self.context = f"vlan-{self.cisco_vlan}"
        # self._kwargs["use_enums"] = False
        # self._kwargs["use_numeric"] = False
        # self._kwargs["use_sprint_value"] = False
        # # self._kwargs["best_guess"] = 2
        self._session = easysnmp.Session(**self._kwargs)
        logger.debug("%s finished setting up", type(self))

        # best_guess – this setting controls how oids are parsed; setting to 0 causes a
        # regular lookup. setting to 1 causes a regular expression match
        # (defined as -Ib in snmpcmd); setting to 2 causes a random access lookup
        # (defined as -IR in snmpcmd).

    def set_v3_auth_priv(
        self,
        snmpuser: str,
        authtype: str,
        auth: str,
        privtype: str,
        priv: str,
    ):
        if auth not in EASY_AUTHS:
            raise ValueError(f"Invalid Auth Type for Easy SNMP: {auth}")
        if priv not in EASY_PRIVS:
            raise ValueError(f"Invalid Priv Type for Easy SNMP: {priv}")
        self._kwargs["version"] = 3
        self._kwargs["security_level"] = "auth_with_privacy"
        self._kwargs["security_username"] = snmpuser
        self._kwargs["auth_protocol"] = authtype
        self._kwargs["auth_password"] = auth
        self._kwargs["privacy_protocol"] = privtype
        self._kwargs["privacy_password "] = priv

    def set_v3_auth(
        self,
        snmpuser: str,
        authtype: str,
        auth: str,
    ):
        if auth not in EASY_AUTHS:
            raise ValueError(f"Invalid Auth Type for Easy SNMP: {auth}")
        self._kwargs["version"] = 3
        self._kwargs["security_level"] = "auth_without_privacy"
        self._kwargs["security_username"] = snmpuser
        self._kwargs["auth_protocol"] = authtype
        self._kwargs["auth_password"] = auth

    def set_v3(
        self,
        snmpuser: str,
    ):
        self._kwargs["version"] = 3
        self._kwargs["security_level"] = "no_auth_or_privacy"
        self._kwargs["security_username"] = snmpuser

    def set_v2(
        self,
        community: str,
    ):
        self._kwargs["version"] = 2
        self._kwargs["community"] = community

    def _get(
        self,
        *paths,
    ):
        logger.debug("%s _get invoked: %s", type(self), paths)
        results = []
        try:
            results = self._session.get(
                list(paths),
            )
        except easysnmp.exceptions.EasySNMPError:
            logger.error("Error attempting to get: %s", "".join(paths))
        return results

    def get(
        self,
        *paths,
    ) -> list[tuple[typing.Any, str, typing.Any]]:
        logger.debug("%s get invoked: %s", type(self), paths)

        results = self._get(*paths)
        logger.debug("%s received %s results", type(self), len(results))
        self.debug_dumper.dump(self.host, results, *paths)
        processed = self._process_results(results)
        logger.debug(
            "%s received %s results after processing", type(self), len(processed)
        )
        return processed

    def _walk(
        self,
        *paths,
    ):
        logger.debug("%s _walk invoked: %s", type(self), paths)
        results = []
        try:
            results = self._session.bulkwalk(
                list(paths),
            )
        except easysnmp.exceptions.EasySNMPError:
            logger.error("Error attempting to walk: %s", "".join(paths))
        return results

    def walk(
        self,
        *paths,
    ) -> list[tuple[typing.Any, str, typing.Any]]:
        results = self._walk(*paths)
        logger.debug("%s received %s results", type(self), len(results))
        self.debug_dumper.dump(self.host, results, *paths)
        processed = self._process_results(results)
        logger.debug(
            "%s received %s results after processing", type(self), len(processed)
        )
        return processed

    def _process_index(self, result):
        logger.debug("Processing index %s", result.oid_index)
        field = result.oid
        index = result.oid_index
        if field == "sysUpTimeInstance":
            return 0
        return index

    def _process_field(self, result):
        logger.debug("Processing field %s", result.oid)
        field = result.oid
        if field == "sysUpTimeInstance":
            return "sysUpTime"
        return field

    def _process_value(self, result):
        logger.debug("Processing value %s", result.value)
        value = result.value
        if value.isdigit():
            return int(value)
        # if result.snmp_type == "OCTETSTR" and result.oid == "dot1dTpFdbAddress":
        #     value = ":".join(f"{ord(c):02x}" for c in result.value)
        return value

    def _process_results(
        self, results: list[easysnmp.SNMPVariable]
    ) -> list[tuple[typing.Any, str, typing.Any]]:
        processed = []
        for result in results:
            # error check?
            index = self._process_index(result)
            field = self._process_field(result)
            value = self._process_value(result)
            processed.append((index, field, value))
        return processed

    def object_paths_compile(self, binding, index=None):
        paths = []
        for field in dataclasses.fields(binding):
            prefix = f"{binding.MIB}::{field.name}"
            if index is not None:
                paths.append(f"{prefix}.{index}")
            else:
                paths.append(prefix)
        return paths
