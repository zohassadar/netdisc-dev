from netdisc.discover import authen
from netdisc.base import constant
import pytest


@pytest.fixture
def example_input_1():
    return {
        "userpass": {
            "username": "asdf",
            "password": "asdf",
        },
        "userpasssecret": {
            "username": "fdsa",
            "password": "fdsa",
            "secret": "secret",
        },
        "version3": {
            "snmpuser": "fdsa",
            "authtype": "fdsa",
            "auth": "secret",
        },
        "version2": {
            "community": "fdsa",
        },
    }


@pytest.fixture
def example_input_invalid():
    return {
        "userpass": {
            "username": "asdf",
            "password": "asdf",
        },
        "userpasssecret": {
            "username": "fdsa",
            "password": "fdsa",
            "secret": "secret",
        },
        "version3": {
            "snmpuser": "fdsa",
            "authtype": "fdsa",
            "auth": "secret",
        },
        "version2": {
            "blahblah": "fdsa",
        },
    }


@pytest.fixture
def simple_input():
    return {
        "userpass1": {
            "username": "asdf",
            "password": "asdf",
        },
        "userpass2": {
            "username": "asdf",
            "password": "asdf",
        },
        "version2": {
            "community": "fdsa",
        },
    }


@pytest.fixture
def simple_input_with_retries():
    return {
        "userpass1": {
            "username": "asdf",
            "password": "asdf",
            "retries": 1,
        }
    }


def test_valid_username_auth_method():
    authen.AuthMethod(
        username="asdf",
        password="asdf",
    )


def test_valid_username_auth_method_with_secret():
    authen.AuthMethod(
        username="asdf",
        password="asdf",
        secret="asdf",
    )


def test_valid_snmp_noauth_nopriv():
    authen.AuthMethod(
        snmpuser="asdf",
    )


def test_valid_snmp_auth_nopriv():
    authen.AuthMethod(
        snmpuser="asdf",
        authtype="MD5",
        auth="asdf",
    )


def test_valid_snmp_auth_priv():
    authen.AuthMethod(
        snmpuser="asdf",
        authtype="MD5",
        auth="asdf",
        privtype="AES",
        priv="asdf",
    )


def test_valid_snmp_community():
    authen.AuthMethod(
        community="asdf",
    )


def test_invalid_snmp_community_v3user():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            snmpuser="asdf",
            community="asdf",
        )


def test_invalid_snmp_v3user_user():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            snmpuser="asdf",
            username="asdf",
        )


def test_invalid_snmp_user_community():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            username="asdf",
            community="asdf",
        )


def test_invalid_snmp_user_auth_missing():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            snmpuser="asdf",
            authtype="MD5",
        )


def test_invalid_snmp_user_authtype_missing():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            snmpuser="asdf",
            auth="asdf",
        )


def test_invalid_snmp_user_privtype():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            snmpuser="asdf",
            privtype="AES",
            priv="asdf",
        )


def test_invalid_snmp_auth_privtype_missing():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            snmpuser="asdf",
            authtype="MD5",
            auth="asdf",
            priv="asdf",
        )


def test_invalid_snmp_auth_priv_missing():
    with pytest.raises(ValueError):
        authen.AuthMethod(
            snmpuser="asdf",
            authtype="MD5",
            auth="asdf",
            privtype="AES",
        )


def test_example_input(example_input_1):
    a = authen.AuthMethodList()
    a.load_authentication_methods(example_input_1)


def test_example_input_invalid(example_input_invalid):
    with pytest.raises(ValueError):
        a = authen.AuthMethodList()
        a.load_authentication_methods(example_input_invalid)


@pytest.mark.parametrize(
    "kwargs",
    (
        pytest.param({"ssh": 1}, id="invalid ssh"),
        pytest.param({"telnet": 1}, id="invalid telnet"),
        pytest.param({"api": 1}, id="invalid api"),
        pytest.param({"keep_score": 1}, id="invalid keep_score"),
    ),
)
def test_invalid_booleans(kwargs):
    with pytest.raises(ValueError):
        authen.AuthMethodList(**kwargs)


def test_example_input_copy(example_input_1):
    a = authen.AuthMethodList()
    a.load_authentication_methods(example_input_1)
    a.copy()


def test_example_input_copy_copy(example_input_1):
    with pytest.raises(RuntimeError):
        a = authen.AuthMethodList()
        a.load_authentication_methods(example_input_1)
        a.copy().copy()


def test_example_input_next_called(example_input_1):
    with pytest.raises(RuntimeError):
        a = authen.AuthMethodList()
        a.load_authentication_methods(example_input_1)
        a.next()


def test_example_input_next_protocol_called(example_input_1):
    with pytest.raises(RuntimeError):
        a = authen.AuthMethodList()
        a.load_authentication_methods(example_input_1)
        a.next_protocol()


def test_example_input_copy_next_protocol_called(example_input_1):
    with pytest.raises(RuntimeError):
        a = authen.AuthMethodList()
        a.load_authentication_methods(example_input_1)
        a.copy().next_protocol()


def test_example_input_first_auth(simple_input):
    a = authen.AuthMethodList(ssh=True, api=False, telnet=False)
    a.load_authentication_methods(simple_input)
    copy = a.copy()
    auth = copy.next()
    assert auth.proto is constant.Proto.SSH


def test_example_input_second_auth_next(simple_input):
    a = authen.AuthMethodList(ssh=True, api=False, telnet=False)
    a.load_authentication_methods(simple_input)
    copy = a.copy()
    copy.next()
    auth = copy.next()
    assert auth.proto is constant.Proto.SSH


def test_example_input_second_auth_next_protocol(simple_input):
    a = authen.AuthMethodList(ssh=True, api=False, telnet=False)
    a.load_authentication_methods(simple_input)
    copy = a.copy()
    copy.next()
    auth = copy.next_protocol()
    assert auth.proto is constant.Proto.SNMPv2c


def test_example_input_first_auth_retries(simple_input_with_retries):
    a = authen.AuthMethodList(ssh=True, api=False, telnet=False)
    a.load_authentication_methods(simple_input_with_retries)
    copy = a.copy()
    first_auth = copy.next()
    second_auth = copy.next()
    assert first_auth is second_auth


def test_example_input_first_auth_retries_next_protocol(simple_input_with_retries):
    a = authen.AuthMethodList(ssh=True, api=False, telnet=False)
    a.load_authentication_methods(simple_input_with_retries)
    copy = a.copy()
    first_auth = copy.next()
    second_auth = copy.next_protocol()
    assert first_auth is second_auth


def test_example_exhausted_list(simple_input):
    a = authen.AuthMethodList(ssh=True, api=False, telnet=False)
    a.load_authentication_methods(simple_input)
    copy = a.copy()
    copy.next()
    copy.next()
    copy.next()
    assert copy.next() is None


def test_example_keep_score(simple_input):
    a = authen.AuthMethodList(ssh=True, api=False, telnet=False, keep_score=True)
    a.load_authentication_methods(simple_input)
    copy = a.copy()
    assert [a.name for a in copy.authlist] == ["version2", "userpass2", "userpass1"]
    copy.next()
    copy.next()
    copy = a.copy()
    assert ["version2", "userpass1", "userpass2"] == [a.name for a in copy.authlist]
