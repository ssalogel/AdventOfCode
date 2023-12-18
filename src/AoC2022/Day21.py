from typing import Callable
from src.AdventUtils.Day import Day
import operator


class HumanException(Exception):
    pass


class Node:
    eq: tuple[str, str, Callable[[float, float], float]]

    def __init__(self, name, node_dict, part2: bool = False):
        self.name = name
        self.nodes = node_dict
        self._value = None
        self.part2 = part2
        self.og_eq: str = ""
        self.solved = False

    def add_solver(self, eq: str):
        self.og_eq = eq
        if eq.isnumeric():
            self._value = int(eq)
        else:
            operand1, op, operand2 = eq.strip().split(" ")
            self.eq = (operand1, operand2, op_conv[op])

    @property
    def value(self):
        if self._value is None:
            operand1, operand2, op = self.eq
            self._value = op(self.nodes[operand1].value, self.nodes[operand2].value)
        if self.part2 and self.name == "humn":
            raise HumanException
        return self._value

    def __repr__(self):
        return f"{self.name}: {self.og_eq}"


op_conv = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv}


class Day21(Day):
    def __init__(self, content=None):
        super().__init__(day=21, year=2022, content=content)

    def parse_content(self, content: str):
        return [line.split(": ") for line in content.strip().splitlines()]

    def make_tree(self, source: list[list[str]], part2: bool= False):
        nodes = {}
        for node, eq in source:
            nodes[node] = Node(node, nodes, part2)
            nodes[node].add_solver(eq)
        return nodes

    def part1(self, parsed_content) -> int:
        tree = self.make_tree(parsed_content)
        return int(tree["root"].value)

    def reverse(self, tree: dict[str, Node], target: float, root: str):
        new_target = float("inf")
        curr = tree[root]
        if "humn" in curr.og_eq:
            pass
        to_reverse = curr.og_eq.split(" ")[1]
        try:
            operand = tree[curr.eq[0]].value
            to_dig = curr.eq[1]
            if to_reverse == "+":
                new_target = target - operand
            elif to_reverse == "-":
                new_target = operand - target
            elif to_reverse == "*":
                new_target = target // operand
            elif to_reverse == "/":
                new_target = operand // target
        except HumanException:
            operand = tree[curr.eq[1]].value
            to_dig = curr.eq[0]
            if to_reverse == "+":
                new_target = target - operand
            elif to_reverse == "-":
                new_target = target + operand
            elif to_reverse == "*":
                new_target = target // operand
            elif to_reverse == "/":
                new_target = target * operand
        return new_target, to_dig

    def part2(self, parsed_content) -> int:
        tree = self.make_tree(parsed_content, True)
        try:
            target = tree[tree["root"].eq[0]].value
            to_dig = tree["root"].eq[1]
        except HumanException:
            target = tree[tree["root"].eq[1]].value
            to_dig = tree["root"].eq[0]
        while to_dig != "humn":
            target, to_dig = self.reverse(tree, target, to_dig)
        return int(target)


if __name__ == "__main__":
    input_content = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""
    d = Day21(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
