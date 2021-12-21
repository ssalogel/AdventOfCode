from src.AoC2015.Day5 import Day5
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ('aei', True),
    ('xazegov', True),
    ('aeiouaeiouaeiou', True),
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', True),
    ('haegwjzuvuyypxyu', True),
    ('dvszwmarrgswjxmb', False)
])
def test_has_at_least_three_vowels(test_input, expected):
    assert Day5(content='test').has_at_least_three_vowels(string=test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('xx', True),
    ('abcdde', True),
    ('aabbccdd', True),
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', False),
    ('haegwjzuvuyypxyu', True),
    ('dvszwmarrgswjxmb', True)
])
def test_has_at_least_one_double_letter(test_input, expected):
    assert Day5(content='test').has_at_least_one_double_letter(string=test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('xx', True),
    ('abcdde', False),
    ('aabbccdd', False),
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', True),
    ('haegwjzuvuyypxyu', False),
    ('dvszwmarrgswjxmb', True)
])
def test_does_not_contain_forbidden_strings(test_input, expected):
    assert Day5(content='test').does_not_contain_forbidden_strings(string=test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('xyxy', True),
    ('aabcdefgaa', True),
    ('aaa', False),
    ('qjhvhtzxzqqjkmpb', True),
    ('xxyxx', True),
    ('uurcxstgmygtbstg', True),
    ('ieodomkazucvgmuy', False)
])
def test_has_repeating_pair_no_overlaps(test_input, expected):
    assert Day5(content='test').has_repeating_pair_no_overlap(string=test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('xyx', True),
    ('abcdefeghi', False),
    ('aaa', False),
    ('qjhvhtzxzqqjkmpb', True),
    ('xxyxx', True),
    ('uurcxstgmygtbstg', False),
    ('ieodomkazucvgmuy', True)
])
def repeat_letter_with_one_between(test_input, expected):
    assert Day5(content='test').repeat_letter_with_one_between(string=test_input) == expected


def test_part1():
    test_input = '\n'.join(["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"])
    d = Day5(content="test")
    assert d.part1(d.parse_content(test_input)) == 2


def test_part2():
    test_input = '\n'.join(["aaa", "qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"])
    d = Day5(content="test")
    assert d.part2(d.parse_content(test_input)) == 2


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day5.txt', 'r') as file:
        content = file.read().strip()
    d = Day5(content="test")
    assert d.part1(d.parse_content(content)) == 236
    assert d.part2(d.parse_content(content)) == 51
