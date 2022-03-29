"""
To add more mibs:
see devmibs.sh
"""
import dataclasses
import logging
import pprint
import socket
import typing
import os

import pysnmp.hlapi
import pysnmp.proto.rfc1902
import pysnmp.proto.rfc1905
import pysnmp.smi
import pysnmp.smi.builder
import pysnmp.smi.compiler
import pysnmp.smi.rfc1902
import pysnmp.smi.view

from netdisc.snmp import snmpbase, engine
from netdisc.tools import helpers


PYENG_DEBUG_OUTPUT = os.getenv("PYENG_DEBUG_OUTPUT")
debug_dumper = helpers.SNMPEngDebugDumper(PYENG_DEBUG_OUTPUT)


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


PY_AUTH_TABLE = {
    "MD5": pysnmp.hlapi.auth.usmHMACMD5AuthProtocol,
    "SHA": pysnmp.hlapi.auth.usmHMACSHAAuthProtocol,
}

PY_PRIV_TABLE = {
    "AES": pysnmp.hlapi.auth.usmAesCfb128Protocol,
    "AES192": pysnmp.hlapi.auth.usmAesCfb192Protocol,
    "AES256": pysnmp.hlapi.auth.usmAesCfb256Protocol,
    "3DES": pysnmp.hlapi.auth.usm3DESEDEPrivProtocol,
    "DES": pysnmp.hlapi.auth.usmDESPrivProtocol,
}


class PySNMPEngine(engine.SNMPEngine):
    __doc__ == engine.SNMPEngine.__doc__

    def __init__(self, *args, **kwargs):
        self._credential = None
        super().__init__(*args, **kwargs)

    def setup(self):
        logger.debug("PySNMP Setup started")
        self._target = pysnmp.hlapi.UdpTransportTarget(
            (self.host, self.port),
        )
        self._engine = pysnmp.hlapi.SnmpEngine()
        if self.cisco_vlan and not self.community:
            self._context = pysnmp.hlapi.ContextData(
                contextName=f"vlan-{self.cisco_vlan}"
            )
        else:
            self._context = pysnmp.hlapi.ContextData()

        logger.debug("PySNMP Setup complete")

    def set_v3_auth_priv(
        self,
        snmpuser: str,
        authtype: str,
        auth: str,
        privtype: str,
        priv: str,
    ):
        mapped_auth = PY_AUTH_TABLE.get(authtype, None)
        if mapped_auth is None:
            raise ValueError(f"Invalid auth type: {authtype}")
        mapped_priv = PY_PRIV_TABLE.get(privtype, None)
        if mapped_priv is None:
            raise ValueError(f"Invalid priv type: {privtype}")
        credential = {
            "userName": snmpuser,
            "authProtocol": mapped_auth,
            "authKey": auth,
            "privProtocol": mapped_priv,
            "privKey": priv,
        }
        self._credential = pysnmp.hlapi.UsmUserData(**credential)

    def set_v3_auth(
        self,
        snmpuser: str,
        authtype: str,
        auth: str,
    ):
        mapped_auth = PY_AUTH_TABLE.get(authtype, None)
        if mapped_auth is None:
            raise ValueError(f"Invalid auth type: {authtype}")
        no_priv = pysnmp.hlapi.auth.usmNoPrivProtocol
        credential = {
            "userName": snmpuser,
            "authProtocol": mapped_auth,
            "authKey": auth,
            "privProtocol": no_priv,
        }
        self._credential = pysnmp.hlapi.UsmUserData(**credential)

    def set_v3(
        self,
        snmpuser: str,
    ):
        no_auth = pysnmp.hlapi.auth.usmNoAuthProtocol
        no_priv = pysnmp.hlapi.auth.usmNoPrivProtocol
        credential = {
            "userName": snmpuser,
            "authProtocol": no_auth,
            "privProtocol": no_priv,
        }
        self._credential = pysnmp.hlapi.UsmUserData(**credential)

    def set_v2(
        self,
        community: str,
    ):
        if self.cisco_vlan:
            self._credential = pysnmp.hlapi.CommunityData(
                f"{community}@{self.cisco_vlan}"
            )
        else:
            self._credential = pysnmp.hlapi.CommunityData(community)

    def _get(
        self,
        *paths,
    ):
        logger.debug("PyEng _get method invoked: %s", paths)
        var_bindings = self._get_var_bindings(*paths)
        result = pysnmp.hlapi.getCmd(
            self._engine,
            self._credential,
            self._target,
            self._context,
            *var_bindings,
            lexicographicMode=False,
            lookupNames=True,
            lookupValues=True,
        )
        error_ind, error_status, error_index, var_binds = next(result)
        return error_ind, error_status, error_index, var_binds

    def get(
        self,
        *paths,
    ) -> list[tuple[typing.Any, str, typing.Any]]:
        logger.debug("PyEng get method invoked: %s", paths)
        error_ind, error_status, error_index, var_binds = self._get(*paths)
        result = self._process_result(
            error_ind,
            error_status,
            error_index,
            var_binds,
        )
        debug_dumper.dump(self.host, result, *paths)
        return result

    def _walk(self, *paths):
        logger.debug("PyEng _walk method invoked: %s", paths)
        var_bindings = self._get_var_bindings(*paths)
        result = pysnmp.hlapi.nextCmd(
            self._engine,
            self._credential,
            self._target,
            self._context,
            *var_bindings,
            lexicographicMode=False,
            lookupNames=False,
            lookupValues=True,
        )
        results = list(result)
        logger.debug("%s", pprint.pformat(results))
        return results

    def walk(
        self,
        *paths,
    ) -> list[tuple[typing.Any, str, typing.Any]]:
        results = []
        for (
            error_ind,
            error_status,
            error_index,
            var_binds,
        ) in self._walk(*paths):
            results.extend(
                self._process_result(
                    error_ind,
                    error_status,
                    error_index,
                    var_binds,
                )
            )
        debug_dumper.dump(self.host, results, *paths)
        return results

    def _get_var_bindings(self, *paths) -> list:
        var_bindings = []

        get_obj_id = lambda path: pysnmp.hlapi.ObjectIdentity(*path).addMibSource(
            self.mib_helper.mib_source
        )
        for path in paths:
            logger.debug("Retrieving oid info for: %s", path)
            object_identity = get_obj_id(path)
            logger.debug("Oid retrieved: %s", repr(object_identity))
            object_type = pysnmp.hlapi.ObjectType(
                object_identity,
            )
            logger.debug("object_type: %s", repr(object_type))
            var_bindings.append(object_type)
        return var_bindings

    def object_paths_compile(self, binding: snmpbase.VarBindBase, index: int = None):
        paths = []
        for field in dataclasses.fields(binding):
            if index is not None:
                paths.append((binding.MIB, field.name, index))
            else:
                paths.append((binding.MIB, field.name))
        return paths

    def _process_index(self, oid, var_bind):
        logging.debug(
            "Received index with: oid=%s var_bind=%s",
            oid,
            var_bind,
        )
        mib, field, indices = oid.getMibSymbol()
        logger.debug("Processing index result for %s::%s", mib, field)
        indices_results = []
        if not indices:
            return
        for index in indices:
            class_repr = repr(type(index))
            printed = index.prettyPrint()
            logger.debug("Index of type %s pretty prints to: %s", class_repr, printed)
            if 1 == 2:
                pass
            elif isinstance(index, pysnmp.proto.rfc1902.ObjectName):
                indices_results.append(printed)
            elif class_repr == "<class 'AddressFamilyNumbers'>":
                indices_results.append(printed)
            elif class_repr == "<class 'LldpManAddress'>":
                indices_results.append(socket.inet_ntoa(index.asOctets()))
            else:
                logger.debug("Index Processing.  Unknown index type: %s", class_repr)
                indices_results.append(printed)

                # indices_results.append(label)
        indices_results = [int(i) if i.isdigit() else i for i in indices_results]
        index_length = len(indices_results)
        if index_length == 1:
            index = indices_results[0]
        elif index_length > 1:
            index = tuple(indices_results)
        else:
            raise ValueError("No index found")
        return index

    def _process_var_bind(self, oid, var_bind) -> tuple[str, typing.Any]:
        class_repr = repr(type(var_bind))
        logger.debug("Received type: %s", class_repr)
        label = oid.getMibNode().getLabel()
        logger.debug("Label is: %s", label)
        if isinstance(var_bind, pysnmp.proto.rfc1905.EndOfMibView):
            logger.debug("EndOfMibView encountered")
            value = None
        elif class_repr == "<class 'CiscoNetworkAddress'>":
            logger.debug("IP Address.  Converting")
            value = socket.inet_ntoa(var_bind.asOctets())
        elif isinstance(var_bind, pysnmp.smi.rfc1902.ObjectIdentity):
            logger.debug("Object Identity.  Requires secondary lookup")
            oid_tuple = var_bind.getOid().asTuple()
            value = oid_tuple
            # value = self.mib_helper.get_value_from_oid(oid_tuple)
        elif hasattr(var_bind, "prettyPrint"):
            logger.debug("Attempting PrettyPrint")
            value = var_bind.prettyPrint()
        elif hasattr(var_bind, "getValue"):
            logger.debug("Attempting getValue")
            value = var_bind.getValue()
        else:
            raise ValueError(
                f"Unexpected type: {type(var_bind)}.  Input:  {oid=} {var_bind=}"
            )
        logger.debug("Result is: %s", value)
        if isinstance(value, str) and value.isdigit():
            value = int(value)
        return label, value

    def _process_result(
        self,
        error_indication,
        error_index,
        error_status,
        var_binds: list,
    ) -> list[tuple[str, typing.Any]]:
        if error_indication:
            logger.error(
                "Error encountered: %s, %s, %s",
                error_indication,
                error_index,
                error_status,
            )
            return []
        results = []
        for oid, var_bind in var_binds:
            index = self._process_index(oid, var_bind)
            label, value = self._process_var_bind(oid, var_bind)
            if not isinstance(label, str):
                raise ValueError(
                    f"Label is not a string. "
                    f" Is is {type(label)}.  Result from: {oid!r} {var_bind!r}"
                )
            results.append((index, label, value))
        return results
