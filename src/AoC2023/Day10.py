from src.AdventUtils.Day import Day
from copy import deepcopy
from pprint import pprint

class Day10(Day):
    def __init__(self, content=None):
        super().__init__(day=10, year=2023, content=content)

    def parse_content(self, content: str):
        return content.strip().splitlines()

    def get_start(self, grid):
        for i, row in enumerate(grid):
            if "S" in row:
                return row.find("S"), i

    def create_graph(self, grid, start):
        graph = {}
        to_visit = [start]
        while to_visit:
            x, y = to_visit.pop()
            graph[(x, y)] = set()
            curr = grid[y][x]
            if y > 0 and curr in ['|', 'L', 'J', 'S'] and grid[y-1][x] in ['|', 'F', '7', 'S']:
                graph[(x, y)].add((x, y-1))
                if (x, y-1) not in graph:
                    to_visit.append((x, y-1))
            if y < len(grid) - 1 and curr in ['|', 'F', '7', 'S'] and grid[y+1][x] in ['|', 'L', 'J', 'S']:
                graph[(x, y)].add((x, y + 1))
                if (x, y + 1) not in graph:
                    to_visit.append((x, y + 1))
            if x > 0 and curr in ['-', 'J', '7', 'S'] and grid[y][x-1] in ['-', 'L', 'F', 'S']:
                graph[(x, y)].add((x-1, y))
                if (x-1, y) not in graph:
                    to_visit.append((x-1, y))
            if x < len(grid)-1 and curr in ['-', 'L', 'F', 'S'] and grid[y][x+1] in ['-', 'J', '7', 'S']:
                graph[(x, y)].add((x+1, y))
                if (x+1, y) not in graph:
                    to_visit.append((x+1, y))
        return graph

    def part1(self, parsed_content) -> int:
        start = self.get_start(parsed_content)
        graph = self.create_graph(parsed_content, start)
        return len(graph)//2

    def part2(self, parsed_content) -> int:
        start = self.get_start(parsed_content)
        graph = self.create_graph(parsed_content, start)
        inside = set()
        for y in range(len(parsed_content)-1, -1, -1):
            j = 0
            nb_edge = 0
            for i in range(y, len(parsed_content)):
                if (j, i) in graph and parsed_content[i][j] not in ['7', 'L']:
                    nb_edge += 1
                elif nb_edge % 2 == 1 and parsed_content[i][j] not in ['7', 'L']:
                    inside.add((j, i))
                j += 1
                if j >= len(parsed_content[0]):
                    break

        for x in range(1, len(parsed_content[0])):
            j = 0
            nb_edge = 0
            for i in range(x, len(parsed_content[0])):
                p = parsed_content[j][i]
                if (i, j) in graph and parsed_content[j][i] not in ['7', 'L']:
                    nb_edge += 1
                elif nb_edge % 2 == 1 and parsed_content[j][i] not in ['7', 'L']:
                    inside.add((i, j))
                j += 1
                if j >= len(parsed_content):
                    break
        return len(inside)


if __name__ == "__main__":
    input_content = """.....
.S-7.
.|.|.
.L-J.
.....
"""
    d = Day10(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
