from src.AdventUtils.Day import Day


class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2020, content=content)

    def parse_content(self, content: str):
        return sorted(int(elem) for elem in content.split('\n') if elem)


    def part1(self, parsed_content) -> int:
        small = 0
        big = len(parsed_content) - 1
        while parsed_content[small] + parsed_content[big] != 2020:
            if parsed_content[small] + parsed_content[big] > 2020:
                big -= 1
            else:
                small += 1
        return parsed_content[small] * parsed_content[big]

    def part2(self, parsed_content) -> int:
        small = 0
        big = len(parsed_content) - 1
        while small < big:
            for middle in range(small+1, big):
                curr = parsed_content[small] + parsed_content[middle] + parsed_content[big]
                if curr > 2020:
                    big -= 1
                    break
                if curr == 2020:
                    return parsed_content[small] * parsed_content[middle] * parsed_content[big]
            else:
                small += 1


if __name__ == "__main__":
    input_content = """
"""
    d = Day1(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
