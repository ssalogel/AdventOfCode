from AdventUtils.Day import Day


class Day8(Day):
    def __init__(self, content=None):
        super().__init__(day=8, year=2015, content=content)

    def parse_content(self) -> list[str]:
        return self.content.split('\n')

    @staticmethod
    def calc_num_of_coded_chars(string: str) -> int:
        return len(string)

    @staticmethod
    def calc_actual_str_len(string: str) -> int:
        return len(eval(string))

    @staticmethod
    def calc_encoded_str_len(string: str) -> int:
        return len(string) + 2 + string.count('"') + string.count('\\')

    def part1(self) -> int:
        char_code = 0
        mem_code = 0
        for line in self.data_p1:
            char_code += self.calc_num_of_coded_chars(line)
            mem_code += self.calc_actual_str_len(line)
        return char_code - mem_code

    def part2(self) -> int:
        char_code = 0
        encoded_code = 0
        for line in self.data_p2:
            char_code += self.calc_num_of_coded_chars(line)
            encoded_code += self.calc_encoded_str_len(line)

        return encoded_code - char_code
