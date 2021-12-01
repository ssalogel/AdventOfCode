from AdventUtils.Day import Day


class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2016, content=content)

    def parse_content(self) -> list[list[int]]:
        lines = self.content.strip().split('\n')
        clean_lines = [line.strip().split(' ') for line in lines]
        res = []
        for line in clean_lines:
            n_l = []
            for elem in line:
                if elem:
                    n_l.append(int(elem))
            res.append(n_l)
        return res

    def part1(self) -> int:
        count = 0
        for t in self.data_p1:
            t.sort()
            count += 1 if (t[0] + t[1]) > t[2] else 0
        return count

    def part2(self) -> int:
        count = 0
        for x, y, z in zip(self.data_p2[::3], self.data_p2[1::3], self.data_p2[2::3]):
            t1, t2, t3 = [x[0], y[0], z[0]], [x[1], y[1], z[1]], [x[2], y[2], z[2]]
            for t in [t1, t2, t3]:
                t.sort()
                count += 1 if (t[0] + t[1]) > t[2] else 0
        return count
