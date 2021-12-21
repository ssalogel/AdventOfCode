from src.AdventUtils import Math
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


@pytest.mark.parametrize("test_input, expected", [
    (52, [1, 2, 4, 13, 26, 52]),
    (1, [1]),
    (17, [1, 17]),
    (12, [1, 2, 3, 4, 6, 12])
])
def test_divisors(test_input, expected):
    assert Math.divisors(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    (52, [1, 2, 4, 13, 26, 52]),
    (1, [1]),
    (17, [1, 17]),
    (12, [1, 2, 3, 4, 6, 12])
])
def test_magic_divisors(test_input, expected):
    assert sorted(Math.magic_divisors(test_input)) == expected


@pytest.mark.parametrize("target, nums, expected", [
    (10, range(1, 11), 1),
    (10, range(1, 10), 4)
])
def test_(target, nums, expected):
    assert len(Math.get_subsets_min_len_sum_target(target=target, nums=nums)) == expected
