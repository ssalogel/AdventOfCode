import math
import re
from operator import mul
from functools import reduce
from src.AdventUtils.Day import Day


class Day6(Day):
    def __init__(self, content=None):
        super().__init__(day=6, year=2023, content=content)

    def parse_content(self, content: str):
        time, distance = content.strip().splitlines()
        return map(int, re.findall(r"(\d+)", time)), map(int, re.findall(r"(\d+)", distance))

    def part1(self, parsed_content) -> int:
        res = []
        for time, distance in zip(parsed_content[0], parsed_content[1]):
            victory = 0
            for t in range(time):
                if (time - t)*t > distance:
                    victory += 1
            res.append(victory)
        return reduce(mul, res)

    def magic_math(self, duration, distance):
        tmp = math.sqrt(duration**2-(4*distance))
        h1 = (-duration + tmp)/2
        h2 = (-duration - tmp)/2

        offset = (h1 == h1//1 and h2 == h2//1)*2

        return abs(math.floor(h2) - math.ceil(h1) - offset + 1)

    def part2(self, parsed_content) -> int:
        time, distance = self.content.splitlines()
        time = int(time[6:].replace(" ", ""))
        distance = int(distance[10:].replace(" ", ""))
        too_slow = """victory = 0
        for t in range(time):
            if (time - t)*t > distance:
                victory = t
                break
        for t in range(time, 0, -1):
            if (time - t) * t > distance:
                victory = t - victory + 1
                break
        return victory"""
        return self.magic_math(time, distance)


if __name__ == "__main__":
    input_content = """Time:      7  15   30
Distance:  9  40  200
"""
    d = Day6(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
