from src.AdventUtils.Day import Day
from collections import defaultdict


class Day5(Day):
    def __init__(self, content=None):
        super().__init__(day=5, year=2021, content=content)

    def parse_content(self, content: str):
        return [(tuple(map(int, start.split(','))), tuple(map(int, stop.split(','))))
                for start, stop in [line.split(' -> ') for line in content.strip().split('\n')]]

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
