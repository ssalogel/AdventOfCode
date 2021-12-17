from AdventUtils.Day import Day
from math import floor, ceil


class Day7(Day):
    def __init__(self, content=None):
        super().__init__(day=7, year=2021, content=content)

    def parse_content(self, content: str):
        return [int(x) for x in content.strip().split(',')]

    def part1(self, parsed_content) -> int:
        positions = list(sorted(parsed_content))
        return sum(map(lambda x: abs(x - positions[len(positions)//2]), positions))

    def part2(self, parsed_content) -> int:
        pos = sum(parsed_content)/len(parsed_content)
        floor_fuel = sum((abs(x - floor(pos)) * (abs(x - floor(pos)) + 1)) // 2 for x in parsed_content)
        ceil_fuel = sum((abs(x - ceil(pos)) * (abs(x - ceil(pos)) + 1)) // 2 for x in parsed_content)
        return floor_fuel if floor_fuel < ceil_fuel else ceil_fuel


if __name__ == '__main__':
    content = """16,1,2,0,4,2,7,1,2,14
"""
    d = Day7(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))
