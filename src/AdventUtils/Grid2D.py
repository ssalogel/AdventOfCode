from dataclasses import dataclass
from typing import Tuple
from collections import defaultdict
from enum import Enum, auto


@dataclass(frozen=True, eq=True)
class Position2D:
    x: int = 0
    y: int = 0

    def move_up(self, magnitude=1):
        return Position2D(self.x, self.y + magnitude)

    def move_down(self, magnitude=1):
        return Position2D(self.x, self.y - magnitude)

    def move_left(self, magnitude=1):
        return Position2D(self.x - magnitude, self.y)

    def move_right(self, magnitude=1):
        return Position2D(self.x + magnitude, self.y)


class WalkingPosition:
    class direction(Enum):
        NORTH = auto()
        EST = auto()
        SOUTH = auto()
        WEST = auto()

    def __init__(self):
        self.pos: Position2D = Position2D(0, 0)
        self.heading = self.direction.NORTH

    def turn_right(self):
        if self.heading == self.direction.NORTH:
            self.heading = self.direction.EST
        elif self.heading == self.direction.EST:
            self.heading = self.direction.SOUTH
        elif self.heading == self.direction.SOUTH:
            self.heading = self.direction.WEST
        elif self.heading == self.direction.WEST:
            self.heading = self.direction.NORTH

    def turn_left(self):
        for _ in range(3):
            self.turn_right()

    def move_forward(self, magnitude=1):
        if self.heading == self.direction.NORTH:
            self.pos = self.pos.move_up(magnitude)
        if self.heading == self.direction.EST:
            self.pos = self.pos.move_right(magnitude)
        if self.heading == self.direction.SOUTH:
            self.pos = self.pos.move_down(magnitude)
        if self.heading == self.direction.WEST:
            self.pos = self.pos.move_left(magnitude)


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
