from collections import defaultdict
from typing import Callable


class Computer:
    def __init__(self):
        self.registers: dict[str, int] = defaultdict(int)
        self.instruction_set = {}
        self.instructions: list[tuple[str, str]] = []
        self.counter = 0

    def add_instruction_type(self, name: str, instr: Callable[[str, int, dict[str, int]], tuple[int, dict[str, int]]]):
        self.instruction_set[name] = instr

    def set_program(self, instructions: list[tuple[str, str]]):
        self.instructions = instructions

    def set_register(self, reg: str, value: int):
        self.registers[reg] = value

    def run(self):
        while 0 <= self.counter < len(self.instructions):
            instr, args = self.instructions[self.counter]
            self.counter, self.registers = self.instruction_set[instr](args, self.counter, self.registers)
        return self.registers


class Instructions:
    @staticmethod
    def half_register(args: str, cntr: int, registers: dict[str, int]):
        registers[args] //= 2
        return cntr + 1, registers

    @staticmethod
    def triple_register(args: str, cntr: int, registers: dict[str, int]):
        registers[args] *= 3
        return cntr + 1, registers

    @staticmethod
    def increment_register(args: str, cntr: int, registers: dict[str, int]):
        registers[args] += 1
        return cntr + 1, registers

    @staticmethod
    def jump(args: str, cntr: int, registers: dict[str, int]):
        return cntr + int(args), registers

    @staticmethod
    def jump_if_even(args: str, cntr: int, registers: dict[str, int]):
        reg, offset = args.split(', ')
        if registers[reg] % 2 == 0:
            cntr += int(offset)
        else:
            cntr += 1
        return cntr, registers

    @staticmethod
    def jump_if_one(args: str, cntr: int, registers: dict[str, int]):
        reg, offset = args.split(', ')
        if registers[reg] == 1:
            cntr += int(offset)
        else:
            cntr += 1
        return cntr, registers
