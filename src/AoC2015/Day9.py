from AdventUtils.Day import Day
from AdventUtils.Graph import Graph


class Day9(Day):
    def __init__(self, content=None):
        super().__init__(day=9, year=2015, content=content)

    def parse_content(self) -> list[tuple[int, str, str]]:
        data = self.content.split('\n')
        return [(int(s[-1]), s[0], s[2]) for s in [d.split(' ') for d in data]]

    def part1(self):
        data = self.data_p1
        data.sort()
        # the graph approach work, but what follows is much more optimized (works with my specific input)
        # graph = Graph([])
        # for dist, src, dest in data:
        #     graph.add_bi_connection(source=src, dest=dest, dist_forward=dist)
        # return graph.get_best_route_total()[0]
        total = 0
        town_num = len(set([x for _, x, _ in data] + [x for _, _, x in data]))
        half_sorted: set[str] = set()
        done: set[str] = set()
        while len(done) < town_num - 2 and len(half_sorted) != town_num:
            dist, pos1, pos2 = data.pop(0)
            if pos1 in done or pos2 in done:
                continue
            total += dist
            for pos in [pos1, pos2]:
                if pos not in half_sorted:
                    half_sorted.add(pos)
                else:
                    done.add(pos)
        return total

    def part2(self):
        data = self.data_p2
        towns = set([x for _, x, _ in data] + [x for _, _, x in data])
        graph = Graph(towns, lambda: float("-inf"))
        for dist, src, dest in data:
            graph.add_bi_connection(source=src, dest=dest, dist_forward=dist)
        return graph.get_best_route_total(max)[0]
