from AdventUtils.Day import Day
from AdventUtils.Crypto import find_hash

class Day5(Day):
    def __init__(self, content="ffykfhsq"):
        super().__init__(day=5, year=2016, content=content)

    def parse_content(self) -> str:
        return self.content

    def part1(self) -> int:
        hashes = find_hash(self.data_p1, '00000', 8)
        return ''.join([c[5] for _, c in hashes])


    def part2(self) -> int:
        hashes = find_hash(self.data_p2, '00000', 36)
        keys = {}
        for _, h in hashes:
            key = int(h[5], 16)
            if key < 8 and key not in keys:
                keys[key] = h[6]
        return ''.join( c for _, c in sorted(keys.items()))
