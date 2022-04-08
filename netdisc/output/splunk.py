import argparse
import getpass
import json
import logging
import os
import pprint
import socket

import requests
import urllib3
import urllib3.exceptions
from netdisc.tools import log_setup


DEFAULT_SPLUNK_PORT = 8088
DEFAULT_SPLUNK_INDEX = "syslog"
DEFAULT_SPLUNK_SOURCETYPE = "netdisc"
DEFAULT_SPLUNK_USE_HTTP = False
DEFAULT_SPLUNK_MESSAGE_SIZE_LIMIT = 5000

SPLUNK_SOURCETYPE = "SPLUNK_SOURCETYPE"
SPLUNK_INDEX = "SPLUNK_INDEX"
SPLUNK_HOST = "SPLUNK_HOST"
SPLUNK_PORT = "SPLUNK_PORT"
SPLUNK_HEC_TOKEN = "SPLUNK_HEC_TOKEN"
SPLUNK_USE_HTTP = "SPLUNK_USE_HTTP"
SPLUNK_MESSAGE_SIZE_LIMIT = "SPLUNK_MESSAGE_SIZE_LIMIT"

pprinter = pprint.PrettyPrinter(width=200)
pp = pprinter.pprint

parser = argparse.ArgumentParser(add_help=False)
splunk_group = parser.add_argument_group("Splunk options")

splunk_group.add_argument(
    "--splunk-host",
    dest="host",
    type=str,
    help="Splunk host",
)
splunk_group.add_argument(
    "--splunk-index",
    dest="index",
    type=str,
    default=DEFAULT_SPLUNK_INDEX,
    help="Splunk index",
)
splunk_group.add_argument(
    "--splunk-sourcetype",
    dest="sourcetype",
    type=str,
    default=DEFAULT_SPLUNK_SOURCETYPE,
    help="Splunk sourcetype",
)
splunk_group.add_argument(
    "--splunk-port",
    dest="port",
    type=int,
    default=DEFAULT_SPLUNK_PORT,
    help="Splunk port",
)
splunk_group.add_argument(
    "--splunk-hec-token",
    dest="hec_token",
    type=str,
    help="Splunk http event collector token",
)
splunk_group.add_argument(
    "--splunk-size-limit",
    dest="message_size_limit",
    type=int,
    default=DEFAULT_SPLUNK_MESSAGE_SIZE_LIMIT,
    help="Splunk message size limit",
)
splunk_group.add_argument(
    "--splunk-use-http",
    dest="http",
    action="store_true",
    help="use http",
)

debug_parser = argparse.ArgumentParser(add_help=False)

debug_splunk_group = debug_parser.add_argument_group("Splunk debug options")

debug_splunk_group.add_argument(
    "--message",
    type=str,
    help="Message sent with log",
)


class SplunkOutput:
    def __init__(
        self,
        host=None,
        port=None,
        hec_token=None,
        index=None,
        sourcetype=None,
        http=False,
        message_size_limit=None,
    ):

        self.host = host or os.getenv(SPLUNK_HOST)
        self.port = port or os.getenv(SPLUNK_PORT) or DEFAULT_SPLUNK_PORT
        self.hec_token = hec_token or os.getenv(SPLUNK_HEC_TOKEN)
        self.index = index or os.getenv(SPLUNK_INDEX) or DEFAULT_SPLUNK_INDEX
        self.sourcetype = (
            sourcetype or os.getenv(SPLUNK_SOURCETYPE) or DEFAULT_SPLUNK_SOURCETYPE
        )
        self.http = http or os.getenv(SPLUNK_USE_HTTP) or DEFAULT_SPLUNK_USE_HTTP
        self.message_size_limit = (
            message_size_limit
            or os.getenv(SPLUNK_MESSAGE_SIZE_LIMIT)
            or DEFAULT_SPLUNK_MESSAGE_SIZE_LIMIT
        )

        if not self.host:
            raise RuntimeError("Unable to instantiate without a host")
        if not self.hec_token:
            raise RuntimeError(
                "Unable to instantiate without an http event collector token"
            )
        logging.info(
            'Initialized with host: "%s", splunkindex: "%s" & sourcetype: "%s"',
            self.host,
            self.index,
            self.sourcetype,
        )
        self._script = __name__
        self._server = socket.gethostname()
        self._server_ip = socket.gethostbyname(self._server)
        self._user = getpass.getuser()
        self._set_session()

    def _set_session(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self._url = f'http{"" if self.http else "s"}://{self.host}:{self.port}/services/collector'
        self._session = requests.Session()
        self._session.verify = False
        self._session.headers.update(
            {
                "Authorization": f"Splunk {self.hec_token}",
                "Content-Type": "application/json",
            }
        )

    def _get_splunk_payload(self, **kwargs):
        payload_dict = {
            "host": self._server_ip,
            "source": self._script,
            "index": self.index,
            "sourcetype": self.sourcetype,
            "event": {
                "server": self._server,
                "script": self._script,
                "user": self._user,
            },
        }
        logging.debug("Base splunk entry:\n%s", json.dumps(payload_dict, indent=4))
        added_payload = {}
        added_payload = {k: str(v) for k, v in kwargs.items() if v is not None}
        payload_dict["event"].update(**added_payload)
        logging.debug("Sending %s k,v pairs to splunk", len(payload_dict["event"]))
        logging.debug("Post splunk entry:\n%s", json.dumps(payload_dict, indent=4))
        return json.dumps(payload_dict)

    def dump(self, *args, **kwargs) -> None:
        if args and (len(args) > 1 or not isinstance(args[0], dict)):
            raise RuntimeError(f"dump takes either keyword arguments or a single dict")
        elif not args and not kwargs:
            raise RuntimeError(f"cannot dump an empty message")
        payload = self._get_splunk_payload(**kwargs)
        payload_length = len(payload)
        if payload_length > self.message_size_limit:
            logging.critical(
                "Message of %s bytes too long.  Discarding.", payload_length
            )
            return
        logging.debug("Sending %s bytes to splunk", payload_length)
        try:
            result = self._session.post(self._url, data=payload, verify=False)
            logging.debug("Splunk result: %s, %s", result.status_code, result.text)
        except requests.exceptions.SSLError as exc:
            if self.http_fallback and not self.http:
                logging.error(f"Attempting HTTP fallback: {exc!s}")
                self.http = True
                self._set_session()
                self.dump(*args, **kwargs)
            elif self.http_fallback:
                logging.error(f"Unexpected ssl error: {exc!s}")
            else:
                logging.error(f"Ssl error: {exc!s}")


help_only = argparse.ArgumentParser(
    parents=[
        log_setup.log_parser,
        parser,
        debug_parser,
    ]
)

if __name__ == "__main__":

    help_only.parse_args()
    log_setup.set_logger_from_args()
    args, _ = parser.parse_known_args()
    debug_args, _ = debug_parser.parse_known_args()

    pp(vars(debug_args) | vars(args))

    sender = SplunkOutput(
        **vars(args),
    )
    sender.dump(message=debug_args.message)
