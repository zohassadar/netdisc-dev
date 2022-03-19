import socket
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def get_host_by_ip(ip):
    try:
        result = socket.gethostbyaddr(ip)
        logging.debug("Resolved %s to: %s", ip, result)
        return result[0]
    except socket.herror as exc:
        logging.debug("Unable to resolve %s: %s.  Returning IP.", ip, exc)
        return ip


def get_ip_by_host(host):
    try:
        result = socket.gethostbyname(host)
        logging.debug("Resolved %s to: %s", host, result)
        return result
    except socket.gaierror as exc:
        logging.debug("Unable to resolve %s: %s.  Returning IP.", host, exc)
        return None
