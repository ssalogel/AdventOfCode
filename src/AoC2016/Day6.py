from AdventUtils.Day import Day
from collections import Counter


class Day6(Day):
    def __init__(self, content=None):
        super().__init__(day=6, year=2016, content=content)

    def parse_content(self) -> list[str]:
        return self.content.split('\n')

    def part1(self) -> str:
        res: list[str] = []
        for c in zip(*self.data_p1):
            res.append(Counter(c).most_common(1)[0][0])
        return ''.join(res)

    def part2(self) -> str:
        res: list[str] = []
        for c in zip(*self.data_p1):
            res.append(Counter(c).most_common().pop()[0])
        return ''.join(res)
