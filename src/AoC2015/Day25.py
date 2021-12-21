from src.AdventUtils.Day import Day


class Day25(Day):
    def __init__(self, content=None):
        super().__init__(day=25, year=2015, content=content)
        self.start = 20151125

    def parse_content(self, content: str) -> tuple[int, int]:
        data = content.replace('.', '').replace(',', '').split(' ')
        return int(data[-1]), int(data[-3])

    def part1(self, parsed_content: tuple[int, int]) -> int:
        x_target, y_target = parsed_content
        x, y = 1, 1
        num = self.start
        while x != x_target or y != y_target:
            if y == 1:
                x, y = 1, x + 1
            else:
                x, y = x + 1, y - 1
            num = (num * 252533) % 33554393
        return num

    def part2(self, parsed_content: tuple[int, int]) -> str:
        return "WINNER!"
