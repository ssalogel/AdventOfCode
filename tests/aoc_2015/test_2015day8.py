from AoC2015.Day8 import Day8
import pytest


@pytest.mark.parametrize("test_input,expected", [
    (r'""', 2),
    (r'"abc"', 5),
    (r'"aaa\"aaa"', 10),
    (r'"\x27"', 6),
])
def test_calc_num_of_coded_chars(test_input, expected):
    assert Day8(content='test').calc_num_of_coded_chars(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (r'""', 0),
    (r'"abc"', 3),
    (r'"aaa\"aaa"', 7),
    (r'"\x27"', 1),
])
def test_calc_actual_str_len(test_input, expected):
    assert Day8(content='test').calc_actual_str_len(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (r'""', 6),
    (r'"abc"', 9),
    (r'"aaa\"aaa"', 16),
    (r'"\x27"', 11),
])
def test_calc_encoded_str_len(test_input, expected):
    assert Day8(content='test').calc_encoded_str_len(test_input) == expected


def test_part1():
    content = r'''""
"abc"
"aaa\"aaa"
"\x27"'''
    assert Day8(content=content).part1() == 12


def test_part2():
    content = r'''""
"abc"
"aaa\"aaa"
"\x27"'''
    assert Day8(content=content).part2() == 19


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day8.txt', 'r') as file:
        content = file.read().strip()
    assert Day8(content=content).part1() == 1350
    assert Day8(content=content).part2() == 2085
