from AdventUtils.Day import Day
from collections import Counter


class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2021, content=content)

    def parse_content(self) -> str:
        return self.content.split('\n')

    def part1(self) -> int:
        length = len(self.data_p1[0])
        measurements = list(map(lambda x: int(x, 2), self.data_p1))
        mask = 2**length -1
        most_common_digits = []
        for pos in reversed(range(length)):
            masked = [(m & (1 << pos)) >> pos for m in measurements]
            most_common_digits.append(Counter(masked).most_common()[0][0])
        gamma = int(''.join(str(d) for d in most_common_digits), 2)
        epsilon = ~gamma & mask
        return gamma * epsilon

    def part2(self) -> int:
        length = len(self.data_p2[0])
        measurements = list(map(lambda x: int(x, 2), self.data_p2))
        oxygen = co2 = measurements
        for pos in reversed(range(length)):
            oxy_masked = [(m & (1 << pos)) >> pos for m in oxygen]
            co2_masked = [(m & (1 << pos)) >> pos for m in co2]
            oxy_counts = Counter(oxy_masked).most_common()
            co2_counts = Counter(co2_masked).most_common()
            if len(oxy_counts) != 1:
                oxy_most_common = oxy_counts[0][0] if oxy_counts[0][1] != oxy_counts[1][1] else 1
                oxygen = list(filter(lambda x: x & (1 << pos) == oxy_most_common << pos, oxygen))

            if len(co2_counts) != 1:
                co2_least_common =  co2_counts[1][0] if co2_counts[0][1] != co2_counts[1][1] else 0
                co2 = list(filter(lambda x: x & (1 << pos) == co2_least_common << pos, co2))

        return oxygen[0] * co2[0]
