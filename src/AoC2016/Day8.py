from src.AdventUtils.Day import Day
from collections import deque


class Day8(Day):
    def __init__(self, content=None):
        super().__init__(day=8, year=2016, content=content)

    def parse_content(self, content: str) -> list[list[str]]:
        return [instr.split(" ") for instr in content.split("\n")]

    def run_screen(self, width, height, instructions) -> list[list[int]]:
        screen = [deque([0] * width) for _ in range(height)]
        for instr in instructions:
            if instr[0] == "rect":
                x = instr[-1].find("x")
                for i in range(int(instr[-1][x + 1 :])):
                    for j in range(int(instr[-1][:x])):
                        screen[i][j] = 1
            else:
                offset = int(instr[2][2:])
                if instr[2].startswith("x"):
                    for _ in range(int(instr[-1])):
                        # flake8: noqa
                        (
                            screen[0][offset],
                            screen[1][offset],
                            screen[2][offset],
                            screen[3][offset],
                            screen[4][offset],
                            screen[5][offset],
                        ) = (
                            screen[5][offset],
                            screen[0][offset],
                            screen[1][offset],
                            screen[2][offset],
                            screen[3][offset],
                            screen[4][offset],
                        )
                else:
                    screen[offset].rotate(int(instr[-1]))
        return [list(d) for d in screen]

    def part1(self, parsed_content: list[list[str]]) -> int:
        return sum(map(sum, self.run_screen(50, 6, parsed_content)))

    def part2(self, parsed_content: list[list[str]]) -> str:
        screen = self.run_screen(50, 6, parsed_content)
        rows = "\n".join([" ".join(map(str, t)).replace("0", " ") for t in screen])
        return rows
