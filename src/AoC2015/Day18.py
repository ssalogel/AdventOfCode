from AdventUtils.Day import Day
from AdventUtils.Conway import FullBoardConway2D


class Day18(Day):
    def __init__(self, content=None):
        super().__init__(day=18, year=2015, content=content)

    def parse_content(self, content: str) -> list[list[bool]]:
        data = content.strip().split('\n')
        return [list(map(lambda x: x == '#', d)) for d in data]

    def create_board(self, starting_board: list[list[bool]]) -> FullBoardConway2D:
        on_pos = set()
        for i, row in enumerate(starting_board):
            for j, v in enumerate(row):
                if v:
                    on_pos.add((j, i))
        game = FullBoardConway2D(to_on=lambda x: x == 3, to_off=lambda x: x < 2 or x > 3)
        game.new_board(on_pos, height=len(starting_board), width=len(starting_board[0]))
        return game

    def part1(self, parsed_content: list[list[bool]]) -> int:
        game = self.create_board(parsed_content)
        for i in range(100):
            game.step()
        return len(game.board)

    def part2(self, parsed_content: list[list[bool]]) -> int:
        game = self.create_board(parsed_content)
        stuck_on = set([(0, 0), (0, game.height-1), (game.width-1, 0), (game.width-1, game.height-1)])
        game.turn_on(stuck_on)
        for i in range(100):
            game.step()
            game.turn_on(stuck_on)
        return len(game.board)
