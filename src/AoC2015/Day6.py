from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import Grid2DBool, Grid2Dint

from typing import Protocol, Any


Coord = tuple[int, int]
Instruct = tuple[str, Coord, Coord]


class Grid(Protocol):
    grid: dict[Coord, Any]

    def turn_on(self, pos: Coord):
        pass

    def turn_off(self, pos: Coord):
        pass

    def toggle(self, pos: Coord):
        pass


class Day6(Day):
    def __init__(self, content=None):
        super().__init__(day=6, year=2015, content=content)

    def parse_content(self, content: str) -> list[Instruct]:
        data = content.replace("turn ", "").split("\n")
        res = []

        def make_coord(coord: str) -> tuple[int, int]:
            coord_split: list[str] = coord.split(",")
            return int(coord_split[0]), int(coord_split[1])

        for row in data:
            datum = row.split(" ")
            res.append((datum[0], make_coord(datum[1]), make_coord(datum[3])))
        return res

    def apply(self, instructions, grid: Grid) -> Grid:
        for instruct in instructions:
            for i in range(instruct[1][0], instruct[2][0] + 1):
                for j in range(instruct[1][1], instruct[2][1] + 1):
                    if instruct[0] == "on":
                        grid.turn_on((i, j))
                    elif instruct[0] == "off":
                        grid.turn_off((i, j))
                    elif instruct[0] == "toggle":
                        grid.toggle((i, j))
                    else:
                        raise NotImplementedError
        return grid

    def part1(self, parsed_content: list[Instruct]) -> int:
        grid: Grid = Grid2DBool()
        grid = self.apply(parsed_content, grid)
        return sum(grid.grid.values())

    def part2(self, parsed_content: list[Instruct]) -> int:
        grid: Grid = Grid2Dint()
        grid = self.apply(parsed_content, grid)
        return sum(grid.grid.values())
