from src.AdventUtils.Equation_solver import Solver


def set_up_solver() -> Solver:
    one_op_instructions = {
        'NEG': lambda x: -x,
    }
    two_op_instructions = {
        'PLUS': lambda a, b: a + b,
        'MINUS': lambda a, b: a - b
    }
    return Solver(one_op_instr=one_op_instructions, two_op_instr=two_op_instructions)


def test_do_one_op_instr():
    assert set_up_solver().do_one_op_instr(operand=5, instr='NEG') == -5


def test_do_two_op_instr():
    s = set_up_solver()
    assert s.do_two_op_instr(op1=1, op2=2, instr='PLUS') == 3
    assert s.do_two_op_instr(op1=12, op2=5, instr='MINUS') == 7


def test_add_equation():
    s = set_up_solver()
    s.add_equation(('1',), 'x')
    s.add_equation(('NEG', 'x'), "y")
    s.add_equation(('NEG', 'y'), "k")
    s.add_equation(('y', 'PLUS', 'x'), "l")
    s.add_equation(('l', 'PLUS', 'l'), "m")
    s.add_equation(('k', 'MINUS', 'x'), "z")
    assert len(s.no_op_equations) == 1
    assert len(s.one_op_equations) == 2
    assert len(s.two_op_equations) == 3


def test_solve():
    s = set_up_solver()
    s.add_equation(('1',), 'x')
    s.add_equation(('NEG', 'x'), "y")
    s.add_equation(('NEG', 'y'), "k")
    s.add_equation(('y', 'PLUS', 'x'), "l")
    s.add_equation(('l', 'PLUS', 'l'), "m")
    s.add_equation(('k', 'MINUS', 'x'), "z")
    assert s.solve() == {'x': 1, 'y': -1, 'k': 1,
                         'l': 0, 'm': 0, 'z': 0}
