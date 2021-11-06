from AdventUtils.Day import Day


class Day5(Day):
    def __init__(self, content=None):
        super().__init__(day=5, year=2015, content=content)

    def parse_content(self) -> list[str]:
        return list(self.content.split('\n'))

    @classmethod
    def has_at_least_three_vowels(cls, string: str) -> bool:
        vowels = string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')
        return vowels >= 3

    @classmethod
    def has_at_least_one_double_letter(cls, string: str) -> bool:
        for i, c in enumerate(string[:-1]):
            if c == string[i+1]:
                return True
        return False

    @classmethod
    def does_not_contain_forbidden_strings(cls, string: str) -> bool:
        for no in ['ab', 'cd', 'pq', 'xy']:
            if no in string:
                return False
        return True

    def part1(self) -> int:
        vowels = set(filter(self.has_at_least_three_vowels, self.data_p1))
        doubles = set(filter(self.has_at_least_one_double_letter, self.data_p1))
        allowed = set(filter(lambda x: self.does_not_contain_forbidden_strings(x), self.data_p1))
        return len(vowels.intersection(doubles).intersection(allowed))

    @classmethod
    def has_repeating_pair_no_overlap(cls, string: str) -> bool:
        string = ''.join(string)
        for i, c in enumerate(string[:-2]):
            if c + string[i+1] in string[i+2:]:
                return True
        return False

    @classmethod
    def repeat_letter_with_one_between(cls, string: str) -> bool:
        for i, c in enumerate(string[:-2]):
            if c == string[i+2]:
                return True
        return False

    def part2(self) -> int:
        two_pairs = set(filter(self.has_repeating_pair_no_overlap, self.data_p2))
        repeat = set(filter(self.repeat_letter_with_one_between, self.data_p2))
        return len(two_pairs.intersection(repeat))
