from AoC2021.Day11 import Day11


def test_step():
    test_input = """11111
19991
19191
19991
11111"""
    d = Day11(content=test_input)
    grid, flashes = d.step(d.parse_content(test_input))
    assert grid == [[3, 4, 5, 4, 3],
                    [4, 0, 0, 0, 4],
                    [5, 0, 0, 0, 5],
                    [4, 0, 0, 0, 4],
                    [3, 4, 5, 4, 3]]
    assert flashes == 9


def test_part1():
    test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    d = Day11(content="test")
    assert d.part1(d.parse_content(test_input)) == 1656


def test_part2():
    test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    d = Day11(content="test")
    assert d.part2(d.parse_content(test_input)) == 195


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day11.txt', 'r') as file:
        content = file.read().strip()
    d = Day11(content="test")
    assert d.part1(d.parse_content(content)) == 1719
    assert d.part2(d.parse_content(content)) == 232
