from src.AoC2021.Day4 import Day4


def test_part1():
    test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    d = Day4(content="test")
    assert d.part1(d.parse_content(test_input)) == 4512


def test_part2():
    test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    d = Day4(content="test")
    assert d.part2(d.parse_content(test_input)) == 1924


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day4.txt', 'r') as file:
        content = file.read().strip()
    d = Day4(content="test")
    assert d.part1(d.parse_content(content)) == 74320
    assert d.part2(d.parse_content(content)) == 17884
