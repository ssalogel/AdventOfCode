from src.AdventUtils.Day import Day
from functools import reduce
from operator import mul


class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2020, content=content)

    def parse_content(self, content: str):
        return content.splitlines()

    def part1(self, parsed_content) -> int:
        x = 0
        d_x = 3
        res = 0
        for row in parsed_content:
            if row[x] == '#':
                res += 1
            x = (x + d_x) % len(row)
        return res

    def part2(self, parsed_content) -> tuple[list[int], int]:
        checks = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        res = [0] * len(checks)
        for i, row in enumerate(parsed_content):
            for j, (d_x, d_y) in enumerate(checks):
                if (i % d_y) == 0:
                    x = ((i//d_y) * d_x) % len(row)
                    res[j] += row[x] == '#'
        return res, reduce(mul, res)


if __name__ == "__main__":
    input_content = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""
    d = Day3(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
