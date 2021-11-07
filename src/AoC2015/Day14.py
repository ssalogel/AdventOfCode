from AdventUtils.Day import Day


class Day14(Day):
    def __init__(self, content=None):
        super().__init__(day=14, year=2015, content=content)

    def parse_content(self) -> list[tuple[str, int, int, int]]:
        data = self.content.strip().split('\n')
        return [(d[0], int(d[3]), int(d[6]), int(d[-2])) for d in [d.split(' ') for d in data]]

    def part1(self):
        distances = {}
        for reindeer, _, _, _ in self.data_p1:
            distances[reindeer] = 0
        for i in range(2503):
            for r, speed, active, rest in self.data_p1:
                if i % (active + rest) < active:
                    distances[r] += speed
        return max(distances.values())

    def part2(self):
        distances = {}
        scores = {}
        for reindeer, _, _, _ in self.data_p1:
            distances[reindeer] = 0
            scores[reindeer] = 0
        for i in range(2503):
            for r, speed, active, rest in self.data_p1:
                if i % (active + rest) < active:
                    distances[r] += speed
            best_dist = max([dist for _, dist in distances.items()])
            for name, dist in distances.items():
                if dist == best_dist:
                    scores[name] += 1
        return max(scores.values())
