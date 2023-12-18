from src.AdventUtils.Day import Day
from src.AdventUtils.Math import (
    bitwise_and,
    bitwise_or,
    bitwise_not,
    bitwise_rshift,
    bitwise_lshift,
)
from src.AdventUtils.Equation_solver import Solver
from functools import partial


class Day7(Day):
    def __init__(self, content=None):
        super().__init__(day=7, year=2015, content=content)

    def parse_content(self, content):
        data = content.strip().split("\n")
        return [
            (
                tuple(
                    d.split(" "),
                ),
                k,
            )
            for d, k in [tuple(d.split(" -> ")) for d in data]
        ]

    def set_up_solver(self) -> Solver:
        mask = 0xFFFF
        one_op_instructions = {"NOT": partial(bitwise_not, mask=mask)}
        two_op_instructions = {
            "AND": partial(bitwise_and, mask=mask),
            "OR": partial(bitwise_or, mask=mask),
            "LSHIFT": partial(bitwise_lshift, mask=mask),
            "RSHIFT": partial(bitwise_rshift, mask=mask),
        }
        return Solver(
            one_op_instr=one_op_instructions, two_op_instr=two_op_instructions
        )

    def part1(self, parsed_content):
        solver = self.set_up_solver()
        for op, target in parsed_content:
            solver.add_equation(operands=op, res=target)
        res = solver.solve()
        return res["a"]

    def part2(self, parsed_content):
        changed_data = []
        parsed_content = parsed_content
        for op, target in parsed_content:
            if target == "b":
                op = (str(self.part1(parsed_content)),)
            changed_data.append((op, target))
        parsed_content = changed_data
        return self.part1(parsed_content)
