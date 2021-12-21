from src.AdventUtils.Graph import Graph


def test_default_values():
    assert Graph([]).connections[1][0] == float("inf")
    assert Graph([], lambda: float('-inf')).connections[1][0] == float("-inf")


def test_add_bi_connection():
    graph = Graph([])
    graph.add_bi_connection(0, 1, 10, 5)
    graph.add_bi_connection(0, 2, 3)
    assert 0 in graph.node_names
    assert 1 in graph.node_names
    assert 2 in graph.node_names
    assert graph.connections[0][1] == 10
    assert graph.connections[1][0] == 5
    assert graph.connections[0][2] == graph.connections[2][0]


def test_get_best_route_total():
    graph = Graph([])
    graph.add_bi_connection(0, 1, 10, 5)
    graph.add_bi_connection(0, 2, 3)
    assert graph.get_best_route_total()[0] == 8
