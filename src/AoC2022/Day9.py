from src.AdventUtils.Day import Day
from src.AdventUtils import Grid2D


class Day9(Day):
    def __init__(self, content=None):
        super().__init__(day=9, year=2022, content=content)

    def parse_content(self, content: str):
        return [(instr[0], int(instr[2:])) for instr in content.strip().splitlines()]

    def resolve_distance(self, mover: Grid2D.Position2D, attached: Grid2D.Position2D) -> Grid2D.Position2D:
        if mover.x != attached.x:
            if mover.x > attached.x:
                attached = attached.move_right()
            else:
                attached = attached.move_left()
        if mover.y != attached.y:
            if mover.y > attached.y:
                attached = attached.move_up()
            else:
                attached = attached.move_down()
        return attached

    def part1(self, parsed_content) -> int:
        head = Grid2D.Position2D(0, 0)
        tail = Grid2D.Position2D(0, 0)
        tail_visited: set[Grid2D.Position2D] = {tail}
        for direction, mag in parsed_content:
            for _ in range(mag):
                if direction == 'U':
                    head = head.move_up()
                elif direction == 'D':
                    head = head.move_down()
                elif direction == 'R':
                    head = head.move_right()
                elif direction == 'L':
                    head = head.move_left()
                else:
                    assert False, "wtf direction"
                if (tail.x, tail.y) in Grid2D.get_neighbours_dig_with_self_unbound(head.x, head.y):
                    continue
                tail = self.resolve_distance(head, tail)
                tail_visited.add(tail)

        return len(tail_visited)

    def part2(self, parsed_content) -> int:
        rope = [Grid2D.Position2D(0, 0) for _ in range(10)]
        tail_visited = {rope[-1]}
        for direction, mag in parsed_content:
            for _ in range(mag):
                if direction == 'U':
                    rope[0] = rope[0].move_up()
                elif direction == 'D':
                    rope[0] = rope[0].move_down()
                elif direction == 'R':
                    rope[0] = rope[0].move_right()
                elif direction == 'L':
                    rope[0] = rope[0].move_left()
                else:
                    assert False, "wtf direction"
                for i, point in enumerate(rope[1:]):
                    if (point.x, point.y) in Grid2D.get_neighbours_dig_with_self_unbound(rope[i].x, rope[i].y):
                        continue
                    rope[i + 1] = self.resolve_distance(rope[i], rope[i + 1])
                tail_visited.add(rope[-1])
        return len(tail_visited)


if __name__ == '__main__':
    input_content = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    d = Day9(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
