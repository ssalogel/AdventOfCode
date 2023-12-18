from typing import Iterable, Optional, Any, Callable
from collections import defaultdict
from itertools import permutations


Path = tuple[int, list[tuple[Any, Any]]]


class Graph:
    def __init__(self, nodes: Iterable[Any], default_value=lambda: float("inf")):
        self.node_names: set[Any] = set(nodes)
        self.connections: dict[Any, dict[Any, int]] = defaultdict(
            lambda: defaultdict(default_value)
        )

    def add_bi_connection(
        self,
        source: Any,
        dest: Any,
        dist_forward: int,
        dist_backward: Optional[int] = None,
    ):
        self.node_names.update([source, dest])
        self.connections[source][dest] = dist_forward
        self.connections[dest][source] = (
            dist_backward if dist_backward else dist_forward
        )

    def add_uni_connection(self, source: Any, dest: Any, dist: int):
        self.node_names.update([source, dest])
        self.connections[source][dest] = dist

    def get_best_route_total(self, comparator: Callable[[Any], Path] = min) -> Path:
        pairs = list(permutations(self.node_names))
        paths = [list(zip(pair, pair[1:])) for pair in pairs]
        paths_costs: list[Path] = []
        for path in paths:
            paths_costs.append(
                (sum([self.connections[src][dest] for src, dest in path]), path)
            )
        return comparator(paths_costs)

    def get_best_two_way_round_total(
        self, comparator: Callable[[Any], Path] = min
    ) -> Path:
        pairs = list(permutations(self.node_names))
        paths = [list(zip(pair, pair[1:] + (pair[0],))) for pair in pairs]
        paths_costs: list[Path] = []
        for path in paths:
            paths_costs.append(
                (
                    sum(
                        [
                            self.connections[src][dest] + self.connections[dest][src]
                            for src, dest in path
                        ]
                    ),
                    path,
                )
            )
        return comparator(paths_costs)
