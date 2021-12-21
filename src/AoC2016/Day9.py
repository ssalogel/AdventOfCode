from src.AdventUtils.Day import Day
from collections import deque


class Day9(Day):
    def __init__(self, content=None):
        super().__init__(day=9, year=2016, content=content)

    def parse_content(self, content: str) -> str:
        return content

    def decompress(self, text: str) -> str:
        stream = deque(text)
        res = []
        while '(' in stream:
            for _ in range(stream.index('(')):
                res.append(stream.popleft())
            stream.popleft()
            marker = []
            for _ in range(stream.index(')')):
                marker.append(stream.popleft())
            stream.popleft()
            amount, times = ''.join(marker).split('x')
            to_repeat = []
            for _ in range(int(amount)):
                to_repeat.append(stream.popleft())
            res.extend(to_repeat*int(times))
        return ''.join(res + list(stream))

    def part1(self, parsed_content: str) -> int:
        return len(self.decompress(parsed_content))

    def part2(self, parsed_content: str) -> int:
        compressed: str = parsed_content
        weight = [1] * len(compressed)
        ix = 0
        while ix < len(compressed):
            if compressed[ix] == '(':
                end = compressed.find(')', ix)
                amount, times = compressed[ix+1:end].split('x')
                for i in range(ix, end+1):
                    weight[i] = 0
                for i in range(int(amount)):
                    weight[end+1+i] *= int(times)
                ix = end
            ix += 1
        return sum(weight)
