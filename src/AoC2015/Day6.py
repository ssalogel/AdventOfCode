from AdventUtils.Day import Day
from AdventUtils.Grid2D import Grid2DBool, Grid2Dint

from typing import Tuple, Protocol, Any


class Grid(Protocol):
    grid: dict[Tuple[int, int], Any]

    def turn_on(self, pos: Tuple[int, int]):
        pass

    def turn_off(self, pos: Tuple[int, int]):
        pass

    def toggle(self, pos: Tuple[int, int]):
        pass


class Day6(Day):
    def __init__(self, content=None):
        super().__init__(day=6, year=2015, content=content)

    def parse_content(self):
        data = self.content.replace('turn ', '').split('\n')
        res = []

        def make_coord(coord: str):
            coord_split: list[str] = coord.split(',')
            return int(coord_split[0]), int(coord_split[1])

        for row in data:
            cells = row.split(' ')
            cells[1] = make_coord(cells[1])
            cells[3] = make_coord(cells[3])
            cells.pop(2)
            res.append(cells)

        return res

    def apply(self, instructions, grid: Grid) -> Grid:
        for instruct in instructions:
            for i in range(instruct[1][0], instruct[2][0] + 1):
                for j in range(instruct[1][1], instruct[2][1] + 1):
                    if instruct[0] == 'on':
                        grid.turn_on((i, j))
                    elif instruct[0] == 'off':
                        grid.turn_off((i, j))
                    elif instruct[0] == 'toggle':
                        grid.toggle((i, j))
                    else:
                        raise NotImplementedError
        return grid

    def part1(self) -> int:
        grid: Grid = Grid2DBool()
        grid = self.apply(self.data_p1, grid)
        return sum(grid.grid.values())

    def part2(self) -> int:
        grid: Grid = Grid2Dint()
        grid = self.apply(self.data_p2, grid)
        return sum(grid.grid.values())
