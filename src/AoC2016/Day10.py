from src.AdventUtils.Day import Day
from collections import defaultdict


class Day10(Day):
    def __init__(self, content=None):
        super().__init__(day=10, year=2016, content=content)

    def parse_content(self, content: str) -> list[str]:
        return sorted(content.split('\n'))

    def create_start(self, states: list[str]) -> tuple[dict[int, list[int]], dict[int, tuple[tuple[str, int], tuple[str, int]]]]:
        bots = defaultdict(list)
        pipeline = {}
        for line in states:
            info = line.split(' ')
            if info[0] == 'bot':
                bot, low_id, low_v, high_id, high_v = int(info[1]), info[5], int(info[6]), info[-2], int(info[-1])
                pipeline[bot] = (low_id, low_v), (high_id, high_v)
            elif info[0] == 'value':
                bots[int(info[-1])].append(int(info[1]))
        return bots, pipeline

    def part1(self, parsed_content: list[str]) -> int:
        bots, pipeline = self.create_start(parsed_content)
        outputs = [0] * 100
        while bots:
            for bot, v in dict(bots).items():
                if len(v) == 2:
                    low, high = sorted(v)
                    if low == 17 and high == 61:
                        return bot
                    bots.pop(bot)
                    low_dest, high_dest = pipeline[bot]
                    if low_dest[0] == 'output':
                        outputs[low_dest[1]] = low
                    else:
                        bots[low_dest[1]].append(low)

                    if high_dest[0] == 'output':
                        outputs[high_dest[1]] = high
                    else:
                        bots[high_dest[1]].append(high)
        return -1

    def part2(self, parsed_content: list[str]) -> int:
        bots, pipeline = self.create_start(parsed_content)
        outputs = [0] * 100
        while bots:
            for bot, v in dict(bots).items():
                if len(v) == 2:
                    low, high = sorted(v)
                    bots.pop(bot)
                    low_dest, high_dest = pipeline[bot]
                    if low_dest[0] == 'output':
                        outputs[low_dest[1]] = low
                    else:
                        bots[low_dest[1]].append(low)

                    if high_dest[0] == 'output':
                        outputs[high_dest[1]] = high
                    else:
                        bots[high_dest[1]].append(high)
        return outputs[0] * outputs[1] * outputs[2]
