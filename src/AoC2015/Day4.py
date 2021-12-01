from AdventUtils.Day import Day
from AdventUtils.Crypto import find_hash


class Day4(Day):
    def __init__(self, content=None):
        super().__init__(day=4, year=2015, content=content)

    def parse_content(self) -> str:
        return self.content.strip()

    def part1(self) -> int:
        return find_hash(self.data_p1, '00000')[0][0]

    def part2(self) -> int:
        return find_hash(self.data_p2, '000000')[0][0]
