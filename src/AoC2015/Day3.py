from AdventUtils.Day import Day
from AdventUtils.Grid2D import Position2D


class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2015, content=content)

    def parse_content(self):
        return self.content.strip()

    @classmethod
    def move(cls, move: str, pos: Position2D):
        if move == '^':
            return pos.move_up()
        elif move == '<':
            return pos.move_left()
        elif move == '>':
            return pos.move_right()
        elif move == 'v':
            return pos.move_down()
        else:
            raise NotImplementedError

    def part1(self) -> int:
        curr = Position2D(0, 0)
        visited = {curr}
        for move in self.data_p1:
            curr = self.move(move, curr)
            visited.add(curr)
        return len(visited)

    def part2(self) -> int:
        santa = Position2D(0, 0)
        robot = Position2D(0, 0)
        visited = {santa, robot}
        for move in self.data_p2[::2]:
            santa = self.move(move, santa)
            visited.add(santa)
        for move in self.data_p2[1::2]:
            robot = self.move(move, robot)
            visited.add(robot)
        return len(visited)
