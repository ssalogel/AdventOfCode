from dataclasses import dataclass
from typing import Tuple
from collections import defaultdict


@dataclass(frozen=True, eq=True)
class Position2D:
    x: int = 0
    y: int = 0

    def move_up(self):
        return Position2D(self.x, self.y + 1)

    def move_down(self):
        return Position2D(self.x, self.y - 1)

    def move_left(self):
        return Position2D(self.x - 1, self.y)

    def move_right(self):
        return Position2D(self.x + 1, self.y)


class Grid2DBool:
    def __init__(self):
        self.grid: dict[Tuple[int, int], bool] = {}

    def turn_on(self, pos: Tuple[int, int]):
        self.grid[pos] = True

    def turn_off(self, pos: Tuple[int, int]):
        self.grid[pos] = False

    def toggle(self, pos: Tuple[int, int]):
        self.grid[pos] = not self.grid.get(pos, False)


class Grid2Dint:
    def __init__(self):
        self.grid: dict[Tuple[int, int], int] = defaultdict(lambda: 0)

    def turn_on(self, pos: Tuple[int, int]):
        self.grid[pos] += 1

    def turn_off(self, pos: Tuple[int, int]):
        if self.grid[pos] > 0:
            self.grid[pos] -= 1

    def toggle(self, pos: Tuple[int, int]):
        self.grid[pos] += 2
