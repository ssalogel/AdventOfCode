from AdventUtils import Math
import pytest


@pytest.mark.parametrize("op,mask,expected", [
    (123, 0xffff, 65412),
    (456, 0xffff, 65079)
])
def test_bitwise_not(op, mask, expected):
    assert Math.bitwise_not(op, mask) == expected


@pytest.mark.parametrize("op1, op2,mask,expected", [
    (123, 456, 0xffff, 507),
])
def test_bitwise_or(op1, op2, mask, expected):
    assert Math.bitwise_or(op1, op2, mask) == expected


@pytest.mark.parametrize("op1, op2,mask,expected", [
    (123, 456, 0xffff, 72),
])
def test_bitwise_and(op1, op2, mask, expected):
    assert Math.bitwise_and(op1, op2, mask) == expected


@pytest.mark.parametrize("op1, op2,mask,expected", [
    (123, 2, 0xffff, 492),
])
def test_bitwise_lshift(op1, op2, mask, expected):
    assert Math.bitwise_lshift(op1, op2, mask) == expected


@pytest.mark.parametrize("op1, op2,mask,expected", [
    (456, 2, 0xffff, 114),
])
def test_bitwise_rshift(op1, op2, mask, expected):
    assert Math.bitwise_rshift(op1, op2, mask) == expected
