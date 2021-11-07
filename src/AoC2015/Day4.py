from AdventUtils.Day import Day
from hashlib import md5


class Day4(Day):
    def __init__(self, content=None):
        super().__init__(day=4, year=2015, content=content)

    def parse_content(self) -> str:
        return self.content.strip()

    def find_hash(self, start: str, pattern: str) -> int:
        x = 0
        while True:
            if md5((start + str(x)).encode()).hexdigest().startswith(pattern):
                return x
            x += 1

    def part1(self) -> int:
        return self.find_hash(self.data_p1, '00000')

    def part2(self) -> int:
        return self.find_hash(self.data_p2, '000000')
