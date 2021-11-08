from AdventUtils.Day import Day
from AdventUtils.Grid2D import Position2D


class Day2(Day):
    def __init__(self, content=None):
        super().__init__(day=2, year=2016, content=content)

    def parse_content(self) -> list[str]:
        return self.content.strip().split('\n')

    def part1(self) -> str:
        res = []
        num = 5
        for num_instr in self.data_p1:
            for instr in num_instr:
                if instr == 'U':
                    if num > 3:
                        num -= 3
                elif instr == 'L':
                    if (1 < num < 4) or (4 < num < 7) or 7 < num:
                        num -= 1
                elif instr == 'D':
                    if num < 7:
                        num += 3
                elif instr == 'R':
                    if num < 3 or (3 < num < 6) or (6 < num < 9):
                        num += 1
            res.append(num)
        return ''.join([str(r) for r in res])

    def part2(self) -> str:
        keypad = {
            Position2D(2, 4): '1',
            Position2D(1, 3): '2',
            Position2D(2, 3): '3',
            Position2D(3, 3): '4',
            Position2D(0, 2): '5',
            Position2D(1, 2): '6',
            Position2D(2, 2): '7',
            Position2D(3, 2): '8',
            Position2D(4, 2): '9',
            Position2D(1, 1): 'A',
            Position2D(2, 1): 'B',
            Position2D(3, 1): 'C',
            Position2D(2, 0): 'D',
        }
        pos = Position2D(0, 2)
        res = []
        for num_instr in self.data_p1:
            for instr in num_instr:
                if instr == 'U':
                    new = pos.move_up()
                elif instr == 'D':
                    new = pos.move_down()
                elif instr == 'L':
                    new = pos.move_left()
                elif instr == 'R':
                    new = pos.move_right()
                pos = new if new in keypad else pos
            res.append(pos)
        return ''.join([keypad[k] for k in res])
