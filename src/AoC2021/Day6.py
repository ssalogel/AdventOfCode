from AdventUtils.Day import Day
from collections import Counter


class Day6(Day):
    def __init__(self, content=None):
        super().__init__(day=6, year=2021, content=content)

    def parse_content(self, content: str):
        return [int(x) for x in content.split(',')]

    @staticmethod
    def spawn_fishes(fishes: list[int], days: int) -> list[int]:
        for _ in range(days):
            spawning = fishes[0]
            fishes = fishes[1:] + [spawning]
            fishes[6] += spawning
        return fishes

    def part1(self, parsed_content) -> int:
        amount = [0] * 9
        for time in parsed_content:
            amount[time] += 1
        return sum(self.spawn_fishes(amount, 80))

    def part2(self, parsed_content) -> int:
        amount = [0] * 9
        for time in parsed_content:
            amount[time] += 1
        return sum(self.spawn_fishes(amount, 256))


if __name__ == '__main__':
    content = """3,4,3,1,2
"""
    d = Day6(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))
