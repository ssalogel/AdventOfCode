from src.AdventUtils.Day import Day
from itertools import product


class Day24(Day):
    def __init__(self, content=None):
        super().__init__(day=24, year=2021, content=content)

    def parse_content(self, content: str) -> list[tuple[int, int]]:
        lines = content.strip().split('\n')
        return [(int(lines[i*18:(i+1)*18][5][6:]), int(lines[i*18:(i+1)*18][-3][6:])) for i in range(14)]

    @staticmethod
    def get_constraints(pairs: list[tuple[int, int]]) -> dict[int, tuple[int, int]]:
        stack = []
        constraints = {}
        for step, (mod_offset, add) in enumerate(pairs):
            # Model: since each step either *26 or /26, we model each result of a step as a new digit of a base 26 number
            # this way, we push on the stack each new number, and when we reduce we pop the latest number

            if mod_offset > 0:
                stack.append((step, add))
                # would z = z * 26 + add, where 0 <= add < 26
            else:
                # get previous relevant step (to get the modulo answer)
                p_step, mod_ans = stack.pop()
                constraints[step] = (p_step, mod_ans + mod_offset)
        return constraints

    def part1(self, parsed_content: list[tuple[int, int]]) -> int:
        constraints = self.get_constraints(parsed_content)
        digits = {}
        for source, (divi, offset) in constraints.items():
            # simple example, pairs[(11, 1), (0, -2)] -> constraint {d1: (d0, 1 - 0)}
            # so ((d0 + 1) % 26) + 0 == d2
            #    by problem, d0 + 1 <= 26
            #      d0 + 1 = d2
            #      d0 = d2 - 1
            # so d0 = min(9, 9 - 1)
            #    d1 = min(9, 9 + 1)
            # so that d0 + 1 == d2 and d0 < 10 and d1 < 10
            digits[source] = min(9, 9 + offset)  # digit at decrease
            digits[divi] = min(9, 9 - offset)  # digit at increase
        return int(''.join(str(digits[x]) for x in range(len(parsed_content))))

    def part2(self, parsed_content: list[tuple[int, int]]) -> int:
        constraints = self.get_constraints(parsed_content)
        digits = {}
        for source, (divi, offset) in constraints.items():
            digits[source] = max(1, 1 + offset)  # digit at decrease
            digits[divi] = max(1, 1 - offset)    # digit at increase
        return int(''.join(str(digits[x]) for x in range(len(parsed_content))))


if __name__ == '__main__':
    input_content = None
    d = Day24(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
