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
