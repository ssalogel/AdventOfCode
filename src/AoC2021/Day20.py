from src.AdventUtils.Day import Day
from src.AdventUtils.Grid2D import get_neighbours_dig_with_self_unbound


class Day20(Day):
    def __init__(self, content=None):
        super().__init__(day=20, year=2021, content=content)

    def parse_content(self, content: str):
        content = content.replace('.', '0').replace('#', '1')
        alg = content[:content.index('\n\n')]
        picture = [[c for c in row] for row in content[content.index('\n\n')+1:].strip().split('\n')]
        return alg, picture

    def pad_picture(self, picture: list[list[str]], value: str) -> list[str]:
        padded_picture = [[value] * (len(picture) + 2)]
        for row in picture:
            padded_picture.append([value] + row + [value])
        padded_picture.append([value] * (len(picture) + 2))
        return padded_picture

    def enhance(self, picture, alg, cycle) -> int:
        defaults = ('0', alg[0])
        for step in range(cycle):
            picture = self.pad_picture(picture, defaults[step % 2])
            width = height = len(picture)
            new_picture = [['' for _ in range(width)] for _ in range(height)]
            for ix, row in enumerate(picture):
                for jx, _ in enumerate(row):
                    nei = get_neighbours_dig_with_self_unbound(ix, jx)
                    index = ''.join([picture[x % width][y % height] for x, y in nei])
                    new_picture[ix][jx] = alg[int(index, 2)]
            picture = new_picture
        return sum(sum(int(v) for v in x) for x in picture)

    def part1(self, parsed_content) -> int:
        cycle = 2
        alg = parsed_content[0]
        picture = parsed_content[1]
        return self.enhance(picture, alg, cycle)

    def part2(self, parsed_content) -> int:
        cycle = 50
        alg = parsed_content[0]
        picture = parsed_content[1]
        return self.enhance(picture, alg, cycle)


if __name__ == '__main__':
    input_content = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
    input_content = None
    d = Day20(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
