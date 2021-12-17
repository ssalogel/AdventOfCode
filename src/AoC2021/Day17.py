from AdventUtils.Day import Day
from math import sqrt, floor
from itertools import product


class Day17(Day):
    def __init__(self, content=None):
        super().__init__(day=17, year=2021, content=content)

    def parse_content(self, content: str):
        return [list(map(int, v.split('..'))) for v in content.replace('target area: x=', '').replace('y=', '').strip().split(', ')]

    def step(self, x, y, x_speed, y_speed):
        y += y_speed
        x += x_speed
        y_speed -= 1
        if x_speed > 0:
            x_speed -= 1
        return x, y, x_speed, y_speed

    def part1(self, parsed_content) -> int:
        max_y_speed = abs(parsed_content[1][0]) - 1
        return (max_y_speed * (max_y_speed + 1)) // 2

    def part2(self, parsed_content) -> int:
        left_x = parsed_content[0][0]
        right_x = parsed_content[0][1]
        top_y = parsed_content[1][1]
        bottom_y = parsed_content[1][0]
        max_x_speed = parsed_content[0][1]
        # start_of_target = n*(n+1)/2 -> st*2 = n^2 + n -> floor(sqrt(2st)) = n
        min_x_speed = floor(sqrt(parsed_content[0][0]*2))
        max_y_speed = abs(parsed_content[1][0]) - 1
        min_y_speed = parsed_content[1][0]
        valid = 0
        for x_speed, y_speed in product(range(min_x_speed, max_x_speed + 1), range(min_y_speed, max_y_speed + 1)):
            x = y = 0
            while x <= right_x and y > bottom_y:
                x, y, x_speed, y_speed = self.step(x, y, x_speed, y_speed)
                if left_x <= x <= right_x and top_y >= y >= bottom_y:
                    valid += 1
                    break
        return valid


if __name__ == '__main__':
    content = """target area: x=195..238, y=-93..-67"""
    #content = """target area: x=20..30, y=-10..-5"""
    d = Day17(content=content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
