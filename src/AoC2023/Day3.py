from src.AdventUtils.Day import Day
import re

class Day3(Day):
    def __init__(self, content=None):
        super().__init__(day=3, year=2023, content=content)

    def parse_content(self, content: str):
        return content

    def get_neigh(self, beg, end, row_len, nb_row) -> list[int]:
        neigh = set()
        tot_end = row_len * nb_row
        cur_row, r = divmod(beg, row_len)
        neigh.update([x for x in range(beg-1-row_len, end+1-row_len) if x//row_len == cur_row - 1])
        if r != 0:
            neigh.add(beg-1)
        if r < row_len - 1:
            neigh.add(end)
        neigh.update([x for x in range(beg-1+row_len, end+row_len+1) if x//row_len == cur_row + 1])
        return [x for x in neigh if 0 <= x < tot_end]

    def part1(self, parsed_content) -> int:
        res = []
        row_len = parsed_content.find('\n') + 1
        nb_row = parsed_content.count('\n')
        grid = parsed_content
        numbers = re.finditer("(\d+)", grid)
        for matches in numbers:
            beg, end = matches.span()
            neighs = self.get_neigh(beg, end, row_len, nb_row)
            if any(filter(lambda x: grid[x] != '.' and grid[x] != '\n', neighs)):
                res.append(int(matches.group(0)))
        return sum(res)

    def part2(self, parsed_content) -> int:
        res = []
        row_len = parsed_content.find('\n') + 1
        nb_row = parsed_content.count('\n')
        grid = parsed_content
        gears = {i: [] for i,x in enumerate(grid) if x == '*'}
        numbers = re.finditer("(\d+)", grid)
        for matches in numbers:
            beg, end = matches.span()
            for neigh in self.get_neigh(beg, end, row_len, nb_row):
                if neigh in gears:
                    gears[neigh].append(int(matches.groups()[0]))
        for gear, nbs in gears.items():
            if len(nbs) == 2:
                res.append(nbs[0]*nbs[1])
        return sum(res)

#996543 too high
if __name__ == "__main__":
    input_content = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    d = Day3(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
