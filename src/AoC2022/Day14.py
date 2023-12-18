from typing import Optional

from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import Position2D


class Day14(Day):
    def __init__(self, content=None):
        super().__init__(day=14, year=2022, content=content)

    def parse_content(self, content: str):
        return [
            [
                (int(a.split(",")[0]), int(a.split(",")[1]))
                for a in lines.strip().split(" -> ")
            ]
            for lines in content.strip().splitlines()
        ]

    def make_board(self, instrs: list[list[tuple[int, int]]]) -> set[Position2D]:
        blocks = set()
        for block in instrs:
            for source, dest in zip(block, block[1:]):
                if source[0] != dest[0]:
                    if source[0] < dest[0]:
                        for x in range(source[0], dest[0] + 1):
                            blocks.add(Position2D(x, source[1]))
                    else:
                        for x in range(dest[0], source[0] + 1):
                            blocks.add(Position2D(x, source[1]))
                else:
                    if source[1] < dest[1]:
                        for y in range(source[1], dest[1] + 1):
                            blocks.add(Position2D(source[0], y))
                    else:
                        for y in range(dest[1], source[1] + 1):
                            blocks.add(Position2D(source[0], y))
        return blocks

    def resting_place_generator(self, board: set[Position2D], floor: int):
        current = Position2D(500, 0)
        path = [current]
        while len(path) > 0:
            if current.y >= floor:
                break
            down = current.move_up()
            if down not in board:
                path.append(current)
                current = down
                path.append(down)
                continue
            downleft = down.move_left()
            if downleft not in board:
                path.append(current)
                current = downleft
                path.append(downleft)
                continue
            downright = down.move_right()
            if downright not in board:
                path.append(current)
                current = downright
                path.append(downright)
                continue
            else:
                yield current
                current = path.pop()

    def get_next_resting_place(
        self, board: set[Position2D], floor: int
    ) -> Optional[Position2D]:
        current = Position2D(500, 0)
        while True:
            if current.y >= floor:
                break
            down = current.move_up()
            if down not in board:
                current = down
                continue
            downleft = down.move_left()
            if downleft not in board:
                current = downleft
                continue
            downright = down.move_right()
            if downright not in board:
                current = downright
                continue
            else:
                return current

    def part1(self, parsed_content) -> int:
        board = self.make_board(parsed_content)
        starting_fill = len(board)
        floor = max(board, key=lambda p: p.y).y
        for pos in self.resting_place_generator(board, floor):
            if pos is not None:
                board.add(pos)
            else:
                break
        return len(board) - starting_fill

    def part2(self, parsed_content) -> int:
        board = self.make_board(parsed_content)
        floor = max(board, key=lambda p: p.y).y + 2
        for x in range(
            min(board, key=lambda p: p.x).x - (floor + 25),
            max(board, key=lambda p: p.x).x + floor + 25,
        ):
            board.add(Position2D(x, floor))
        starting_fill = len(board)
        for pos in self.resting_place_generator(board, floor + 10):
            board.add(pos)
        return len(board) - starting_fill


if __name__ == "__main__":
    input_content = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
    d = Day14(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
