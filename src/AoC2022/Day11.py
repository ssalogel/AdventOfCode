from typing import Callable
from functools import partial
from src.AdventUtils.Day import Day
from math import lcm


class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.operation = lambda x: x
        self.test = 1
        self.if_true = self
        self.if_false = self
        self.inspections = 0

    def setup(
        self,
        items: list[int],
        increaser: Callable[[int], int],
        test: int,
        if_true: "Monkey",
        if_false: "Monkey",
    ):
        self.items.extend(items)
        self.operation = increaser
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

    def inspect_all(self):
        while len(self.items) > 0:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item //= 3
            if item % self.test == 0:
                self.if_true.receive(item)
            else:
                self.if_false.receive(item)

    def inspect_all_2(self, divisor):
        while len(self.items) > 0:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item %= divisor
            if item % self.test == 0:
                self.if_true.receive(item)
            else:
                self.if_false.receive(item)

    def receive(self, item):
        self.items.append(item)

    def __repr__(self):
        return f"Monkey {self.name}"


class Day11(Day):
    def __init__(self, content=None):
        super().__init__(day=11, year=2022, content=content)

    def parse_content(self, content: str):
        res = [Monkey(i) for i, _ in enumerate(content.strip().split("\n\n"))]

        for ix, monkey in enumerate(content.strip().split("\n\n")):
            name, items, op, test, true, false = monkey.splitlines()
            items = list(
                map(int, items.strip().removeprefix("Starting items: ").split(", "))
            )
            if "+" in op:
                if op.split("+ ")[-1].isnumeric():
                    value = int(op.split("+ ")[-1])
                    operation = partial(lambda x, y: y + x, value)
                else:
                    operation = lambda x: x * x
            else:
                if op.split("* ")[-1].isnumeric():
                    value = int(op.split("* ")[-1])
                    operation = partial(lambda x, y: x * y, value)
                else:
                    operation = lambda x: x * x
            test = int(test.split(" ")[-1])
            true = int(true.split(" ")[-1])
            false = int(false.split(" ")[-1])
            res[ix].setup(items, operation, test, res[true], res[false])
        return res

    def part1(self, parsed_content) -> int:
        for _ in range(20):
            for monkey in parsed_content:
                monkey.inspect_all()
        return (
            sorted([x.inspections for x in parsed_content])[-1]
            * sorted([x.inspections for x in parsed_content])[-2]
        )

    def part2(self, parsed_content) -> int:
        divisor = lcm(*[monkey.test for monkey in parsed_content])
        for _ in range(10000):
            for monkey in parsed_content:
                monkey.inspect_all_2(divisor)
        return (
            max([x.inspections for x in parsed_content])
            * sorted([x.inspections for x in parsed_content])[-2]
        )


if __name__ == "__main__":
    input_content = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
    d = Day11(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
