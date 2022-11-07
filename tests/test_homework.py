from pytest import mark, param

#
# homework#2 create positive and negative tests for main python types: int,
#   float, bool, strings, lists, tuples, dicts
#


@mark.parametrize(
    ("a", "type_"),
    [
        (1, int),
        (3123455, int),
        (0.23123, float),
        (1.1, float),
        (True, bool),
        (False, bool),
        ("a string", str),
        ("x", str),
        ([1, 2, 3, 4], list),
        ([x*2 for x in range(100)], list),
        (list("abcdefg"), list),
        ((1, 2, 3, 4), tuple),
        (tuple([x*2 for x in range(100)]), tuple),
        ({"a": 123, "b": 456, "c": 789}, dict),
        ({k: k*2 for k in range(100)}, dict),

        param(1, float, marks=mark.xfail(reason="int is not a float")),
        param(3123455, tuple, marks=mark.xfail(reason="int is not a tuple")),
        param(0.23123, int, marks=mark.xfail(reason="float is not an int")),
        param(1.1, str, marks=mark.xfail(reason="float is not a str")),
        param(True, dict, marks=mark.xfail(reason="bool is not a dict")),
        param(False, int, marks=mark.xfail(reason="bool is not an int")),
        param("a string", list, marks=mark.xfail(reason="str is not a list")),
        param("x", float, marks=mark.xfail(reason="str is not a float")),
        param([1, 2, 3, 4], tuple,
              marks=mark.xfail(reason="list is not a tuple")),
        param([x*2 for x in range(100)], str,
              marks=mark.xfail(reason="list is not a str")),
        param(list("abcdefg"), bool,
              marks=mark.xfail(reason="list is not a bool")),
        param((1, 2, 3, 4), list,
              marks=mark.xfail(reason="tuple is not a list")),
        param(tuple([x*2 for x in range(100)]), int,
              marks=mark.xfail(reason="tuple is not an int")),
        param({"a": 123, "b": 456, "c": 789}, float,
              marks=mark.xfail(reason="dict is not a float")),
        param({k: k*2 for k in range(100)}, bool,
              marks=mark.xfail(reason="dict is not a bool"))
    ]
)
def test_is_variable_correct_type(a, type_):
    assert type(a) is type_
