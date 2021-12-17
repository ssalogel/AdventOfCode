from AoC2021.Day16 import Day16
import pytest


def test_get_type4():
    data = "101111111000101000"
    v, offset = Day16.get_type4(data)
    assert v == 2021
    assert offset == 15


@pytest.mark.parametrize("test_input,expected", [
    ("D2FE28", 6),
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31)
])
def test_part1(test_input, expected):
    d = Day16(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("D2FE28", 2021),
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1)
])
def test_part2(test_input, expected):
    d = Day16(content="test")
    assert d.part2(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day16.txt', 'r') as file:
        content = file.read().strip()
    d = Day16(content="test")
    assert d.part1(d.parse_content(content)) == 986
    assert d.part2(d.parse_content(content)) == 18234816469452
