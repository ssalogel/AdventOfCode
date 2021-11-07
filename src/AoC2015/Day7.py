from AdventUtils.Day import Day
from AdventUtils.Math import bitwise_and, bitwise_or, bitwise_not, bitwise_rshift, bitwise_lshift
from AdventUtils.Equation_solver import Solver
from functools import partial


class Day7(Day):
    def __init__(self, content=None):
        super().__init__(day=7, year=2015, content=content)

    def parse_content(self):
        data = self.content.strip().split('\n')
        return [(tuple(d.split(' '),), k) for d, k in [tuple(d.split(' -> ')) for d in data]]

    def set_up_solver(self) -> Solver:
        mask = 0xffff
        one_op_instructions = {
            'NOT': partial(bitwise_not, mask=mask)
        }
        two_op_instructions = {
            'AND': partial(bitwise_and, mask=mask),
            'OR': partial(bitwise_or, mask=mask),
            'LSHIFT': partial(bitwise_lshift, mask=mask),
            'RSHIFT': partial(bitwise_rshift, mask=mask)
        }
        return Solver(one_op_instr=one_op_instructions, two_op_instr=two_op_instructions)

    def part1(self):
        solver = self.set_up_solver()
        for op, target in self.data_p1:
            solver.add_equation(operands=op, res=target)
        res = solver.solve()
        return res['a']

    def part2(self):
        changed_data = []
        self.data_p1 = self.data_p2
        for op, target in self.data_p2:
            if target == 'b':
                op = (str(self.part1()),)
            changed_data.append((op, target))
        self.data_p1 = changed_data
        return self.part1()
