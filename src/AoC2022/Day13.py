from src.AdventUtils.Day import Day
from ast import literal_eval


class packet:
    def __init__(self, values):
        if isinstance(values, int):
            self.values = values
        else:
            self.values = [packet(x) for x in values]

    def __repr__(self):
        return f"{self.values}"

    def __len__(self):
        if isinstance(self.values, list):
            return len(self.values)
        else:
            return -1

    def __eq__(self, other: "packet"):
        if isinstance(self.values, int):
            if isinstance(other.values, int):
                return self.values == other.values
            else:
                return packet([self.values]) == other
        else:
            if isinstance(other.values, int):
                return self == packet([other.values])
            else:
                for a, b in zip(self.values, other.values):
                    if a == b:
                        continue
                    else:
                        return False
                return len(self) == len(other)

    def __lt__(self, other: "packet"):
        if isinstance(self.values, int):
            if isinstance(other.values, int):
                return self.values < other.values
            else:
                return packet([self.values]) < other
        else:
            if isinstance(other.values, int):
                return self < packet([other.values])
            else:
                for a, x in zip(self.values, other.values):
                    if a == x:
                        continue
                    if a < x:
                        return True
                    if a > x:
                        return False
                return len(self) < len(other)


class Day13(Day):
    def __init__(self, content=None):
        super().__init__(day=13, year=2022, content=content)

    def parse_content(self, content: str):
        res = []
        for pairs in content.strip().split("\n\n"):
            left, right = pairs.split("\n")
            res.append((literal_eval(left), literal_eval(right)))
        return res

    def part1(self, parsed_content) -> int:
        acc = 0
        for ix, (left, right) in enumerate(parsed_content):
            if packet(left) < packet(right):
                acc += ix + 1
        return acc

    def part2(self, parsed_content) -> int:
        dividers = [([[2]], [[6]])]
        sorted_packets = sorted(
            [
                item
                for sublist in [
                    [packet(left), packet(right)]
                    for left, right in parsed_content + dividers
                ]
                for item in sublist
            ]
        )
        ix1 = sorted_packets.index(packet(dividers[0][0])) + 1
        ix2 = sorted_packets.index(packet(dividers[0][1])) + 1
        return ix1 * ix2


if __name__ == "__main__":
    input_content = """

[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]

"""
    d = Day13(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
