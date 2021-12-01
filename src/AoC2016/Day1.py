from AdventUtils.Day import Day
from AdventUtils.Grid2D import WalkingPosition


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2016, content=content)

    def parse_content(self) -> list[tuple[str, int]]:
        return [(d[0], int(d[1:])) for d in self.content.split(', ')]

    def part1(self) -> int:
        walker = WalkingPosition()
        for turn, mag in self.data_p1:
            if turn == 'R':
                walker.turn_right()
            else:
                walker.turn_left()
            walker.move_forward(mag)
        return abs(walker.pos.x) + abs(walker.pos.y)

    def part2(self) -> int:
        walker = WalkingPosition()
        visited = {walker.pos}
        for turn, mag in self.data_p1:
            if turn == 'R':
                walker.turn_right()
            else:
                walker.turn_left()
            for _ in range(mag):
                walker.move_forward()
                if walker.pos in visited:
                    return abs(walker.pos.x) + abs(walker.pos.y)
                else:
                    visited.add(walker.pos)
        return -1
