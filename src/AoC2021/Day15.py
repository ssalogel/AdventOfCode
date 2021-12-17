from AdventUtils.Day import Day
from AdventUtils.Grid2D import get_neighbours
from collections import defaultdict
from sys import maxsize
from queue import PriorityQueue


class Day15(Day):
    def __init__(self, content=None):
        super().__init__(day=15, year=2021, content=content)

    def parse_content(self, content: str):
        return [list(map(int, x)) for x in content.strip().split('\n')]

    def path_find(self, grid: list[list[int]]) -> int:
        height, width = len(grid), len(grid[0])
        target = (height - 1, width - 1)
        nodes = defaultdict(lambda: maxsize)
        nodes[(0, 0)]: dict[tuple[int, int], int] = 0
        to_visit = PriorityQueue()
        to_visit.put((nodes[(0, 0)], (0, 0)))
        while to_visit:
            dist, current = to_visit.get()
            if current == target:
                break
            nei = get_neighbours(current[0], current[1], width, height)
            for n in nei:
                risk = grid[n[0]][n[1]]
                if nodes[n] > dist + risk:
                    nodes[n] = dist + risk
                    to_visit.put((nodes[n], n))
        return nodes[target]

    def part1(self, parsed_content) -> int:
        return self.path_find(parsed_content)

    def part2(self, parsed_content) -> int:
        height, _ = len(parsed_content), len(parsed_content[0])
        map = []
        for row in parsed_content:
            final_row = []
            for i in range(5):
                for cell in row:
                    v = cell + i
                    final_row.append(v if v <= 9 else v - 9)
            map.append(final_row)

        for i in range(0, 4):
            for row in map[i*height:i*height+height]:
                new_row = []
                for cell in row:
                    v = cell + 1
                    new_row.append(v if v <= 9 else v - 9)
                map.append(new_row)
        return self.path_find(map)
