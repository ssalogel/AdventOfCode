from src.AdventUtils.Day import Day


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2017, content=content)

    def parse_content(self, content: str):
        return [int(elem) for elem in content]

    def part1(self, parsed_content) -> int:
        return sum(
            [
                e
                for i, e in enumerate(parsed_content)
                if parsed_content[(i + 1) % (len(parsed_content))] == e
            ]
        )

    def part2(self, parsed_content) -> int:
        size = len(parsed_content)
        return sum(
            [
                e
                for i, e in enumerate(parsed_content)
                if parsed_content[(i + (size // 2)) % size] == e
            ]
        )


if __name__ == "__main__":
    input_content = """12131415
""".strip()
    d = Day1(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
