from dataclasses import dataclass
from typing import Tuple
from collections import defaultdict
from enum import Enum, auto


def get_neighbours_dig(x, y, width, height):
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return {
        (x + x_add, y + y_add)
        for x_add, y_add in offsets
        if x + x_add >= 0
        and x + x_add < width
        and y + y_add >= 0
        and y + y_add < height
    }


def get_neighbours_dig_with_self_unbound(x, y):
    offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    return [(x + x_add, y + y_add) for x_add, y_add in offsets]


def get_neighbours(x, y, width, height) -> set[tuple[int, int]]:
    offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    return {
        (x + x_add, y + y_add)
        for x_add, y_add in offsets
        if x + x_add >= 0
        and x + x_add < width
        and y + y_add >= 0
        and y + y_add < height
    }


def manhatthan_dist(start: tuple[int, int], end: tuple[int, int]):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def manhatthan_dist_pos(start: "Position2D", end: "Position2D"):
    return abs(start.x - end.x) + abs(start.y - end.y)


@dataclass(frozen=True, eq=True)
class Position2D:
    x: int = 0
    y: int = 0

    def move_up(self, magnitude=1) -> "Position2D":
        return Position2D(self.x, self.y + magnitude)

    def move_down(self, magnitude=1) -> "Position2D":
        return Position2D(self.x, self.y - magnitude)

    def move_left(self, magnitude=1) -> "Position2D":
        return Position2D(self.x - magnitude, self.y)

    def move_right(self, magnitude=1) -> "Position2D":
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
    def __init__(self, neutral_value: int = 0):
        self.grid: dict[Tuple[int, int], int] = defaultdict(lambda: neutral_value)

    def turn_on(self, pos: Tuple[int, int]):
        self.grid[pos] += 1

    def turn_off(self, pos: Tuple[int, int]):
        if self.grid[pos] > 0:
            self.grid[pos] -= 1

    def toggle(self, pos: Tuple[int, int]):
        self.grid[pos] += 2
