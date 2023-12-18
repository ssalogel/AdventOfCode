from src.AdventUtils.Day import Day


class Day6(Day):
    def __init__(self, content=None):
        super().__init__(day=6, year=2022, content=content)

    def parse_content(self, content: str):
        return content.strip()

    def part1(self, parsed_content) -> int:
        for i, marker in enumerate(
            zip(
                parsed_content,
                parsed_content[1:],
                parsed_content[2:],
                parsed_content[3:],
            )
        ):
            if len(set(marker)) == 4:
                return i + 4

    def part2(self, parsed_content) -> int:
        length = 14
        for i in range(len(parsed_content) - length):
            if len(set(parsed_content[i : i + 14])) == length:
                return i + 14


if __name__ == "__main__":
    input_content = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""
    d = Day6(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
