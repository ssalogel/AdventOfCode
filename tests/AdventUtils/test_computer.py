from AdventUtils.Computer import Computer, Instructions
import pytest


class TestComputer:
    @staticmethod
    def get_Computer() -> Computer:
        c = Computer()
        c.add_instruction_type('hlf', Instructions.half_register)
        c.add_instruction_type('inc', Instructions.increment_register)
        c.add_instruction_type('tpl', Instructions.triple_register)
        c.add_instruction_type('jio', Instructions.jump_if_one)
        return c

    def test_add_instructions(self):
        c = Computer()
        c.add_instruction_type('hlf', Instructions.half_register)
        c.add_instruction_type('inc', Instructions.increment_register)
        c.add_instruction_type('tpl', Instructions.triple_register)
        assert len(c.instruction_set) == 3

    @pytest.mark.parametrize("instrs, reg, value", [
        ([('inc', 'a'), ('inc', 'a'), ('tpl', 'a'), ('hlf', 'a')], 'a', 3),
        ([("inc", 'a'), ('jio', 'a, +2'), ('tpl', 'a'), ('inc', 'a')], 'a', 2)
    ])
    def test_run(self, instrs, reg, value):
        comp = self.get_Computer()
        comp.set_program(instrs)
        assert comp.run()[reg] == value

    def test_set_register(self):
        c = self.get_Computer()
        c.set_register('a', 1)
        assert c.registers['b'] == 0
        assert c.registers['a'] == 1


class TestInstructions:
    @pytest.mark.parametrize('arg, reg, cntr, ex_reg, ex_cntr', [
        ('a', {'a': 4}, 0, {'a': 2}, 1)
    ])
    def test_half_register(self, arg: str, reg: dict[str, int], cntr: int, ex_reg: dict[str, int], ex_cntr: int):
        assert Instructions.half_register(args=arg, cntr=cntr, registers=reg) == (ex_cntr, ex_reg)

    @pytest.mark.parametrize('arg, reg, cntr, ex_reg, ex_cntr', [
        ('a', {'a': 1}, 0, {'a': 3}, 1)
    ])
    def test_triple_register(self, arg: str, reg: dict[str, int], cntr: int, ex_reg: dict[str, int], ex_cntr: int):
        assert Instructions.triple_register(args=arg, cntr=cntr, registers=reg) == (ex_cntr, ex_reg)

    @pytest.mark.parametrize('arg, reg, cntr, ex_reg, ex_cntr', [
        ('a', {'a': 0}, 0, {'a': 1}, 1)
    ])
    def test_increment_register(self, arg: str, reg: dict[str, int], cntr: int, ex_reg: dict[str, int], ex_cntr: int):
        assert Instructions.increment_register(args=arg, cntr=cntr, registers=reg) == (ex_cntr, ex_reg)

    @pytest.mark.parametrize('arg, reg, cntr, ex_reg, ex_cntr', [
        ('5', {'a': 0}, 0, {'a': 0}, 5),
        ('5', {'a': 0}, 3, {'a': 0}, 8),
        ('-5', {'a': 0}, 13, {'a': 0}, 8)
    ])
    def test_jump(self, arg: str, reg: dict[str, int], cntr: int, ex_reg: dict[str, int], ex_cntr: int):
        assert Instructions.jump(args=arg, cntr=cntr, registers=reg) == (ex_cntr, ex_reg)

    @pytest.mark.parametrize('arg, reg, cntr, ex_reg, ex_cntr', [
        ('a, +3', {'a': 0}, 0, {'a': 0}, 1),
        ('a, +3', {'a': 1}, 0, {'a': 1}, 3)
    ])
    def test_jump_if_one(self, arg: str, reg: dict[str, int], cntr: int, ex_reg: dict[str, int], ex_cntr: int):
        assert Instructions.jump_if_one(args=arg, cntr=cntr, registers=reg) == (ex_cntr, ex_reg)

    @pytest.mark.parametrize('arg, reg, cntr, ex_reg, ex_cntr', [
        ('a, +4', {'a': 0}, 0, {'a': 0}, 4),
        ('a, +4', {'a': 1}, 0, {'a': 1}, 1)
    ])
    def test_jump_if_even(self, arg: str, reg: dict[str, int], cntr: int, ex_reg: dict[str, int], ex_cntr: int):
        assert Instructions.jump_if_even(args=arg, cntr=cntr, registers=reg) == (ex_cntr, ex_reg)
