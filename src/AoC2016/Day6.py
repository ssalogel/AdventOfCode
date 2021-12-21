from src.AdventUtils.Day import Day
from collections import Counter


class Day6(Day):
    def __init__(self, content=None):
        super().__init__(day=6, year=2016, content=content)

    def parse_content(self, content: str) -> list[str]:
        return content.split('\n')

    def part1(self, parsed_content: list[str]) -> str:
        res: list[str] = []
        for c in zip(*parsed_content):
            res.append(Counter(c).most_common(1)[0][0])
        return ''.join(res)

    def part2(self, parsed_content: list[str]) -> str:
        res: list[str] = []
        for c in zip(*parsed_content):
            res.append(Counter(c).most_common().pop()[0])
        return ''.join(res)
