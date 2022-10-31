from pytest import mark


# not a test
def somefunction():
    assert True is True


def test_always_passes():
    assert (1, 2, 3) == (1, 2, 3)


@mark.xfail
def test_always_failed():
    assert False


# not a test
def always_passes_test():
    assert True is True
