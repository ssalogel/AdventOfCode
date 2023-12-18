from src.AdventUtils.Day import Day


class Day0(Day):
    def __init__(self, content=None):
        super().__init__(day=0, year=2023, content=content)

    def parse_content(self, content: str):
        return content

    def part1(self, parsed_content) -> int:
        return parsed_content

    def part2(self, parsed_content) -> int:
        pass


if __name__ == "__main__":
    input_content = """
"""
    d = Day0(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
