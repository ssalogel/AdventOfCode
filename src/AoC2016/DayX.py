from AdventUtils.Day import Day


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2016, content=content)

    def parse_content(self, content: str) -> str:
        return content

    def part1(self, parsed_content) -> int:
        pass

    def part2(self, parsed_content) -> int:
        pass
