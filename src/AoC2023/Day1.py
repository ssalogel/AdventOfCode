from src.AdventUtils.Day import Day
from sys import maxsize

class Day1(Day):
    def __init__(self, content=None):
        super().__init__(day=1, year=2023, content=content)

    def parse_content(self, content: str):
        return content.splitlines()

    def part1(self, parsed_content) -> int:
        res = 0
        for line in parsed_content:
            first = last = ""
            for char in line:
                if char.isnumeric():
                    first = char
                    break
            for char in line[::-1]:
                if char.isnumeric():
                    last = char
                    break
            res += int(first+last)
        return res

    def part2old(self, parsed_content):
        values = {
            "0": 0,
            "zero": 0,
            "1": 1,
            "one": 1,
            "2": 2,
            "two": 2,
            "3": 3,
            "three": 3,
            "4": 4,
            "four": 4,
            "5": 5,
            "five": 5,
            "6": 6,
            "six": 6,
            "7": 7,
            "seven": 7,
            "8": 8,
            "eight": 8,
            "9": 9,
            "nine": 9
        }

        res = []
        for line in parsed_content:
            last_ix = first = last = 0
            first_ix = maxsize
            for key, value in values.items():
                left = line.find(key)
                right = line.rfind(key)
                if left == -1:
                    continue
                if left < first_ix:
                    first_ix = left
                    first = value
                if right > last_ix:
                    last_ix = right
                    last = value
            res += first * 10 + last
        return res

    def part2(self, parsed_content: list[str]):
        digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        res = []
        for line in parsed_content:
            nums = []
            for i, c in enumerate(line):
                if c.isnumeric():
                    nums.append(int(c))
                    continue
                for j, digit in enumerate(digits):
                    if line[i:].startswith(digit):
                        nums.append(j)
                        break
            res.append(nums[0]*10 + nums[-1])

        return sum(res)


if __name__ == "__main__":
    input_content = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    d = Day1(content=input_content)
    #print(d.part1(parsed_content=d.parse_content(content=d.content)))
    newres = d.part2(parsed_content=d.parse_content(content=d.content))
    oldres = d.part2old(parsed_content=d.parse_content(content=d.content))
    for i, (n, o) in enumerate(zip(oldres, newres)):
        if n != o:
            print(i, o, n)