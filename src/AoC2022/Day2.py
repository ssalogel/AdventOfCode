from src.AdventUtils.Day import Day


class Day2(Day):
    def __init__(self, content=None):
        super().__init__(day=2, year=2022, content=content)

    def parse_content(self, content: str) -> list[tuple[str, str]]:
        return [(x[0], x[-1]) for x in content.strip().splitlines()]


    #  there exists a no precomputation solution, using % (-1%3=2)
    def part1(self, parsed_content) -> int:
        scores = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3,
                  ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
                  ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}
        match = [scores[x] for x in parsed_content]
        return sum(match)

    def part2(self, parsed_content) -> int:
        scores = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
                  ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
                  ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7}
        match = [scores[x] for x in parsed_content]
        return sum(match)


if __name__ == '__main__':
    input_content = """A Y
B X
C Z
"""
    d = Day2(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
