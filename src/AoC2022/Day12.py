from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import get_neighbours
from collections import defaultdict
from queue import PriorityQueue


class Day12(Day):
    def __init__(self, content=None):
        super().__init__(day=12, year=2022, content=content)

    def parse_content(self, content: str):
        return [
            [ord(x) - 96 if x.islower() else x for x in line]
            for line in content.strip().splitlines()
        ]

    @staticmethod
    def djikstra(
        board: list[list[int]], start: tuple[int, int]
    ) -> dict[tuple[int, int] : float]:
        width = len(board[0])
        height = len(board)
        visited = set()
        distance = defaultdict(lambda: float("inf"))
        distance[start] = 0
        q = PriorityQueue()
        q.put((distance[start], start))
        while not q.empty():
            dist, current = q.get()
            if current in visited:
                continue
            visited.add(current)
            curr_height = board[current[0]][current[1]]
            for nei in get_neighbours(current[0], current[1], height, width):
                if nei in visited:
                    continue
                nei_height = board[nei[0]][nei[1]]
                if curr_height - nei_height <= 1:
                    q.put((dist + 1, nei))
                    distance[nei] = min(distance[nei], dist + 1)
        return distance

    @staticmethod
    def set_up_board(
        content,
    ) -> tuple[tuple[int, int], tuple[int, int], list[list[int]]]:
        start = (0, 0)
        end = (0, 0)

        for ix, row in enumerate(content):
            if "S" not in row and "E" not in row:
                continue
            for jx, point in enumerate(row):
                if point == "S":
                    start = (ix, jx)
                if point == "E":
                    end = (ix, jx)
        content[start[0]][start[1]] = 1
        content[end[0]][end[1]] = 26
        return start, end, content

    def part1(self, parsed_content) -> float:
        start, goal, board = self.set_up_board(parsed_content)
        return self.djikstra(board, goal)[start]

    def part2(self, parsed_content) -> float:
        _, goal, board = self.set_up_board(parsed_content)
        return min(
            [
                x
                for point, x in self.djikstra(board, goal).items()
                if board[point[0]][point[1]] == 1
            ]
        )


if __name__ == "__main__":
    input_content = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
    d = Day12(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
