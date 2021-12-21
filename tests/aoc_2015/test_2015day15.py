from src.AoC2015.Day15 import Day15


def test_part1():
    content = """a: capacity -1, durability -2, flavor 6, texture 3, calories 8"""
    dico = {'a': (-1, -2, 6, 3, 8),
            'b': (2, 3, -2, -1, 3)}
    cap, dur, fla, tex, _ = Day15(content=content).calc_ingredients(dico, [('a', 44), ('b', 56)])
    assert cap * dur * fla * tex == 62842880


def test_part2():
    content = """a: capacity -1, durability -2, flavor 6, texture 3, calories 8"""
    dico = {'a': (-1, -2, 6, 3, 8),
            'b': (2, 3, -2, -1, 3)}
    cap, dur, fla, tex, cal = Day15(content=content).calc_ingredients(dico, [('a', 40), ('b', 60)])
    assert cap * dur * fla * tex == 57600000


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day15.txt', 'r') as file:
        content = file.read().strip()
    d = Day15(content="test")
    assert d.part1(d.parse_content(content)) == 18965440
    assert d.part2(d.parse_content(content)) == 15862900
