from AdventUtils.Day import Day


class Day9(Day):
    def __init__(self, content=None):
        super().__init__(day=9, year=2021, content=content)

    def parse_content(self, content: str):
        res = []
        for line in content.strip().split('\n'):
            res.append([])
            for char in line:
                res[-1].append(int(char))
        return res

    def find_low_points(self, grid: list[list[int]]) -> tuple[list[tuple[int, int]], list[int]]:
        low_points = []
        low_coords = []

        # do first row checks
        if grid[0][0] < grid[0][1] and grid[0][0] < grid[1][0]:
            low_points.append(grid[0][0])
            low_coords.append((0, 0))
        for ix, point in enumerate(grid[0][1:-1]):
            if point < grid[0][ix] and point < grid[0][ix + 2] and point < grid[1][ix + 1]:
                low_points.append(point)
                low_coords.append((0, ix+1))
        if grid[0][-1] < grid[0][-2] and grid[0][-1] < grid[1][-1]:
            low_points.append(grid[0][-1])
            low_coords.append((0, len(grid[0])-1))

        # do all middle rows checks
        for rx, row in enumerate(grid):
            if rx == 0 or rx == len(grid) - 1:
                continue
            for ix, point in enumerate(row):
                if ix == 0 and point < grid[rx - 1][ix] and point < grid[rx + 1][ix] and point < \
                        row[ix + 1]:
                    low_points.append(point)
                    low_coords.append((rx, ix))
                    continue
                if ix == len(row) - 1 and point < grid[rx - 1][ix] and point < grid[rx + 1][
                        ix] and point < row[ix - 1]:
                    low_points.append(point)
                    low_coords.append((rx, ix))
                    continue
                if point < grid[rx - 1][ix] and point < grid[rx + 1][ix] \
                        and point < row[ix - 1] and point < row[ix + 1]:
                    low_points.append(point)
                    low_coords.append((rx, ix))

        # de last row checks
        if grid[-1][0] < grid[-1][1] and grid[-1][0] < grid[-2][0]:
            low_points.append(grid[-1][0])
            low_coords.append((len(grid) - 1, 0))
        for ix, point in enumerate(grid[-1][1:-1]):
            if point < grid[-1][ix] and point < grid[-1][ix + 2] and point < grid[-2][ix + 1]:
                low_points.append(point)
                low_coords.append((len(grid) - 1, ix+1))
        if grid[-1][-1] < grid[-1][-2] and grid[-1][-1] < grid[-2][0]:
            low_points.append(grid[-1][0])
            low_coords.append((len(grid) - 1, len(grid[0]) - 1))
        return low_coords, low_points

    def get_bassin(self, low_point: tuple[int, int], grid: list[list[int]]) -> set[tuple[int, int]]:
        width = len(grid[0])
        height = len(grid)

        def get_neighboors(x: int, y: int, width: int, height: int) -> list[tuple[int, int]]:
            neighbours = []
            if x - 1 >= 0:
                neighbours.append((x-1, y))
            if x + 1 < height:
                neighbours.append((x+1, y))
            if y - 1 >= 0:
                neighbours.append((x, y-1))
            if y + 1 < width:
                neighbours.append((x, y+1))
            return neighbours

        walls = set()
        visited = set()
        to_visit = {(low_point[0], low_point[1])}
        while len(to_visit) != 0:
            x, y = to_visit.pop()
            nei = get_neighboors(x, y, width, height)
            visited.add((x, y))
            for n in nei:
                if n not in walls and n not in visited and n not in to_visit:
                    if grid[n[0]][n[1]] == 9:
                        walls.add(n)
                        continue
                    to_visit.add(n)
        return visited

    def part1(self, parsed_content) -> int:
        _, low_points = self.find_low_points(parsed_content)
        return sum(x + 1 for x in low_points)

    def part2(self, parsed_content) -> int:
        low_coords, _ = self.find_low_points(parsed_content)
        bassins = [self.get_bassin(low_point, parsed_content) for low_point in low_coords]
        bassins_value = [len(bassin) for bassin in bassins]
        bassins_value.sort(reverse=True)
        return bassins_value[0] * bassins_value[1] * bassins_value[2]


if __name__ == '__main__':
    content = """2199943210
3987894921
9856789892
8767896789
9899965678
"""
    d = Day9(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))
