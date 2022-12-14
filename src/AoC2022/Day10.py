from src.AdventUtils.Day import Day


class Day10(Day):
    def __init__(self, content=None):
        super().__init__(day=10, year=2022, content=content)

    def parse_content(self, content: str):
        return content.strip().splitlines()

    def part1(self, parsed_content) -> int:
        cycle = 0
        acc = 1
        res = 0
        for instr in parsed_content:
            cycle += 1
            if (cycle + 20) % 40 == 0:
                res += cycle * acc
            if instr == "noop":
                continue
            cycle += 1
            if (cycle + 20) % 40 == 0:
                res += cycle * acc
            command, amount = instr.split(' ')
            amount = int(amount)
            acc += amount
        return res

    def part2(self, parsed_content) -> str:
        cycle = 0
        acc = 1
        res = []
        for instr in parsed_content:
            cycle += 1
            res.append('#') if abs(acc - ((cycle - 1) % 40)) <= 1 else res.append('.')
            if instr == "noop":
                continue
            cycle += 1
            res.append('#') if abs(acc - ((cycle - 1) % 40)) <= 1 else res.append('.')
            command, amount = instr.split(' ')
            amount = int(amount)
            acc += amount
        return '\n'.join([''.join(res[i:i+40]) for i in range(0, len(res), 40)])


if __name__ == '__main__':
    input_content = """noop
addx 3
addx -5
"""
    input_content = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    d = Day10(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
