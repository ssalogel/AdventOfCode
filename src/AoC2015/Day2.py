from src.AdventUtils.Day import Day
from src.AdventUtils.holders import Box


class Day2(Day):
    def __init__(self, content=None):
        super().__init__(day=2, year=2015, content=content)

    def parse_content(self, content: str) -> list[Box]:
        return [Box(int(a), int(b), int(c)) for a, b, c in [line.split('x') for line in content.split('\n')]]

    def part1(self, parsed_content: list[Box]) -> int:
        total = 0
        for box in parsed_content:
            total += box.get_total_surface()
            total += box.get_smallest_side_size()

        return total

    def part2(self, parsed_content: list[Box]) -> int:
        total = 0
        for box in parsed_content:
            total += box.get_smallest_perimeter()
            total += box.get_volume()
        return total
