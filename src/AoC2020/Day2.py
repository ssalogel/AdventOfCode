from src.AdventUtils.Day import Day


class Day2(Day):
    def __init__(self, content=None):
        super().__init__(day=2, year=2020, content=content)

    def parse_content(self, content: str):
        lines = content.strip().split('\n')
        lines = [l.split(' ') for l in lines]
        return [(int(x[0].split('-')[0]), int(x[0].split('-')[1]), x[1][0], x[-1]) for x in lines]

    def part1(self, parsed_content) -> int:
        tot = 0
        for minimum, maximum, char, password in parsed_content:
            if minimum <= password.count(char) <= maximum:
                tot += 1
        return tot

    def part2(self, parsed_content) -> int:
        tot = 0
        for idx1, idx2, char, password in parsed_content:
            if (password[idx1-1] == char) ^ (password[idx2-1] == char):
                tot += 1
        return tot


if __name__ == "__main__":
    input_content = """
"""
    d = Day2(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
