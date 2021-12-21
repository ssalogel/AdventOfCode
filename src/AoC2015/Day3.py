from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import Position2D


class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2015, content=content)

    def parse_content(self, content: str) -> str:
        return content.strip()

    @classmethod
    def move(cls, move: str, pos: Position2D) -> Position2D:
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

    def part1(self, parsed_content: str) -> int:
        curr = Position2D(0, 0)
        visited = {curr}
        for move in parsed_content:
            curr = self.move(move, curr)
            visited.add(curr)
        return len(visited)

    def part2(self, parsed_content: str) -> int:
        santa = Position2D(0, 0)
        robot = Position2D(0, 0)
        visited = {santa, robot}
        for move in parsed_content[::2]:
            santa = self.move(move, santa)
            visited.add(santa)
        for move in parsed_content[1::2]:
            robot = self.move(move, robot)
            visited.add(robot)
        return len(visited)
