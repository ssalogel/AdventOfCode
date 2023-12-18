from src.AdventUtils.Day import Day


Sue = tuple[str, dict[str, int]]


class Day16(Day):
    def __init__(self, content=None):
        super().__init__(day=16, year=2015, content=content)
        self.truth = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        }

    def parse_content(self, content: str) -> list[Sue]:
        data = content.strip().replace(",", "").replace(":", "").split("\n")
        return [
            (d[1], {d[2]: int(d[3]), d[4]: int(d[5]), d[6]: int(d[7])})
            for d in [d.split(" ") for d in data]
        ]

    def part1(self, parsed_content: list[Sue]) -> str:
        for aunt, info in parsed_content:
            for k, v in info.items():
                if self.truth[k] != v:
                    break
            else:
                return aunt
        raise Exception

    def part2(self, parsed_content: list[Sue]) -> str:
        res = []
        for aunt, info in parsed_content:
            for k, v in info.items():
                if k == "cats" or k == "trees":
                    if self.truth[k] >= v:
                        break
                elif k == "pomeranians" or k == "goldfish":
                    if self.truth[k] <= v:
                        break
                else:
                    if self.truth[k] != v:
                        break
            else:
                res.append(aunt)
        return res.pop()
