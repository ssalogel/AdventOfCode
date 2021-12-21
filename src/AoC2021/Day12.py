from src.AdventUtils.Day import Day
from src.AdventUtils.Graph import Graph


class PassGraph(Graph):
    def get_all_routes_small_once(self, start: str, end: str):
        visited = {start}
        routes = []
        for connection in self.connections[start]:
            routes += self._recur_get_all_paths_small_once(connection, end, visited, [start, connection])
        return routes

    def _recur_get_all_paths_small_once(self, pos: str, target: str, visited: set[str], path: list[str]):
        if pos == target:
            return [path]
        possible_paths = []
        if pos.islower():
            visited = {pos}.union(visited)
        for connection in self.connections[pos]:
            if connection in visited:
                continue
            possible_paths += self._recur_get_all_paths_small_once(connection, target, visited, path + [connection])
        return possible_paths

    def get_all_routes_one_small_twice(self, start: str, end: str):
        visited = {start}
        routes = []
        for connection in self.connections[start]:
            routes += self._recur_get_all_paths_one_small_twice(start, connection, end, visited, [start, connection], False)
        return routes

    def _recur_get_all_paths_one_small_twice(self, start: str, pos: str, target: str, visited: set[str], path: list[str], extra_done):
        if pos == target:
            return [path]
        if pos == start:
            return []
        possible_paths = []
        if pos.islower():
            visited = {pos}.union(visited)
        for connection in self.connections[pos]:
            if connection in visited and extra_done:
                continue
            possible_paths += self._recur_get_all_paths_one_small_twice(start, connection, target, visited,
                                                                        path + [connection], connection in visited or extra_done)
        return possible_paths


class Day12(Day):
    def __init__(self, content=None):
        super().__init__(day=12, year=2021, content=content)

    def parse_content(self, content: str):
        res = []
        for line in content.strip().split('\n'):
            res.append(line.split('-'))
        return res

    def part1(self, parsed_content) -> int:
        s = set(sum(parsed_content, []))
        graph = PassGraph(nodes=s)
        for source, dest in parsed_content:
            graph.add_bi_connection(source, dest, 1)
        return len(graph.get_all_routes_small_once('start', 'end'))

    def part2(self, parsed_content) -> int:
        s = set(sum(parsed_content, []))
        graph = PassGraph(nodes=s)
        for source, dest in parsed_content:
            graph.add_bi_connection(source, dest, 1)
        return len(graph.get_all_routes_one_small_twice('start', 'end'))
