from AdventUtils.Crypto import rot13, find_hash
import pytest


@pytest.mark.parametrize("test_input, expected", [
    ('hello', 'uryyb'),
    ('abcdefghijklmnopqrstuvwxyz', 'nopqrstuvwxyzabcdefghijklm')
])
def test_rot13(test_input, expected):
    assert rot13(test_input) == expected


@pytest.mark.parametrize("test_input, mag, expected", [
    ('hello', 14, 'vszzc'),
    ('abcdefghijklmnopqrstuvwxyz', 12, 'mnopqrstuvwxyzabcdefghijkl')
])
def test_rot13_mag(test_input, mag, expected):
    assert rot13(test_input, mag) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("abcdef", 609043),
    ("pqrstuv", 1048970),

])
def test_find_hash(test_input, expected):
    assert find_hash(test_input, '00000')[0][0] == expected
