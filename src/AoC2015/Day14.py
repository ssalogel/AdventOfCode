from AdventUtils.Day import Day


Reindeer = tuple[str, int, int, int]


class Day14(Day):
    def __init__(self, content=None):
        super().__init__(day=14, year=2015, content=content)

    def parse_content(self, content: str) -> list[Reindeer]:
        data = content.strip().split('\n')
        return [(d[0], int(d[3]), int(d[6]), int(d[-2])) for d in [d.split(' ') for d in data]]

    def part1(self, parsed_content: list[Reindeer]) -> int:
        distances = {}
        for reindeer, _, _, _ in parsed_content:
            distances[reindeer] = 0
        for i in range(2503):
            for r, speed, active, rest in parsed_content:
                if i % (active + rest) < active:
                    distances[r] += speed
        return max(distances.values())

    def part2(self, parsed_content: list[Reindeer]) -> int:
        distances = {}
        scores = {}
        for reindeer, _, _, _ in parsed_content:
            distances[reindeer] = 0
            scores[reindeer] = 0
        for i in range(2503):
            for r, speed, active, rest in parsed_content:
                if i % (active + rest) < active:
                    distances[r] += speed
            best_dist = max([dist for _, dist in distances.items()])
            for name, dist in distances.items():
                if dist == best_dist:
                    scores[name] += 1
        return max(scores.values())
