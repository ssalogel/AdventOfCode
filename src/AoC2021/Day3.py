from AdventUtils.Day import Day
from collections import Counter


class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2021, content=content)

    def parse_content(self, content: str) -> list[str]:
        return content.split('\n')

    def part1(self, parsed_content: list[str]) -> int:
        length = len(parsed_content[0])
        measurements = [int(x, 2) for x in parsed_content]
        mask = 2**length - 1
        gamma: int = 0
        for pos in reversed(range(length)):
            masked = [(m & (1 << pos)) >> pos for m in measurements]
            gamma += Counter(masked).most_common()[0][0] << pos
        epsilon: int = ~gamma & mask
        return gamma * epsilon

    def part2(self, parsed_content: list[str]) -> int:
        length = len(parsed_content[0])
        measurements = [int(x, 2) for x in parsed_content]
        oxygen = co2 = measurements
        for pos in reversed(range(length)):
            oxy_masked = [(m & (1 << pos)) >> pos for m in oxygen]
            oxy_counts = Counter(oxy_masked).most_common()
            if len(oxy_counts) != 1:
                oxy_most_common = oxy_counts[0][0] if oxy_counts[0][1] != oxy_counts[1][1] else 1
                oxygen = list(filter(lambda x: x & (1 << pos) == oxy_most_common << pos, oxygen))

            co2_masked = [(m & (1 << pos)) >> pos for m in co2]
            co2_counts = Counter(co2_masked).most_common()
            if len(co2_counts) != 1:
                co2_least_common = co2_counts[1][0] if co2_counts[0][1] != co2_counts[1][1] else 0
                co2 = list(filter(lambda x: x & (1 << pos) == co2_least_common << pos, co2))
        return oxygen[0] * co2[0]
