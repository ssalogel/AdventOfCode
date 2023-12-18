from src.AdventUtils.Day import Day
from src.AdventUtils.Math import get_subsets_min_len_sum_target
from functools import reduce
from operator import mul


class Day24(Day):
    def __init__(self, content=None):
        super().__init__(day=24, year=2015, content=content)

    def parse_content(self, content: str) -> list[int]:
        return [int(d) for d in content.strip().split("\n")]

    def part1(self, parsed_content: list[int]):
        target = sum(parsed_content) // 3
        potential = get_subsets_min_len_sum_target(target=target, nums=parsed_content)
        qes = [reduce(mul, p) for p in potential]
        return min(qes)

    def part2(self, parsed_content: list[int]):
        target = sum(parsed_content) // 4
        potential = get_subsets_min_len_sum_target(target=target, nums=parsed_content)
        qes = [reduce(mul, p) for p in potential]
        return min(qes)
