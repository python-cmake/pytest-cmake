import pytest

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 2 == 3

@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 10),
    (10, 5, 15),
    (0, 0, 0),
])
def test_addition_with_params(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize("input", [
    "\x17",
])
def test_byte_char_conversion(input):
    assert ord(input) < 128
