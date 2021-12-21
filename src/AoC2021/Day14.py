from src.AdventUtils.Day import Day
from collections import Counter
from itertools import pairwise


class Day14(Day):
    def __init__(self, content=None):
        super().__init__(day=14, year=2021, content=content)

    def parse_content(self, content: str):
        start, rules = content.strip().split('\n\n')
        return start, [r.split(' -> ') for r in rules.split('\n')]

    def step(self, start, rules, number) -> list[tuple[str, int]]:
        occurences = Counter(start)
        pairs = Counter(pairwise(start))
        for _ in range(number):
            new_pairs = Counter()
            for ab, count in pairs.items():
                a, b = ab
                occurences[rules[ab]] += count
                new_pairs[(a, rules[ab])] += count
                new_pairs[(rules[ab], b)] += count
            pairs = new_pairs
        return occurences.most_common()

    def part1(self, parsed_content) -> int:
        start = parsed_content[0]
        rules = {(r[0][0], r[0][1]): r[1] for r in parsed_content[1]}
        most_commons = self.step(start, rules, 10)
        return most_commons[0][1] - most_commons[-1][1]

    def part2(self, parsed_content) -> int:
        start = parsed_content[0]
        rules = {(r[0][0], r[0][1]): r[1] for r in parsed_content[1]}
        most_commons = self.step(start, rules, 40)
        return most_commons[0][1] - most_commons[-1][1]
