from src.AdventUtils.Day import Day
import re

class Day5(Day):
    def __init__(self, content=None):
        super().__init__(day=5, year=2022, content=content)

    def parse_content(self, content: str) -> tuple[list[str], list[tuple[int, int, int]]]:
        crates_dat, insrt_dat = content.split("\n\n")[0].splitlines(), content.split('\n\n')[1].splitlines()
        crates = [row[1::4] for row in crates_dat][:-1]
        instr = [tuple(map(int, re.match(R"move (\d+) from (\d+) to (\d+)", line).groups())) for line in insrt_dat]
        return crates, instr

    def make_stack(self, crates: list[str]) -> list[list[str]]:
        stack = [[] for _ in range(len(crates[0]))]
        for row in reversed(crates):
            for i, l in enumerate(row):
                if l != " ":
                    stack[i].append(l)
        return stack

    def part1(self, parsed_content) -> str:
        stack = self.make_stack(parsed_content[0])
        for amount, i, j in parsed_content[1]:
            i -= 1
            j -= 1
            for _ in range(amount):
                stack[j].append(stack[i].pop())
        return ''.join([s[-1] for s in stack])

    def part2(self, parsed_content) -> str:
        stack = self.make_stack(parsed_content[0])
        for amount, i, j in parsed_content[1]:
            i -= 1
            j -= 1
            stack[j] += stack[i][-amount:]
            stack[i] = stack[i][:-amount]
        return ''.join([s[-1] for s in stack])


if __name__ == '__main__':
    input_content = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
    d = Day5(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
