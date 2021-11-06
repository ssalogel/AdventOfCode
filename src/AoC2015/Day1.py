from AdventUtils.Day import Day


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2015, content=content)

    def parse_content(self) -> str:
        return self.content

    def part1(self) -> int:
        floor = 0
        for c in self.data_p1:
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            else:
                raise NotImplementedError
        return floor

    def part2(self) -> int:
        floor = 0
        for i, c in enumerate(self.data_p1):
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            else:
                raise NotImplementedError
            if floor < 0:
                return i + 1
        return floor
