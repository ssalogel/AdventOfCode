from AdventUtils.Day import Day
from AdventUtils.Graph import Graph


class Day13(Day):
    def __init__(self, content=None):
        super().__init__(day=13, year=2015, content=content)

    def parse_content(self) -> list[tuple[str, str, int, str]]:
        data = self.content.replace('.', '').split('\n')
        return [(d[0], d[2], int(d[3]), d[len(d)-1]) for d in [d.split(' ') for d in data]]

    def part1(self) -> int:
        people = set(x[0] for x in self.data_p1)
        graph = Graph(nodes=people, default_value=lambda: float('-inf'))
        for a, sign, hap, b in self.data_p1:
            value = hap if sign == 'gain' else -hap
            graph.add_uni_connection(source=a, dest=b, dist=value)
        return graph.get_best_two_way_round_total(max)[0]

    def part2(self):
        people = set(x[0] for x in self.data_p1)
        graph = Graph(nodes=people)
        for a, sign, hap, b in self.data_p1:
            value = hap if sign == 'gain' else -hap
            graph.add_uni_connection(source=a, dest=b, dist=value)
        for p in people:
            graph.add_bi_connection(source="me", dest=p, dist_forward=0, dist_backward=0)
        return graph.get_best_two_way_round_total(max)[0]
