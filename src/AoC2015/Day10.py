from AdventUtils.Day import Day


class Day10(Day):
    def __init__(self, content=None):
        super().__init__(day=10, year=2015, content=content)

    def parse_content(self) -> str:
        return self.content.strip()

    def step(self, string: str) -> str:
        count = 0
        res = ''
        for i, c in enumerate(string[:-1]):
            count += 1
            if string[i + 1] == c:
                continue
            else:
                res += f"{str(count)}{c}"
                count = 0
        res += f"{str(count + 1)}{string[-1]}"
        return res

    def part1(self) -> int:
        res = self.data_p1
        for _ in range(40):
            res = self.step(res)
        return len(res)

    def part2(self) -> int:
        res = self.data_p2
        for _ in range(50):
            res = self.step(res)
        return len(res)
