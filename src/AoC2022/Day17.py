from __future__ import annotations

from typing import Sequence

from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import Position2D
from itertools import cycle, count
from sys import maxsize


def cycle_with_ix(winds: Sequence):
    ix = 0
    n = len(winds)
    while True:
        yield winds[ix], ix
        ix = (ix + 1) % n


class Polygon:
    def __init__(self, points: list[Position2D] = list):
        self.points: list[Position2D] = points

    def go_left(self) -> Polygon:
        return Polygon([p.move_left() for p in self.points])

    def go_right(self) -> Polygon:
        return Polygon([p.move_right() for p in self.points])

    def go_down(self) -> Polygon:
        return Polygon([p.move_down() for p in self.points])

    def get_leftest(self) -> int:
        return min(x.x for x in self.points)

    def get_rightest(self) -> int:
        return max(x.x for x in self.points)

    def get_lowest(self, col: int = None) -> int:
        try:
            return min(x.y for x in self.points if col is None or x.x == col)
        except ValueError:
            return maxsize

    def get_highest(self, col: int) -> int:
        try:
            return max(x.y for x in self.points if col == x.x)
        except ValueError:
            return -1

    def __repr__(self):
        return f"{self.points}"


class Shape:
    poly: Polygon

    def go_left(self, lim: int, board: set[Position2D]) -> bool:
        new_pos = self.poly.go_left()
        if new_pos.get_leftest() > lim and all(x not in board for x in new_pos.points):
            self.poly = new_pos
            return True
        return False

    def go_right(self, lim: int, board: set[Position2D]) -> bool:
        new_pos = self.poly.go_right()
        if new_pos.get_rightest() < lim and all(x not in board for x in new_pos.points):
            self.poly = new_pos
            return True
        return False

    def go_down(self, board: set[Position2D]) -> bool:
        new_pos = self.poly.go_down()
        if all(x not in board for x in new_pos.points):
            self.poly = new_pos
            return True
        return False

    def get_highest(self, col: int):
        return self.poly.get_highest(col)

    def get_positions(self):
        return self.poly.points

    def __repr__(self):
        return f"{type(self)}: {self.poly}"


class HLine(Shape):
    def __init__(self, lowest: int):
        self.poly = Polygon([Position2D(2 + i, lowest) for i in range(4)])


class Cross(Shape):
    def __init__(self, lowest: int):
        self.poly = Polygon(
            [
                Position2D(3, lowest),
                Position2D(2, lowest + 1),
                Position2D(3, lowest + 1),
                Position2D(4, lowest + 1),
                Position2D(3, lowest + 2),
            ]
        )


class L(Shape):
    def __init__(self, lowest: int):
        self.poly = Polygon(
            [Position2D(2 + i, lowest) for i in range(3)]
            + [Position2D(4, lowest + 1), Position2D(4, lowest + 2)]
        )


class VLine(Shape):
    def __init__(self, lowest: int):
        self.poly = Polygon([Position2D(2, lowest + i) for i in range(4)])


class Cube(Shape):
    def __init__(self, lowest: int):
        self.poly = Polygon(
            [
                Position2D(2, lowest),
                Position2D(3, lowest),
                Position2D(2, lowest + 1),
                Position2D(3, lowest + 1),
            ]
        )


class Cave:
    def __init__(self, winds: str):
        self.winds_gen = cycle_with_ix(winds)
        self.rock_gen = cycle_with_ix([HLine, Cross, L, VLine, Cube])
        self.width = 7
        self._floor = {Position2D(i, -1) for i in range(self.width)}
        self.occupied: set[Position2D] = {Position2D(i, -1) for i in range(self.width)}
        self.columns = [-1 for _ in range(self.width)]
        self.base: int = 0
        self._height = -1

    def _add_rock(self, rock: Shape):
        for p in rock.get_positions():
            self.occupied.add(p)
            self.columns[p.x] = max(self.columns[p.x], p.y)
            self._height = max(self._height, p.y)

    @property
    def height(self) -> int:
        return self._height + self.base + 1

    def drop_new_rock(self):
        shape_cls, rock_idx = next(self.rock_gen)
        rock: Shape = shape_cls((max(self.columns) + 4))
        while True:
            wind_dir, wind_idx = next(self.winds_gen)
            if wind_dir == ">":
                rock.go_right(self.width, self.occupied)
            elif wind_dir == "<":
                rock.go_left(-1, self.occupied)
            else:
                raise NotImplementedError
            if not rock.go_down(self.occupied):
                break
        self._add_rock(rock)
        return rock_idx, wind_idx


class Day17(Day):
    def __init__(self, content=None):
        super().__init__(day=17, year=2022, content=content)

    def parse_content(self, content: str):
        return content.strip()

    def part1(self, parsed_content):
        cave = Cave(parsed_content)
        for _ in range(2022):
            cave.drop_new_rock()
        return cave.height

    def part2(self, parsed_content) -> int:
        cave = Cave(parsed_content)
        target = 1_000_000_000_000
        states = {}
        jump_height = 0
        current_step = 0
        while current_step < target:
            rock_idx, wind_idx = cave.drop_new_rock()
            current_step += 1

            key = (rock_idx, wind_idx, tuple([i - cave.height for i in cave.columns]))
            if key in states:
                old_step, old_height = states[key]
                jump_step = current_step - old_step
                jumps = ((target - old_step) // jump_step) - 1
                current_step += jump_step * jumps
                jump_height = jumps * (cave.height - old_height)
                states = {}

            states[key] = (current_step, cave.height)
        return cave.height + jump_height


if __name__ == "__main__":
    input_content = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
    d = Day17(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
