from src.AdventUtils.Day import Day
import re


class Day2(Day):
    def __init__(self, content=None):
        super().__init__(day=2, year=2023, content=content)

    def parse_content(self, content: str):
        lines = content.splitlines()
        games = []
        for line in lines:
            line = line.split(':')[1].strip()
            games.append(line.split(';'))
        return games

    def part1(self, parsed_content) -> int:
        res = []
        blue_max = 14
        green_max = 13
        red_max = 12
        blues = re.compile("(\d+) blue")
        greens = re.compile("(\d+) green")
        reds = re.compile("(\d+) red")
        for i, game in enumerate(parsed_content):
            for subset in game:
                nb_blue = re.search(blues, subset)
                nb_green = re.search(greens, subset)
                nb_red = re.search(reds, subset)
                if nb_blue and int(nb_blue.group(1)) > blue_max:
                    break
                if nb_green and int(nb_green.group(1)) > green_max:
                    break
                if nb_red and int(nb_red.group(1)) > red_max:
                    break
            else:
                res.append(i+1)
        return sum(res)

    def part2(self, parsed_content) -> int:
        res = []
        blues = re.compile("(\d+) blue")
        greens = re.compile("(\d+) green")
        reds = re.compile("(\d+) red")
        for i, game in enumerate(parsed_content):
            blue_min = 0
            green_min = 0
            red_min = 0
            for subset in game:
                nb_blue = re.search(blues, subset)
                nb_green = re.search(greens, subset)
                nb_red = re.search(reds, subset)
                if nb_blue:
                    blue_min = max(blue_min, int(nb_blue.group(1)))
                if nb_green:
                    green_min = max(green_min, int(nb_green.group(1)))
                if nb_red:
                    red_min = max(red_min, int(nb_red.group(1)))
            res.append(blue_min*red_min*green_min)
        return sum(res)


if __name__ == "__main__":
    input_content = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
    d = Day2(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
