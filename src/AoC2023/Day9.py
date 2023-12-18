from src.AdventUtils.Day import Day


class Day9(Day):
    def __init__(self, content=None):
        super().__init__(day=9, year=2023, content=content)

    def parse_content(self, content: str):
        return [list(map(int, x.split(' '))) for x in content.splitlines()]

    def part1(self, parsed_content) -> int:
        res = []
        for row in parsed_content:
            eq = [row]
            while any(eq[-1]):
                eq.append([x - eq[-1][i] for i, x in enumerate(eq[-1][1:])])
            change = 0
            for i, row in enumerate(reversed(eq[:-1])):
                change += row[-1]
            res.append(change)
        return sum(res)

    def part2(self, parsed_content) -> int:
        res = []
        for row in parsed_content:
            eq = [row]
            while any(eq[-1]):
                eq.append([x - eq[-1][i] for i, x in enumerate(eq[-1][1:])])
            change = 0
            for i, row in enumerate(reversed(eq[:-1])):
                change = row[0] - change
            res.append(change)
        return sum(res)


if __name__ == "__main__":
    input_content = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
    d = Day9(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
