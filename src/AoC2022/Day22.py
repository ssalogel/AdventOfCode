from src.AdventUtils.Day import Day


class Day22(Day):
    def __init__(self, content=None):
        super().__init__(day=22, year=2022, content=content)

    def parse_content(self, content: str):
        return content.rstrip().split('\n\n')

    def part1(self, parsed_content) -> int:
        return parsed_content

    def part2(self, parsed_content) -> int:
        pass


if __name__ == "__main__":
    input_content = """
"""
    d = Day22(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
