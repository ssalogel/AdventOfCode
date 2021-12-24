from src.AdventUtils.Day import Day


Rectangle = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]
Action = tuple[str, Rectangle]
State = tuple[int, Rectangle]


class Day22(Day):
    def __init__(self, content=None):
        super().__init__(day=22, year=2021, content=content)

    def parse_content(self, content: str) -> list[Action]:
        res = []
        for line in content.strip().splitlines():
            action, dims, *_ = line.split()
            xs, ys, zs, *_ = [(int(x[2:x.index('..')]), int(x[x.index('..')+2:])) for x in dims.split(',')]
            xs = (min(xs), max(xs))
            ys = (min(ys), max(ys))
            zs = (min(zs), max(zs))
            res.append((action, (xs, ys, zs)))
        return res

    @staticmethod
    def apply(action: Action, states: list[State]):
        state, ((x1, x2), (y1, y2), (z1, z2)) = action
        to_add = []

        for st, ((xp1, xp2), (yp1, yp2), (zp1, zp2)) in states:
            if xp2 < x1 or x2 < xp1 or yp2 < y1 or y2 < yp1 or zp2 < z1 or z2 < zp1:
                # no intersection
                continue
            # common length
            cx1 = max(x1, xp1)
            cx2 = min(x2, xp2)
            cy1 = max(y1, yp1)
            cy2 = min(y2, yp2)
            cz1 = max(z1, zp1)
            cz2 = min(z2, zp2)

            # both on: cancel the overlapping double count
            # old on, new off: negates that overlap
            # both off: cancel the overlapping double count
            # old off, new on: negate that negative square
            to_add.append((-1*st, ((cx1, cx2), (cy1, cy2), (cz1, cz2))))
        if state == "on":
            states.append((1, ((x1, x2), (y1, y2), (z1, z2))))
        for elem in to_add:
            states.append(elem)

    @staticmethod
    def count_on(states: list[State]):
        s = 0
        for st, ((x1, x2), (y1, y2), (z1, z2)) in states:
            if not st:
                continue
            s += st * (abs(x2-x1+1) * abs(y2-y1+1) * abs(z2-z1+1))
        return s

    def part1(self, parsed_content: list[Action]) -> int:
        cubes: list[State] = []
        for action, (xs, ys, zs) in parsed_content:
            if min(xs) > 50 or max(xs) < -50 or min(ys) > 50 or max(ys) < -50 or min(zs) > 50 or max(zs) < -50:
                continue
            self.apply((action, ((max(xs[0], -50), min(xs[1], 50)), (max(ys[0], -50), min(ys[1], 50)), (max(zs[0], -50), min(zs[1], 50)))), cubes)
        return self.count_on(cubes)

    def part2(self, parsed_content) -> int:
        cubes = []
        for action in parsed_content:
            self.apply(action, cubes)
        return self.count_on(cubes)


if __name__ == '__main__':
    input_content = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682"""
    input_content = None
    d = Day22(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
