from functools import partial


class Solver:
    def __init__(self, one_op_instr, two_op_instr):
        self.one_op_instr = one_op_instr
        self.two_op_instr = two_op_instr
        self.solved_vars: dict[str, int] = {}
        self.no_op_equations: set[tuple[tuple[str], str]] = set()
        self.one_op_equations: set[tuple[tuple[str, str], str]] = set()
        self.two_op_equations: set[tuple[tuple[str, str, str], str]] = set()

    def do_one_op_instr(self, operand: int, instr: str):
        return self.one_op_instr[instr](operand)

    def do_two_op_instr(self, op1: int, op2: int, instr: str):
        return self.two_op_instr[instr](op1, op2)

    def add_equation(self, operands, res: str):
        if len(operands) == 1:
            self.no_op_equations.add((operands, res))
        elif len(operands) == 2:
            self.one_op_equations.add((operands, res))
        elif len(operands) == 3:
            self.two_op_equations.add((operands, res))
        else:
            raise NotImplementedError

    def try_no_op_eq(self, op: str, res: str) -> bool:
        if op.isdigit():
            self.solved_vars[res] = int(op)
            return True
        if op in self.solved_vars:
            self.solved_vars[res] = self.solved_vars[op]
            return True
        return False

    def try_one_op_eq(self, op: str, instr: str, res: str) -> bool:
        if op.isdigit():
            self.solved_vars[res] = self.do_one_op_instr(operand=int(op), instr=instr)
            return True
        if op in self.solved_vars:
            self.solved_vars[res] = self.do_one_op_instr(operand=self.solved_vars[op], instr=instr)
            return True
        return False

    def try_two_op_eq(self, op1: str, instr: str, op2: str, res: str) -> bool:
        if op1.isdigit():
            if op2.isdigit():
                self.solved_vars[res] = self.do_two_op_instr(op1=int(op1), op2=int(op2), instr=instr)
                return True
            if op2 in self.solved_vars:
                self.solved_vars[res] = self.do_two_op_instr(op1=int(op1), op2=self.solved_vars[op2], instr=instr)
                return True
        if op1 in self.solved_vars:
            if op2.isdigit():
                self.solved_vars[res] = self.do_two_op_instr(op1=self.solved_vars[op1], op2=int(op2), instr=instr)
                return True
            if op2 in self.solved_vars:
                self.solved_vars[res] = self.do_two_op_instr(op1=self.solved_vars[op1], op2=self.solved_vars[op2], instr=instr)
                return True
        return False

    def solve(self) -> dict[str, int]:
        while self.one_op_equations or self.no_op_equations or self.two_op_equations:
            for op, res in self.no_op_equations.copy():
                if self.try_no_op_eq(op[0], res):
                    self.no_op_equations.remove((op, res))
            for oper, res in self.one_op_equations.copy():
                if self.try_one_op_eq(op=oper[1], instr=oper[0], res=res):
                    self.one_op_equations.remove((oper, res))
            for operands, res in self.two_op_equations.copy():
                if self.try_two_op_eq(op1=operands[0], op2=operands[2], instr=operands[1], res=res):
                    self.two_op_equations.remove((operands, res))
        return self.solved_vars
