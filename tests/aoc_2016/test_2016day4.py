from AoC2016.Day4 import Day4
import pytest


@pytest.mark.parametrize("name, checksum,expected", [
    ("aaaaabbbzyx", "abxyz", True),
    ("abcdefgh", "abcde", True),
    ("notarealroom", "oarel", True),
    ("totallyrealroom", "decoy", False)
])
def test_is_valid(name, checksum, expected):
    print(name, checksum, Day4(content='aaaaa-bbb-z-y-x-123[abxyz]').is_valid(name, checksum))
    assert Day4(content='aaaaa-bbb-z-y-x-123[abxyz]').is_valid(name, checksum) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("aaaaa-bbb-z-y-x-123[abxyz]", 123),
    ("a-b-c-d-e-f-g-h-987[abcde]", 987),
    ("not-a-real-room-404[oarel]", 404),
    ("totally-real-room-200[decoy]", 0)
])
def test_part_1(test_input, expected):
    assert Day4(content=test_input).part1() == expected


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day4.txt', 'r') as file:
        content = file.read().strip()
    assert Day4(content=content).part1() == 173787
    assert Day4(content=content).part2() == 548