import math

from src.AdventUtils.Day import Day
import re


class Day4(Day):
    def __init__(self, content=None):
        super().__init__(day=4, year=2023, content=content)

    def parse_content(self, content: str):
        return [x.split(':')[1] for x in content.splitlines()]

    def part1(self, parsed_content) -> int:
        res = []
        for line in parsed_content:
            score = 0.5
            winning, gotten = line.split('|')
            winnings = [int(x) for x in re.findall(r'(\d+)', winning)]
            for number in [int(x) for x in re.findall(r'(\d+)', gotten)]:
                if number in winnings:
                    score *= 2
            res.append(math.floor(score))
        return sum(res)

    def part2(self, parsed_content) -> int:
        res = {i: 1 for i in range(len(parsed_content))}
        for i, line in enumerate(parsed_content):
            score = 0
            winning, gotten = line.split('|')
            winnings = [int(x) for x in re.findall(r'(\d+)', winning)]
            for number in [int(x) for x in re.findall(r'(\d+)', gotten)]:
                if number in winnings:
                    score += 1
            for card in range(i+1, i+score+1):
                res[card] += res[i]
        return sum(res.values())


if __name__ == "__main__":
    input_content = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    d = Day4(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
