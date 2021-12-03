from AdventUtils.Day import Day


class Day2(Day):
    def __init__(self, content=None):
        super().__init__(day=2, year=2021, content=content)

    def parse_content(self) -> list[tuple[str, int]]:
        return [(d, int(m)) for d, m in (d.split(' ') for d in self.content.split('\n'))]

    def part1(self) -> int:
        pos, depth = 0, 0
        for d, m in self.data_p1:
            if d == 'forward':
                pos += m
            elif d == 'up':
                depth -= m
            elif d == 'down':
                depth += m
            else:
                raise NotImplementedError
        return pos * depth

    def part2(self) -> int:
        pos, depth, aim = 0, 0, 0
        for d, m in self.data_p1:
            if d == 'forward':
                pos += m
                depth += aim * m
            elif d == 'up':
                aim -= m
            elif d == 'down':
                aim += m
            else:
                raise NotImplementedError
        return pos * depth
