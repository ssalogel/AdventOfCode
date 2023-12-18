from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import manhatthan_dist

class Day11(Day):
    def __init__(self, content=None):
        super().__init__(day=11, year=2023, content=content)

    def parse_content(self, content: str):
        return content.strip().splitlines()

    def expand_universe1(self, graph):
        expanded_rows = []
        for row in graph:
            expanded_rows.append(row)
            if len(list(filter(lambda x: x != '.', row))) == 0:
                expanded_rows.append(row)
        expanded_cols = ['']*len(expanded_rows)
        for i in range(len(expanded_rows[0])):
            for j in range(len(expanded_rows)):
                expanded_cols[j] += expanded_rows[j][i]
            if len(list(filter(lambda x: x[i] != '.', expanded_rows))) == 0:
                for j in range(len(expanded_rows)):
                    expanded_cols[j] += expanded_rows[j][i]
        return expanded_cols

    def expand_universe_var(self, graph, var):
        expanded_rows = []
        for i, row in enumerate(graph):
            v = 1
            if len(list(filter(lambda x: x != '.', row))) == 0:
                v = var
            expanded_rows.append([v]*len(row))
        expanded_cols = [[] for _ in range(len(graph[0]))]
        for i in range(len(expanded_rows[0])):
            v = 1
            if len(list(filter(lambda x: x[i] != '.', graph))) == 0:
                v = var
            for j in range(len(expanded_rows)):
                expanded_cols[j].append((v, expanded_rows[j][i]))
        return expanded_cols

    def get_galaxy(self, grid):
        galaxy = []
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if '#' == col:
                    galaxy.append((j, i))
        return galaxy

    def part1(self, parsed_content) -> int:
        exp_universe = self.expand_universe1(parsed_content)
        galaxy = self.get_galaxy(exp_universe)
        res = []
        for i, pos in enumerate(galaxy):
            for pos2 in galaxy[i+1:]:
                res.append(manhatthan_dist(pos, pos2))
        return sum(res)

    def part2(self, parsed_content) -> int:
        galaxy = self.get_galaxy(parsed_content)
        exp_universe = self.expand_universe_var(parsed_content, 1_000_000)
        res = []
        for i, pos in enumerate(galaxy):
            for pos2 in galaxy[i+1:]:
                hoz_cost = [exp_universe[pos[1]][x][0] for x in range(min(pos[0], pos2[0]), max(pos[0], pos2[0]))]
                vert_cost = [exp_universe[y][pos[0]][1] for y in range(min(pos[1], pos2[1]), max(pos[1], pos2[1]))]
                res.append(sum(hoz_cost + vert_cost))
        return sum(res)


if __name__ == "__main__":
    input_content = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
    d = Day11(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
