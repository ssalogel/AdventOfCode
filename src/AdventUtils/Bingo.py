class Bingo:
    def __init__(self, board: list[list[int]]):
        self.numbers = {}
        for row in board:
            for num in row:
                self.numbers[num] = False
        self.boardsize = len(board)
        self.board = [num for row in board for num in row]

    def check_win_no_diag(self) -> bool:
        for start in range(self.boardsize):
            row = self.board[start*self.boardsize:start*self.boardsize + self.boardsize]
            if all(map(lambda x: self.numbers[x], row)):
                return True
            col = self.board[start:len(self.board):self.boardsize]
            if all(map(lambda x: self.numbers[x], col)):
                return True
        return False

    def add_number(self, num: int):
        self.numbers[num] = True

    def get_numbers_not_found(self) -> list[int]:
        return [k for k, v in self.numbers.items() if not v]
