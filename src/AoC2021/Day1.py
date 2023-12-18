from src.AdventUtils.Day import Day
from itertools import islice


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2021, content=content)

    def parse_content(self, content: str) -> list[int]:
        return [int(x) for x in content.split("\n")]

    def part1(self, parsed_content: list[int]) -> int:
        return sum(
            x < y for x, y in zip(parsed_content, islice(parsed_content, 1, None))
        )

    def part2(self, parsed_content: list[int]) -> int:
        return sum(
            x < y for x, y in zip(parsed_content, islice(parsed_content, 3, None))
        )
