from src.AdventUtils.Day import Day
from queue import PriorityQueue
import re


class Day11(Day):
    def __init__(self, content=None):
        super().__init__(day=11, year=2016, content=content)
        self.queue: PriorityQueue[
            tuple[int, int, list[list[int]], str]
        ] = PriorityQueue()
        self.visited: set[str] = set()

    def parse_content(self, content: str) -> list[list[list[str]]]:
        floors = content.strip().split("\n")
        microchips_pattern = re.compile(r"(\w+)-compatible")
        generator_pattern = re.compile(r"(\w+) generator")
        return [
            [
                [str(x) for x in microchips_pattern.findall(f)],
                [str(x) for x in generator_pattern.findall(f)],
            ]
            for f in floors
        ]

    @staticmethod
    def get_elements_mapping(content: list[list[list[str]]]) -> dict[str, int]:
        return dict(
            (v, ix + 1)
            for ix, v in enumerate([el for chip, gen in content for el in chip])
        )

    @staticmethod
    def repr_ligth(elev, floors):
        return f"{elev}${[(len(floor), sum(x < 0 for x in floor)) for floor in floors]}"

    def solve(
        self,
        floors: list[list[int]],
    ) -> int:
        end_repr = self.repr_ligth(3, [[], [], [], sum(floors, [])])
        self.visited = set()
        self.queue = PriorityQueue()
        curr_repr = self.repr_ligth(0, floors)
        self.queue.put((0, 0, floors, curr_repr))

        while True:
            elev, moves, floors, curr_repr = self.queue.get()
            if curr_repr == end_repr:
                return moves
            if curr_repr in self.visited:
                continue

    def part1(self, parsed_content: list[list[list[str]]]) -> int:
        mapping = self.get_elements_mapping(parsed_content)
        floors = [
            [mapping[x] for x in lev[0]] + [-mapping[x] for x in lev[1]]
            for lev in parsed_content
        ]
        return self.solve(floors)

    def part2(self, parsed_content) -> int:
        pass


if __name__ == "__main__":
    content = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""
    d = Day11(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))
