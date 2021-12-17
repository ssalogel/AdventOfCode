from AdventUtils.Day import Day
from AdventUtils.Grid2D import get_neighbours_dig


class Day11(Day):
    def __init__(self, content=None):
        super().__init__(day=11, year=2021, content=content)

    def parse_content(self, content: str) -> list[list[int]]:
        res = []
        for line in content.strip().split('\n'):
            res.append([int(c) for c in line])
        return res

    def step(self, grid: list[list[int]]) -> tuple[list[list[int]], int]:
        for ix, row in enumerate(grid):
            for jx, v in enumerate(row):
                grid[ix][jx] += 1

        changed = True
        flashed = set()
        while changed:
            changed = False
            for ix, row in enumerate(grid):
                for jx, v in enumerate(row):
                    if v >= 10 and (ix, jx) not in flashed:
                        changed = True
                        flashed.add((ix, jx))
                        for x, y in get_neighbours_dig(ix, jx, len(grid), len(grid[0])):
                            grid[x][y] += 1

        for x, y in flashed:
            grid[x][y] = 0
        return grid, len(flashed)

    def part1(self, parsed_content) -> int:
        tot_flashes = 0
        for _ in range(100):
            parsed_content, flashes = self.step(parsed_content)
            tot_flashes += flashes
        return tot_flashes

    def part2(self, parsed_content) -> int:
        tot_step = 0
        sync = False
        while not sync:
            parsed_content, flashes = self.step(parsed_content)
            tot_step += 1
            if flashes == 100:
                sync = True
        return tot_step


if __name__ == '__main__':
    content = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
    d = Day11(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))
