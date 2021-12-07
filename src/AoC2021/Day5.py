from AdventUtils.Day import Day
from collections import defaultdict

class Day5(Day):
    def __init__(self, content=None):
        super().__init__(day=5, year=2021, content=content)

    def parse_content(self, content: str):
        return [(tuple(map(int, start.split(','))), tuple(map(int,stop.split(',')))) for start, stop in [l.split(' -> ') for l in content.strip().split('\n')]]


    def part1(self, parsed_content) -> int:
        board = defaultdict(int)
        for start, end in parsed_content:
            start, end = sorted([start, end])
            if start[0] == end[0] or start[1] == end[1]:
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        board[(i, j)] += 1

        return len([k for k, v in board.items() if v > 1])


    def part2(self, parsed_content) -> int:
        board = defaultdict(int)
        for start, end in parsed_content:
            start, end = sorted([start, end])
            if start[0] == end[0] or start[1] == end[1]:
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        board[(i, j)] += 1
            else:
                if start[1] <= end[1]:
                    for i, j in zip(range(start[0], end[0] + 1), range(start[1], end[1] + 1)):
                        board[(i, j)] += 1
                else:
                    for i, j in zip(range(start[0], end[0] + 1), range(start[1], end[1] - 1, -1)):
                        board[(i, j)] += 1

        return len([k for k, v in board.items() if v > 1])


if __name__ == '__main__':
    content = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
    d = Day5(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))