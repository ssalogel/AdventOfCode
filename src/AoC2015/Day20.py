from AdventUtils.Day import Day
from AdventUtils.Math import magic_divisors


class Day20(Day):
    def __init__(self, content=None):
        super().__init__(day=20, year=2015, content=content)

    def parse_content(self):
        return int(self.content)

    def part1(self):
        house = 1
        gifts = 10
        while gifts < self.data_p1:
            house += 1
            gifts = sum(map(lambda x: 10 * x, magic_divisors(house)))
        return house

    def part2(self):
        house = 1
        gifts = 11
        while gifts < self.data_p2:
            house += 1
            givers = list(filter(lambda x: x * 50 >= house, magic_divisors(house)))
            gifts = sum(map(lambda x: 11 * x, givers))
        return house
