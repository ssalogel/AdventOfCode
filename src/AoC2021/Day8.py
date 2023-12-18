from src.AdventUtils.Day import Day


class Day8(Day):
    def __init__(self, content=None):
        super().__init__(day=8, year=2021, content=content)

    def parse_content(self, content: str):
        lines = [line.split(" | ") for line in content.strip().split("\n")]
        return [(a[0].split(" "), a[1].split(" ")) for a in lines]

    def part1(self, parsed_content) -> int:
        count = 0
        for _, res in parsed_content:
            for digit in res:
                if (
                    len(digit) == 2
                    or len(digit) == 3
                    or len(digit) == 4
                    or len(digit) == 7
                ):
                    count += 1
        return count

    @staticmethod
    def decode_segments(setup: list[str], digits: list[str]) -> list[int]:
        setup.sort(key=len)
        numbers = {8: {"a", "b", "c", "d", "e", "f", "g"}}
        if len(setup[0]) == 2:
            numbers[1] = set(setup[0])
        else:
            raise Exception
        if len(setup[1]) == 3:
            numbers[7] = set(setup[1])
        else:
            raise Exception
        if len(setup[2]) == 4:
            numbers[4] = set(setup[2])
            new_letters = numbers[4] - numbers[1]
            assert len(new_letters) == 2
        else:
            raise Exception

        res = []
        for num in digits:
            number = set(num)
            common_with_one = number.intersection(numbers[1])
            common_with_four = number.intersection(numbers[4])
            match (
                len(number),
                len(common_with_one),
                len(common_with_four),
            ):  # noqa E211
                case 2, _, _:
                    res.append(1)
                case 3, _, _:
                    res.append(7)
                case 4, _, _:
                    res.append(4)
                case 7, _, _:
                    res.append(8)
                case 5, 2, _:
                    res.append(3)
                case 5, _, 2:
                    res.append(2)
                case 5, _, 3:
                    res.append(5)
                case 6, 1, _:
                    res.append(6)
                case 6, _, 4:
                    res.append(9)
                case 6, _, _:
                    res.append(0)
        return res

    def part2(self, parsed_content) -> int:
        return sum(
            int("".join(map(str, self.decode_segments(line, res))))
            for line, res in parsed_content
        )


if __name__ == "__main__":
    content = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""
    d = Day8(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))
