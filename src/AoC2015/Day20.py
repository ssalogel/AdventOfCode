from src.AdventUtils.Day import Day
from src.AdventUtils.Math import magic_divisors


class Day20(Day):
    def __init__(self, content=None):
        super().__init__(day=20, year=2015, content=content)

    def parse_content(self, content: str) -> int:
        return int(content)

    def part1(self, parsed_content: int) -> int:
        house = 1
        gifts = 10
        while gifts < parsed_content:
            house += 1
            gifts = sum(map(lambda x: 10 * x, magic_divisors(house)))
        return house

    def part2(self, parsed_content: int) -> int:
        house = 1
        gifts = 11
        while gifts < parsed_content:
            house += 1
            givers = list(filter(lambda x: x * 50 >= house, magic_divisors(house)))
            gifts = sum(map(lambda x: 11 * x, givers))
        return house
