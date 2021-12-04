from AdventUtils.Day import Day
from AdventUtils.Graph import Graph


class Day9(Day):
    def __init__(self, content=None):
        super().__init__(day=9, year=2015, content=content)

    def parse_content(self, content: str) -> list[tuple[int, str, str]]:
        data = content.split('\n')
        return [(int(s[-1]), s[0], s[2]) for s in [d.split(' ') for d in data]]

    def part1(self, parsed_content: list[tuple[int, str, str]]) -> int:
        data = parsed_content
        data.sort()
        graph = Graph([])
        for dist, src, dest in data:
            graph.add_bi_connection(source=src, dest=dest, dist_forward=dist)
        return graph.get_best_route_total()[0]

    def part2(self, parsed_content: list[tuple[int, str, str]]) -> int:
        data = parsed_content
        towns = set([x for _, x, _ in data] + [x for _, _, x in data])
        graph = Graph(towns, lambda: float("-inf"))
        for dist, src, dest in data:
            graph.add_bi_connection(source=src, dest=dest, dist_forward=dist)
        return graph.get_best_route_total(max)[0]
