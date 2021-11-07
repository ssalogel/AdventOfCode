from AdventUtils.Day import Day


class Day15(Day):
    def __init__(self, content=None):
        super().__init__(day=15, year=2015, content=content)

    def parse_content(self) -> list[tuple[str, int, int, int, int, int]]:
        data = self.content.strip().replace(',', '').split('\n')
        return [(d[0], int(d[2]), int(d[4]), int(d[6]), int(d[8]), int(d[-1])) for d in [d.split(' ') for d in data]]

    def calc_ingredients(self, ingredients: dict[str, tuple[int, int, int, int, int]], amounts: list[tuple[str, int]]):
        tot_ingredients = [tuple(map(lambda x: x*amount, ingredients[ingr])) for ingr, amount in amounts]
        return tuple(map(sum, zip(*tot_ingredients)))

    def part1(self):
        ing_dic = {d[0]: (d[1], d[2], d[3], d[4], d[5]) for d in self.data_p1}
        ing_list = list(ing_dic.keys())
        best = 0
        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - i - j):
                    cap, dur, fla, tex, _ = self.calc_ingredients(ing_dic,  [(ing_list[0], i), (ing_list[1], j),
                                                                             (ing_list[2], k), (ing_list[3], 100-(i + j + k))])
                    if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0:
                        continue
                    if cap * dur * fla * tex > best:
                        best = cap * dur * fla * tex
        return best

    def part2(self):
        ing_dic = {d[0]: (d[1], d[2], d[3], d[4], d[5]) for d in self.data_p1}
        ing_list = list(ing_dic.keys())
        best = 0
        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - i - j):
                    cap, dur, fla, tex, cal = self.calc_ingredients(ing_dic,  [(ing_list[0], i), (ing_list[1], j),
                                                                               (ing_list[2], k), (ing_list[3], 100-(i + j + k))])
                    if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0 or cal != 500:
                        continue
                    if cap * dur * fla * tex > best:
                        best = cap * dur * fla * tex
        return best
