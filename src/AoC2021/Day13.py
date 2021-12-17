from AdventUtils.Day import Day


class Day13(Day):
    def __init__(self, content=None):
        super().__init__(day=13, year=2021, content=content)

    def parse_content(self, content: str):
        points, folds = content.strip().replace('fold along ', '').split('\n\n')
        return [(int(point.split(',')[0]), int(point.split(',')[1])) for point in points.strip().split('\n')], \
               [(fold.split('=')[0], int(fold.split('=')[1])) for fold in folds.strip().split('\n')]

    def fold(self, axis, dist, points):
        res = set()
        for point in points:
            if axis == 'x':
                if point[0] > dist:
                    res.add((point[0] - (point[0] - dist)*2, point[1]))
                else:
                    res.add(point)
            else:
                if point[1] > dist:
                    res.add((point[0], point[1] - (point[1] - dist)*2))
                else:
                    res.add(point)
        return res

    def part1(self, parsed_content) -> int:
        points = set(parsed_content[0])
        folds = parsed_content[1]
        return len(self.fold(folds[0][0], folds[0][1], points))

    def part2(self, parsed_content) -> str:
        points = set(parsed_content[0])
        for axis, dist in parsed_content[1]:
            points = self.fold(axis, dist, points)
        res = []
        for y in range(8):
            res.append([])
            for x in range(55):
                res[-1].append('X' if (x, y) in points else ' ')
        return '\n'.join([''.join(r) for r in res])
