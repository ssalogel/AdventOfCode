from src.AdventUtils.Day import Day
from itertools import cycle
from functools import lru_cache


class Day21(Day):
    def __init__(self, content=None):
        super().__init__(day=21, year=2021, content=content)

    def roll(self):
        for n in cycle(range(1, 101)):
            yield n

    def parse_content(self, content: str):
        return [int(e[1:]) for e in content.replace('Player ', '').replace(' starting position: ', '').split('\n')]

    def part1(self, parsed_content) -> int:
        play1, play2, *_ = parsed_content
        play1 -= 1
        play2 -= 1
        player = {0: play1, 1: play2}
        scores = {0: 0, 1: 0}
        die = self.roll()
        for turn, a in enumerate(zip(die, die, die)):
            move = sum(a)
            play = turn % 2
            player[play] = (player[play] + move) % 10
            scores[play] += player[play] + 1
            if scores[play] >= 1000:
                return scores[(play + 1) % 2] * 3 * (turn + 1)

    @lru_cache(maxsize=None)
    def play(self, p1: int, s1: int, p2: int, s2: int) -> tuple[int, int]:
        if s1 >= 21:
            return 1, 0
        if s2 >= 21:
            return 0, 1
        res = (0, 0)
        for d1 in range(1, 4):
            for d2 in range(1, 4):
                for d3 in range(1, 4):
                    np1 = (p1 + d1 + d2 + d3) % 10
                    ns1 = s1 + np1 + 1

                    w1, w2 = self.play(p2, s2, np1, ns1)
                    res = (res[0] + w2, res[1] + w1)
        return res

    def part2(self, parsed_content) -> int:
        play1, play2, *_ = parsed_content
        return max(self.play(play1 - 1, 0, play2 - 1, 0))


if __name__ == '__main__':
    input_content = """Player 1 starting position: 4
Player 2 starting position: 8"""
    #input_content = None
    d = Day21(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
