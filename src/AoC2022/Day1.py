from src.AdventUtils.Day import Day


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2022, content=content)

    def parse_content(self, content: str) -> list[list[int]]:
        return [
            [int(x) for x in elf.split("\n")] for elf in content.strip().split("\n\n")
        ]

    def part1(self, parsed_content: list[list[int]]):
        return max(map(lambda x: sum(x), parsed_content))

    def part2(self, parsed_content: list[list[int]]) -> int:
        return sum(sorted(map(lambda x: sum(x), parsed_content), reverse=True)[:3])


if __name__ == "__main__":
    input_content = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    d = Day1(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
