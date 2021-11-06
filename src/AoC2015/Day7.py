from AdventUtils.Day import Day
from AdventUtils.Math import bitwise_and, bitwise_or, bitwise_not, bitwise_rshift, bitwise_lshift


class Day7(Day):
    def __init__(self, content=None):
        super().__init__(day=7, year=2015, content=content)

    def parse_content(self):
        data = self.content.strip().split('\n')
        return [(d.split(' '), k) for d, k in [tuple(d.split(' -> ')) for d in data]]

    def part1(self):
        solved = {}
        mask = 0xffff
        while 'a' not in solved:
            unsolved = []
            for op, target in self.data_p1:
                if len(op) == 1:
                    if op[0].isdigit():
                        solved[target] = int(op[0])
                    elif op[0] in solved:
                        solved[target] = solved[op[0]]
                    else:
                        unsolved.append((op, target))
                elif len(op) == 2:
                    if op[1] in solved:
                        solved[target] = bitwise_not(solved[op[1]], mask)
                    else:
                        unsolved.append((op, target))
                elif len(op) == 3:
                    if op[1] == 'AND' or op[1] == 'OR':
                        if op[0] in solved and op[2] in solved:
                            if op[1] == 'AND':
                                solved[target] = bitwise_and(solved[op[0]], solved[op[2]], mask)
                            elif op[1] == 'OR':
                                solved[target] = bitwise_or(solved[op[0]], solved[op[2]], mask)
                        elif op[0].isdigit() and op[2] in solved:
                            if op[1] == 'AND':
                                solved[target] = bitwise_and(int(op[0]), solved[op[2]], mask)
                            elif op[1] == 'OR':
                                solved[target] = bitwise_or(int(op[0]), solved[op[2]], mask)
                        else:
                            unsolved.append((op, target))
                    else:
                        if op[0] in solved:
                            if op[1] == 'LSHIFT':
                                solved[target] = bitwise_lshift(solved[op[0]], int(op[2]), mask)
                            elif op[1] == 'RSHIFT':
                                solved[target] = bitwise_rshift(solved[op[0]], int(op[2]), mask)
                        else:
                            unsolved.append((op, target))
                else:
                    raise NotImplementedError
            self.data_p1 = unsolved
        return solved['a']

    def part2(self):
        changed_data = []
        self.data_p1 = self.data_p2
        for op, target in self.data_p2:
            if target == 'b':
                op = [str(self.part1())]
            changed_data.append((op, target))
        self.data_p1 = changed_data
        return self.part1()
