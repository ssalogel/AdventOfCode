from src.AdventUtils.Day import Day


class Day10(Day):
    def __init__(self, content=None):
        super().__init__(day=10, year=2021, content=content)

    def parse_content(self, content: str):
        return content.strip().split("\n")

    def part1(self, parsed_content) -> int:
        syntax_error_score = 0
        scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
        for line in parsed_content:
            stack = []
            for char in line:
                if char in "{[(<":
                    stack.append(char)
                elif char in "}])>":
                    corresponding = stack.pop()
                    if char == ")" and corresponding == "(":
                        continue
                    elif ord(char) == ord(corresponding) + 2:
                        continue
                    else:
                        syntax_error_score += scores[char]
                        break
                else:
                    raise Exception
        return syntax_error_score

    def part2(self, parsed_content) -> int:
        auto_complete_scores = []
        scores = {"(": 1, "[": 2, "{": 3, "<": 4}
        for line in parsed_content:
            stack = []
            for char in line:
                if char in "{[(<":
                    stack.append(char)
                elif char in "}])>":
                    corresponding = stack.pop()
                    if char == ")" and corresponding == "(":
                        continue
                    elif ord(char) == ord(corresponding) + 2:
                        continue
                    else:
                        break
                else:
                    raise Exception
            else:
                score = 0
                for char in reversed(stack):
                    score *= 5
                    score += scores[char]
                auto_complete_scores.append(score)
        auto_complete_scores.sort()
        return auto_complete_scores[len(auto_complete_scores) // 2]


if __name__ == "__main__":
    content = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
    d = Day10(content=content)
    print(d.part1(parsed_content=d.parse_content(content=content)))
    print(d.part2(parsed_content=d.parse_content(content=content)))
