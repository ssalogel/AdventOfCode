from AoC2015.Day21 import Day21


def test_play():
    assert Day21(content='test: 1').play(hp=8, att=5, defence=5, boss_hp=12, boss_att=7, boss_def=2)


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day21.txt', 'r') as file:
        content = file.read().strip()
    d = Day21(content="test")
    assert d.part1(d.parse_content(content)) == 91
    assert d.part2(d.parse_content(content)) == 158
