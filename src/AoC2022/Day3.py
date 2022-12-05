from src.AdventUtils.Day import Day


class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2022, content=content)

    def parse_content(self, content: str):
        return [[ord(letter) - 38 if letter.isupper() else ord(letter) - 96 for letter in line] for line in content.strip().splitlines()]

    def part1(self, parsed_content) -> int:
        return sum(sum({e for e in line[:len(line)//2]} & {e for e in line[len(line)//2:]}) for line in parsed_content)

    def part2(self, parsed_content) -> int:
        return sum([set.intersection(*map(set, g)).pop() for g in zip(parsed_content[::3], parsed_content[1::3], parsed_content[2::3])])


if __name__ == '__main__':
    input_content = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
    d = Day3(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
