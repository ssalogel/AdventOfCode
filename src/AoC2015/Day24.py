from AdventUtils.Day import Day
from AdventUtils.Math import get_subsets_min_len_sum_target
from functools import reduce
from operator import mul


class Day24(Day):
    def __init__(self, content=None):
        super().__init__(day=24, year=2015, content=content)

    def parse_content(self):
        return [int(d) for d in self.content.strip().split('\n')]

    def part1(self):
        target = sum(self.data_p1)//3
        potential = get_subsets_min_len_sum_target(target=target, nums=self.data_p1)
        qes = [reduce(mul, p) for p in potential]
        return min(qes)

    def part2(self):
        target = sum(self.data_p2) // 4
        potential = get_subsets_min_len_sum_target(target=target, nums=self.data_p2)
        qes = [reduce(mul, p) for p in potential]
        return min(qes)
