from AdventUtils.Day import Day
from AdventUtils.Bingo import Bingo


Board = list[list[int]]


class Day4(Day):
    def __init__(self, content=None):
        super().__init__(day=4, year=2021, content=content)

    def parse_content(self, content: str) -> tuple[list[int], list[Board]]:
        data = content.replace('  ', ' ').split('\n\n')
        numbers = list(map(int, data.pop(0).split(',')))

        boards = [b.split('\n') for b in data]
        res = []
        for board in boards:
            n_board = []
            for row in board:
                n_board.append(list(map(int, row.strip().split(' '))))
            res.append(n_board)
        return numbers, res

    def part1(self, parsed_content: tuple[list[int], list[Board]]) -> int:
        draws, boards = parsed_content
        bingos = []
        for board in boards:
            bingos.append(Bingo(board))
        for draw in draws:
            for bingo in bingos:
                bingo.add_number(draw)
            winners = []
            for bingo in bingos:
                if bingo.check_win():
                    winners.append(bingo)
            if winners:
                return sum(winners[0].get_numbers_not_found()) * draw
        raise Exception

    def part2(self, parsed_content: tuple[list[int], list[Board]]) -> int:
        draws, boards = parsed_content
        bingos = []
        for board in boards:
            bingos.append(Bingo(board))
        for draw in draws:
            for bingo in bingos:
                bingo.add_number(draw)
            winners = []
            for bingo in bingos:
                if bingo.check_win():
                    winners.append(bingo)
                    if len(bingos) == 1:
                        return sum(bingos[0].get_numbers_not_found()) * draw
            for winner in winners:
                bingos.remove(winner)
        raise Exception
