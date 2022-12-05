from src.AdventUtils.Day import Day
import re
from collections import namedtuple

Assignment = namedtuple("Assignment", ["x1", "x2", "y1", "y2"])


class Day4(Day):
    # if big ranges
    def __init__(self, content=None):
        super().__init__(day=4, year=2022, content=content)

    def parse_content(self, content: str) -> list[Assignment]:
        res = []
        for line in content.strip().splitlines():
            x1, x2, y1, y2 = map(int, re.match(R"(\d+)-(\d+),(\d+)-(\d+)", line).groups())
            res.append(Assignment(x1=x1, x2=x2, y1=y1, y2=y2))
        return res

    def part1(self, parsed_content: list[Assignment]) -> int:
        return sum([1 for ass in parsed_content if
                    (ass.x1 <= ass.y1 and ass.x2 >= ass.y2) or (ass.y1 <= ass.x1 and ass.y2 >= ass.x2)])

    def part2(self, parsed_content: list[Assignment]) -> int:
        return sum([1 for ass in parsed_content if not (ass.x1 > ass.y2 or ass.x2 < ass.y1)])


class Day4SmallInputs(Day):
    Range = set[int]
    Assignment = tuple[Range, Range]

    def __init__(self, content=None):
        super().__init__(day=4, year=2022, content=content)

    def parse_content(self, content: str) -> list[Assignment]:
        res = []
        for line in content.strip().splitlines():
            x1, x2, y1, y2 = map(int, re.match(R"(\d+)-(\d+),(\d+)-(\d+)", line).groups())
            res.append((set(range(x1, x2 + 1)), set(range(y1, y2 + 1))))
        return res

    def part1(self, parsed_content: list[Assignment]) -> int:
        return sum(1 for x, y in parsed_content if len(x | y) == max(len(x), len(y)))

    def part2(self, parsed_content: list[Assignment]) -> int:
        return sum(1 for x, y in parsed_content if len(x & y) > 0)


if __name__ == '__main__':
    input_content = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
    d = Day4(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
