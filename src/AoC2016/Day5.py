from src.AdventUtils.Day import Day
from src.AdventUtils.Crypto import find_hash


class Day5(Day):
    def __init__(self, content="abbhdwsy"):
        super().__init__(day=5, year=2016, content=content)

    def parse_content(self, content: str) -> str:
        return content

    def part1(self, parsed_content: str) -> str:
        hashes = find_hash(parsed_content, '00000', 8)
        return ''.join([c[5] for _, c in hashes])

    def part2(self, parsed_content: str) -> str:
        hashes = find_hash(parsed_content, '00000', 36)
        keys = {}
        for _, h in hashes:
            key = int(h[5], 16)
            if key < 8 and key not in keys:
                keys[key] = h[6]
        return ''.join(c for _, c in sorted(keys.items()))
