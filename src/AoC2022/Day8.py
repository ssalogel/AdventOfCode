from typing import Iterable

from src.AdventUtils.Day import Day


class Day8(Day):
    def __init__(self, content=None):
        super().__init__(day=8, year=2022, content=content)

    def parse_content(self, content: str):
        return [list(map(int, x)) for x in content.strip().splitlines()]

    def part1(self, parsed_content) -> int:
        field = parsed_content
        top_edge = left_edge = 0
        right_edge = len(field[0]) - 1
        bottom_edge = len(field) - 1
        acc = 0
        for i, row in enumerate(field):
            if i in (top_edge, bottom_edge):
                acc += len(row)
                continue
            for j, tree in enumerate(row):
                if j in (left_edge, right_edge):
                    acc += 1
                    continue
                if max(row[0:j]) < tree or max(row[j + 1:]) < tree:
                    acc += 1
                    continue
                if max([c[j] for c in field[0:i]]) < tree or max([c[j] for c in field[i + 1:]]) < tree:
                    acc += 1
        return acc

    def get_view_distance(self, tree: int, view: Iterable[int]):
        score = 0
        for spot in view:
            score += 1
            if spot >= tree:
                break
        return score

    def part2(self, parsed_content) -> int:
        field = parsed_content
        top_edge = left_edge = 0
        right_edge = len(field[0]) - 1
        bottom_edge = len(field) - 1
        max_score = 0
        for i, row in enumerate(field):
            if i in (top_edge, bottom_edge):
                continue
            for j, tree in enumerate(row):
                if j in (left_edge, right_edge):
                    continue

                scenic_score = (self.get_view_distance(tree, (line[j] for line in reversed(field[0:i])))
                                * self.get_view_distance(tree, reversed(row[0:j]))
                                * self.get_view_distance(tree, row[j + 1:])
                                * self.get_view_distance(tree, (line[j] for line in field[i + 1:])))
                max_score = max(max_score, scenic_score)
        return max_score


if __name__ == '__main__':
    input_content = """30373
25512
65332
33549
35390

"""
    d = Day8(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
