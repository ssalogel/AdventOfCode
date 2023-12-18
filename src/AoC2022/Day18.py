from src.AdventUtils.Day import Day
from src.AdventUtils.Grid3D import Position3D
from collections import deque


class Day18(Day):
    def __init__(self, content=None):
        super().__init__(day=18, year=2022, content=content)

    def parse_content(self, content: str):
        return [
            Position3D(*map(int, line.split(",")))
            for line in content.strip().splitlines()
        ]

    def part1(self, parsed_content: list[Position3D]) -> int:
        points = set(parsed_content)
        exposed_sides = 0
        for point in points:
            for nei in point.get_connections():
                if nei not in points:
                    exposed_sides += 1
        return exposed_sides

    def part2(self, parsed_content: list[Position3D]) -> int:
        points = set(parsed_content)
        max_x = max([p.x for p in points]) + 1
        max_y = max([p.y for p in points]) + 1
        max_z = max([p.z for p in points]) + 1
        min_x = min([p.x for p in points]) - 1
        min_y = min([p.y for p in points]) - 1
        min_z = min([p.z for p in points]) - 1
        exposed_sides = 0
        exposed_air = set()
        exposed_sides_2 = 0

        starting_air = Position3D(max_x, max_y, max_z)
        assert starting_air not in points

        queue: deque[Position3D] = deque()
        queue.append(starting_air)
        while len(queue):
            curr = queue.pop()
            for p in curr.get_connections():
                if p in exposed_air:
                    continue
                if p in points:
                    exposed_sides += 1
                    continue
                if (
                    min_x <= p.x <= max_x
                    and min_y <= p.y <= max_y
                    and min_z <= p.z <= max_z
                ):
                    queue.append(p)
                    exposed_air.add(p)
        return exposed_sides


if __name__ == "__main__":
    input_content = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""
    d = Day18(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
