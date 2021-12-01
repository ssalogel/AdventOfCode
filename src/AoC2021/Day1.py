from AdventUtils.Day import Day


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2021, content=content)

    def parse_content(self):
        return [int(x) for x in self.content.split('\n')]

    def part1(self) -> int:
        return sum(x < y for x, y in zip(self.data_p1, self.data_p1[1:]))


    def part2(self) -> int:
        return sum(x < y for x, y in zip(self.data_p1, self.data_p1[3:]))
