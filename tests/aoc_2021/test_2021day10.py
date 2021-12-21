from src.AoC2021.Day10 import Day10


def test_part1():
    test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    d = Day10(content="test")
    assert d.part1(d.parse_content(test_input)) == 26397


def test_part2():
    test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    d = Day10(content="test")
    assert d.part2(d.parse_content(test_input)) == 288957


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day10.txt', 'r') as file:
        content = file.read().strip()
    d = Day10(content="test")
    assert d.part1(d.parse_content(content)) == 278475
    assert d.part2(d.parse_content(content)) == 3015539998
