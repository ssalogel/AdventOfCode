from AdventUtils.Day import Day
from AdventUtils.Computer import Computer, Instructions


class Day23(Day):
    def __init__(self, content=None):
        super().__init__(day=23, year=2015, content=content)

    def parse_content(self) -> list[tuple[str, str]]:
        return [(d[:3], d[4:]) for d in self.content.strip().split('\n')]

    def set_up_computer(self) -> Computer:
        c = Computer()
        c.add_instruction_type('hlf', Instructions.half_register)
        c.add_instruction_type('inc', Instructions.increment_register)
        c.add_instruction_type('tpl', Instructions.triple_register)
        c.add_instruction_type('jmp', Instructions.jump)
        c.add_instruction_type('jio', Instructions.jump_if_one)
        c.add_instruction_type('jie', Instructions.jump_if_even)
        return c

    def part1(self):
        comp = self.set_up_computer()
        comp.set_program(self.data_p1)
        return comp.run()['b']

    def part2(self):
        comp = self.set_up_computer()
        comp.set_register(reg='a', value=1)
        comp.set_program(self.data_p2)
        return comp.run()['b']
