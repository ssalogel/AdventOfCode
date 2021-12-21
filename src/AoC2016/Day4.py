from src.AdventUtils.Day import Day
from src.AdventUtils.Crypto import rot13
from functools import reduce
from collections import defaultdict


class Day4(Day):
    def __init__(self, content=None):
        super().__init__(day=4, year=2016, content=content)

    def parse_content(self, content: str) -> list[tuple[str, int, str]]:
        res = []
        for row in content.split('\n'):
            end_name = row.rindex('-')
            name = row[:end_name].replace('-', '')
            sector = int(row[end_name + 1:row.rindex('[')])
            checksum = row[-6:-1]
            res.append((name, sector, checksum))
        return res

    def incr_item(self, dico, item):
        dico[item] += 1
        return dico

    def is_valid(self, name: str, checksum: str) -> bool:
        chrs: dict[str, int] = reduce(self.incr_item, name, defaultdict(int))
        count_chrs: list[tuple[int, str]] = sorted([(v, k) for k, v in chrs.items()], key=lambda n: (-n[0], n[1]))
        return ''.join([b for _, b in count_chrs[:5]]) == checksum

    def part1(self, parsed_content: list[tuple[str, int, str]]) -> int:
        tot = 0
        for name, room, checksum in parsed_content:
            if self.is_valid(name, checksum):
                tot += room
        return tot

    def part2(self, parsed_content: list[tuple[str, int, str]]) -> int:
        for name, room, checksum in parsed_content:
            if self.is_valid(name, checksum):
                decrypted = rot13(name, room)
                if decrypted.startswith('north'):
                    return room
        raise Exception
