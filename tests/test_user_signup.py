import pytest


def test_sign_up_positive(user_fixture):
    print("Signup test positive")
    user_fixture.name = "hello"
    assert user_fixture.name == "hello"


@pytest.mark.xfail
def test_sign_up_negative(user_fixture):
    print("Signup test negative")
    assert user_fixture.name != "ausername"
