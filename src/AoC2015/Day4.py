from AdventUtils.Day import Day
from hashlib import md5


class Day4(Day):
    def __init__(self, content=None):
        super().__init__(day=4, year=2015, content=content)

    def parse_content(self) -> str:
        return self.content.strip()

    def part1(self) -> int:
        x = 0
        while True:
            if md5((self.data_p1 + str(x)).encode()).hexdigest().startswith('00000'):
                return x
            x += 1

    def part2(self) -> int:
        x = 0
        while True:
            if md5((self.data_p1 + str(x)).encode()).hexdigest().startswith('000000'):
                return x
            x += 1
