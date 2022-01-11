from src.AdventUtils.Day import Day


class Day25(Day):
    def __init__(self, content=None):
        super().__init__(day=25, year=2021, content=content)

    def parse_content(self, content: str):
        return [[c for c in line] for line in content.strip().split('\n')]

    def step(self, grid: list[list[str]]) -> tuple[bool, list[list[str]]]:
        height = len(grid)
        width = len(grid[0])
        down = []
        changed = False
        n_grid = [(['.']*width).copy() for _ in range(height)]
        for j in range(width):
            for i, row in enumerate(grid):
                curr = row[j]
                if curr == '.':
                    continue
                elif curr == 'v':
                    down.append((j, i))
                else:
                    if row[(j+1) % width] == '.':
                        n_grid[i][(j + 1) % width] = '>'
                        changed = True
                    else:
                        n_grid[i][j] = '>'
        down.sort()
        for j, i in down:
            if grid[(i+1) % height][j] != 'v' and n_grid[(i+1) % height][j] == '.':
                n_grid[(i + 1) % height][j] = 'v'
                changed = True
            else:
                n_grid[i][j] = 'v'
        return changed, n_grid

    def part1(self, parsed_content) -> int:
        count = 0
        grid = parsed_content
        changed = True
        while changed:
            count += 1
            changed, grid = self.step(grid)
        return count

    def part2(self, parsed_content) -> str:
        return "WINNER!"


if __name__ == '__main__':
    input_content = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
    input_content = None
    d = Day25(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
