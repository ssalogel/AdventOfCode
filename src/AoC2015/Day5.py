from src.AdventUtils.Day import Day


class Day5(Day):
    def __init__(self, content=None):
        super().__init__(day=5, year=2015, content=content)

    def parse_content(self, content: str) -> list[str]:
        return content.split('\n')

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

    def part1(self, parsed_content: list[str]) -> int:
        vowels = set(filter(self.has_at_least_three_vowels, parsed_content))
        doubles = set(filter(self.has_at_least_one_double_letter, parsed_content))
        allowed = set(filter(lambda x: self.does_not_contain_forbidden_strings(x), parsed_content))
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

    def part2(self, parsed_content: list[str]) -> int:
        two_pairs = set(filter(self.has_repeating_pair_no_overlap, parsed_content))
        repeat = set(filter(self.repeat_letter_with_one_between, parsed_content))
        return len(two_pairs.intersection(repeat))
