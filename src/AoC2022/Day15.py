from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import Position2D, manhatthan_dist

import re
from dataclasses import dataclass
from typing import Optional
from itertools import combinations


@dataclass
class Pair:
    sensor: Position2D
    beacon: Position2D
    min_dist: int = -1

@dataclass
class Square:
    center: Position2D
    up: int
    right: int
    down: int
    left: int
    dist: int

    def __contains__(self, other: Position2D):
        if manhatthan_dist(other, self.center) <= self.dist:
            return True
        return False


def perimeter_generator(sensor: Position2D, distance: int) -> tuple[int, int]:
    for d in range(distance):
        yield (Position2D.x + d, Position2D.y + distance - d)
        yield (Position2D.x - d, Position2D.y - distance + d)
        yield (Position2D.x + distance - d, Position2D.y - d)
        yield (Position2D.x - distance + d, Position2D.y + d)

def upper_left_generator(sensor: Position2D, distance: int) -> Position2D:
    for d in range(distance):
        yield Position2D(Position2D.x - distance + d, Position2D.y + d)

def join_to_lenght(left: tuple[int, int], right: tuple[int, int]):
    # assumes that left[0] <= right[0]
    if left[1] < right[0]:
        return [left, right]
    return [(min(left[0], right[0]), max(left[1], right[1]))]

def get_blocked_range(p: Pair, target_y: int) -> Optional[tuple[int, int]]:
    up_range = p.sensor.y + p.min_dist
    down_range = p.sensor.y - p.min_dist
    if up_range >= target_y and down_range <= target_y:
        dist_to_y = p.min_dist - abs(p.sensor.y - target_y)
        return (p.sensor.x - dist_to_y, p.sensor.x + dist_to_y)
    return None

class Day15(Day):
    def __init__(self, content=None):
        super().__init__(day=15, year=2022, content=content)

    def parse_content(self, content: str):
        res = []
        for line in content.strip().splitlines():
            s1, s2, b1, b2 = map(int, re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups())
            res.append(Pair(Position2D(s1,s2), Position2D(b1, b2)))
        return res

    def part1(self, parsed_content: list[Pair]):
        if __name__ != '__main__':
            y_to_analyze = 2000000 
        else:
            y_to_analyze = 20
        for p in parsed_content:
            p.min_dist = manhatthan_dist(p.beacon, p.sensor)
        points = sorted(parsed_content, key=lambda x: x.min_dist)
        obscured = []
        for p in points:
            range = get_blocked_range(p, y_to_analyze)
            if range is not None:
                obscured.append(range)
        occluded = list(sorted(obscured, key=lambda x: x[0]))
        res = [occluded[0]]
        for lenght in occluded[1:]:
            res.extend(join_to_lenght(res.pop(), lenght))
        return sum(x[1] - x[0] for x in res)

    def part2(self, parsed_content: list[Pair]) -> int:
        # find all "squares" that have a separation of exactly 1
        # find combination of 2 pairs where the separation overlap

        # or

        # find group of 4 squares with 2 pairs of separation 1 
        # where the other parings have separation of 0 or less
        squares = []
        for p in parsed_content:
            dist = manhatthan_dist(p.beacon, p.sensor)
            squares.append(Square(center=p.sensor, up=p.sensor.y+dist, right=p.sensor.x+dist, down=p.sensor.y-dist, left=p.sensor.x-dist, dist=dist))
        up_left_one_sep = []
        up_right_one_sep = []
        acc = 0
        for s1, s2 in combinations(squares, 2):
            if s1.up < s2.down or s2.up < s1.down:
                continue
            if s1.right < s2.left or s2.right < s1.left:
                continue
            down_right_diff = (s2.center.x - s2.up) - (s1.center.x - s1.down)
            if down_right_diff == 2:
                up_left_one_sep.append((s1, s2))
            down_right_diff = (s1.center.x - s1.up) - (s2.center.x - s2.down)
            if down_right_diff == 2:
                up_left_one_sep.append((s2, s1))
            down_left_diff = (s1.center.x + s1.down) - (s2.center.x + s2.up)
            if down_left_diff == 2:
                up_right_one_sep.append((s1, s2))
            down_left_diff = (s2.center.x + s2.down) - (s1.center.x + s1.up)
            if down_left_diff == 2:
                up_right_one_sep.append((s2, s1))
        for a, b in up_left_one_sep:
            for c, d in up_right_one_sep:
                if len(set([a.center, b.center, c.center, d.center])) != 4:
                    continue
                # a/b and d\c
                for p in perimeter_generator(b.center, b.dist):
                    p = p.move_left()
                    if p.x < 0 or p.y < 0:
                        continue
                    if p in a or p in c or p in d:
                        continue
                    print(p)
        return len(up_left_one_sep), len(up_right_one_sep)


if __name__ == '__main__':
    input_content = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
    """
    d = Day15(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
