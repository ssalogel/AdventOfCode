from AoC2016.Day6 import Day6


def test_part1():
    content = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
    assert Day6(content=content).part1() == "easter"


def test_part2():
    content = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
    assert Day6(content=content).part2() == "advent"


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day6.txt', 'r') as file:
        content = file.read().strip()
    assert Day6(content=content).part1() == "liwvqppc"
    assert Day6(content=content).part2() == "caqfbzlh"
