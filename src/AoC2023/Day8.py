import math
from itertools import cycle

from src.AdventUtils.Day import Day
from ast import literal_eval

class Day8(Day):
    def __init__(self, content=None):
        super().__init__(day=8, year=2023, content=content)

    def parse_content(self, content: str):
        instr, nodes_str = content.split("\n\n")
        nodes = {}
        for node_str in nodes_str.strip().split("\n"):
            node_or, tup_str = node_str.split(' = ')
            nodes[node_or] = literal_eval(tup_str.replace('(', '("').replace(", ", '","').replace(')', '")'))
        return instr, nodes

    def part1(self, parsed_content) -> int:
        curr = "AAA"
        instr, nodes = parsed_content
        step = 0
        for direction in cycle(instr):
            step += 1
            curr = nodes[curr][direction == 'R']
            if curr == 'ZZZ':
                break
        return step

    def part2(self, parsed_content) -> int:
        instr, nodes = parsed_content
        curr = [x for x in nodes if x.endswith('A')]
        goal = []
        for ghost in curr:
            step = 0
            pos = ghost
            for direction in cycle(instr):
                step += 1
                pos = nodes[pos][direction == 'R']
                if pos.endswith('Z'):
                    goal.append(step)
                    break
        return math.lcm(*goal)


if __name__ == "__main__":
    input_content = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
    d = Day8(content=input_content)
    #print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
