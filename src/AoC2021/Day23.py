from src.AdventUtils.Day import Day
from queue import PriorityQueue


class Day23(Day):
    def __init__(self, content=None):
        super().__init__(day=23, year=2021, content=content)
        self.costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
        self.hallway = [14, 15, 17, 19, 21, 23, 24]
        self.entrances = [16, 18, 20, 22]
        self.houses = []

    def parse_content(self, content: str):
        return "".join(content.strip().splitlines())

    def is_win(self, current_map: str) -> bool:
        for ix, hou in enumerate(self.houses):
            if any(current_map[h] != "ABCD"[ix] for h in hou):
                return False
        return True

    def moves_out(self, start_map) -> list[tuple[int, str]]:
        valid_moves = []

        # figure out the location and costs for each top house
        house_tops = []
        tops_distances = []
        for ix, home in enumerate(self.houses):
            well_placed = True
            top = None
            top_dist = len(home) + 1
            for pos in reversed(home):
                if start_map[pos] == ".":
                    break
                if start_map[pos] != "ABCD"[ix]:
                    well_placed = False
                if not well_placed:
                    top = pos
                top_dist -= 1
            house_tops.append(top)
            tops_distances.append(top_dist)

        # move out the top of each house
        for ix in range(4):
            # empty house
            if house_tops[ix] is None:
                continue
            moving_ix = house_tops[ix]
            entry = self.entrances[ix]
            for dest_ix in self.hallway:
                if all(
                    start_map[pos] == "."
                    for pos in range(min(dest_ix, entry), max(dest_ix, entry) + 1)
                ):
                    char = start_map[moving_ix]
                    n_map = f"{start_map[:dest_ix]}{char}{start_map[dest_ix + 1:moving_ix]}.{start_map[moving_ix + 1:]}"
                    dist = (tops_distances[ix] + abs(entry - dest_ix)) * self.costs[
                        char
                    ]

                    # after moving someone out of a house, try to move everyone that could back in
                    while True:
                        n_dist, n_map = self.moves_in(n_map)
                        dist += n_dist
                        if n_dist == 0:
                            # nobody else can move in
                            break
                    valid_moves.append((dist, n_map))
        return valid_moves

    def moves_in(self, start_map) -> tuple[int, str]:
        for ix, hou in enumerate(self.houses):
            opening = None
            h_id = "ABCD"[ix]
            hole_dist = len(hou)
            for room in reversed(hou):
                if start_map[room] == ".":
                    opening = room
                    break
                if start_map[room] != h_id:
                    break
                hole_dist -= 1
            if opening is None:
                continue

            entry = self.entrances[ix]
            for pos in self.hallway:
                #             right house                          empty between entry and me
                if all(
                    (x == pos and h_id == start_map[x])
                    or (pos != x and start_map[x] == ".")
                    for x in range(min(pos, entry), max(pos, entry) + 1)
                ):
                    dist = (hole_dist + abs(pos - entry)) * self.costs[h_id]
                    n_map = f"{start_map[:pos]}.{start_map[pos+1:opening]}{h_id}{start_map[opening+1:]}"
                    return dist, n_map
        return 0, start_map

    def solve(self, start_map):
        queue = PriorityQueue()
        queue.put((0, start_map))
        visited = set()
        while not queue.empty():
            cost, curr_map = queue.get()
            if self.is_win(curr_map):
                return cost, curr_map
            if curr_map in visited:
                continue
            visited.add(curr_map)
            for n_cost, n_map in self.moves_out(curr_map):
                if n_map not in visited:
                    queue.put((n_cost + cost, n_map))
        return -1, curr_map

    def part1(self, parsed_content) -> int:
        self.houses = [[29, 42], [31, 44], [33, 46], [35, 48]]
        cost, end_map = self.solve(parsed_content)
        return cost

    def part2(self, parsed_content) -> int:
        self.houses = [
            [29, 42, 55, 68],
            [31, 44, 57, 70],
            [33, 46, 59, 72],
            [35, 48, 61, 74],
        ]
        start_map = (
            f"{parsed_content[:13*3]}  #D#C#B#A#    #D#B#A#C#  {parsed_content[13*3:]}"
        )
        cost, end_map = self.solve(start_map)
        return cost


if __name__ == "__main__":
    input_content = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
    input_content = None
    d = Day23(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
