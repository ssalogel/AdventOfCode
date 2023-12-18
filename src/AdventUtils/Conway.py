from abc import ABC, abstractmethod
from typing import Callable
from collections import defaultdict
from copy import deepcopy


class Conway(ABC):
    def __init__(self, to_on: Callable[[int], bool], to_off: Callable[[int], bool]):
        self.board: set[tuple[int, int]] = set()
        self.to_on: Callable[[int], bool] = to_on
        self.to_off: Callable[[int], bool] = to_off
        self.width: int = 0
        self.height: int = 0

    @abstractmethod
    def new_board(self, positions, width: int, height: int):
        pass

    @abstractmethod
    def step(self):
        pass


class FullBoardConway2D(Conway):
    """Conway game of life"""

    def new_board(
        self, positions: set[tuple[int, int]], width: int, height: int
    ) -> None:
        """positions are just to starting ON positions"""
        self.board: set[tuple[int, int]] = positions
        self.width = width
        self.height = height

    def get_neighbours(self, x, y):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return {
            (x + x_add, y + y_add)
            for x_add, y_add in offsets
            if x + x_add >= 0
            and x + x_add < self.width
            and y + y_add >= 0
            and y + y_add < self.height
        }

    def get_live_neighbours(self, x, y):
        possible = self.get_neighbours(x, y)
        alive = {p for p in possible if p in self.board}
        return alive, possible - alive

    def step(self) -> None:
        n_board = deepcopy(self.board)
        undead: dict[tuple[int, int], int] = defaultdict(int)
        for x, y in self.board:
            alive, dead = self.get_live_neighbours(x, y)
            if self.to_off(len(alive)):
                n_board.remove((x, y))
            for pos in dead:
                undead[pos] += 1
        for pos, nb_nei in undead.items():
            if self.to_on(nb_nei):
                n_board.add(pos)

        self.board = n_board

    def turn_on(self, positions: set[tuple[int, int]]) -> None:
        self.board.update(positions)
