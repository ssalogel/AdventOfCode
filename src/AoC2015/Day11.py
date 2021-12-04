from AdventUtils.Day import Day


class Day11(Day):
    def __init__(self, content=None):
        super().__init__(day=11, year=2015, content=content)

    def parse_content(self, content: str) -> str:
        return content.strip()

    @staticmethod
    def has_three_sequence(num_pass: list[int]) -> bool:
        for i, c in enumerate(num_pass[:-2]):
            if c == num_pass[i+1]-1 == num_pass[i+2]-2:
                return True
        return False

    @staticmethod
    def no_forbidden(num_pass: list[int]) -> bool:
        return ord('i') not in num_pass and ord('o') not in num_pass and ord('l') not in num_pass

    @staticmethod
    def has_double(num_pass: list[int]) -> bool:
        count = 0
        end = -1
        for i, c in enumerate(num_pass[:-1]):
            if i <= end:
                continue
            if c == num_pass[i+1]:
                if count > 0:
                    return True
                count += 1
                end = i+1
        return False

    @classmethod
    def is_valid(cls, num_pass: list[int]) -> bool:
        return cls.no_forbidden(num_pass) and cls.has_double(num_pass) and cls.has_three_sequence(num_pass)

    @staticmethod
    def next_pass(num_pass: list[int]) -> list[int]:
        ix = -1
        while True:
            num_pass[ix] += 1
            if num_pass[ix] > ord('z'):
                num_pass[ix] = ord('a')
                ix -= 1
            else:
                break
        return num_pass

    @classmethod
    def get_next_valid_pass(cls, num_pass: list[int]) -> list[int]:
        while not cls.is_valid(num_pass):
            num_pass = cls.next_pass(num_pass)
        return num_pass

    def part1(self, parsed_content: str) -> str:
        num_pass = list(map(ord, parsed_content))
        num_pass = self.get_next_valid_pass(num_pass)
        return ''.join(map(chr, num_pass))

    def part2(self, parsed_content: str) -> str:
        num_pass = list(map(ord, parsed_content))
        num_pass = self.get_next_valid_pass(num_pass)
        num_pass = self.next_pass(num_pass)
        num_pass = self.get_next_valid_pass(num_pass)
        return ''.join(map(chr, num_pass))
