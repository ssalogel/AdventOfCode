from AdventUtils.Day import Day
from AdventUtils.Crypto import find_hash


class Day4(Day):
    def __init__(self, content=None):
        super().__init__(day=4, year=2015, content=content)

    def parse_content(self, content: str) -> str:
        return content.strip()

    def part1(self, parsed_content: str) -> int:
        return find_hash(parsed_content, '00000')[0][0]

    def part2(self, parsed_content: str) -> int:
        return find_hash(parsed_content, '000000')[0][0]
