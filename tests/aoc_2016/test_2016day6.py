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
    d = Day6(content="test")
    assert d.part1(d.parse_content(content)) == "easter"


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
    d = Day6(content="test")
    assert d.part2(d.parse_content(content)) == "advent"


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day6.txt', 'r') as file:
        content = file.read().strip()
    d = Day6(content="test")
    assert d.part1(d.parse_content(content)) == "liwvqppc"
    assert d.part2(d.parse_content(content)) == "caqfbzlh"
