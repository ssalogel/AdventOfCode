from src.AdventUtils.Day import Day
from itertools import combinations


class Day17(Day):
    def __init__(self, content=None, target=150):
        super().__init__(day=17, year=2015, content=content)
        self.target = target

    def parse_content(self, content: str) -> list[int]:
        data = content.strip().split("\n")
        return [int(d) for d in data]

    def part1(self, parsed_content: list[int]) -> int:
        containers = parsed_content
        containers.sort()
        tot = 0
        count = 0
        for bucket in containers:
            tot += bucket
            count += 1
            if tot > self.target:
                break
        max_amount = count
        tot = 0
        count = 0
        containers.reverse()
        for bucket in containers:
            tot += bucket
            count += 1
            if tot >= self.target:
                break
        min_amount = count
        combo = []
        for i in range(min_amount, max_amount):
            potentials = list(combinations(containers, i))
            combo.extend([x for x in potentials if sum(x) == self.target])
        return len(combo)

    def part2(self, parsed_content: list[int]) -> int:
        containers = parsed_content
        containers.sort()
        tot = 0
        count = 0
        containers.reverse()
        for bucket in containers:
            tot += bucket
            count += 1
            if tot >= self.target:
                break
        min_amount = count
        combo = []
        potentials = list(combinations(containers, min_amount))
        combo.extend([x for x in potentials if sum(x) == self.target])
        return len(combo)
