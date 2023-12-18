from src.AdventUtils.Day import Day


class Day20(Day):
    def __init__(self, content=None):
        super().__init__(day=20, year=2022, content=content)

    def parse_content(self, content: str):
        return [int(i) for i in content.strip().splitlines()]

    def mix(self, nums: dict[int: int], neighbours: dict[int, list[int]]):
        amount = len(nums)

        for i in range(amount):
            move = nums[i]
            if move == 0:
                continue
            move_right = move % (amount - 1)
            prev_back_nei, prev_front_nei = neighbours[i]
            neighbours[prev_back_nei][1] = prev_front_nei
            neighbours[prev_front_nei][0] = prev_back_nei
            next_spot = prev_front_nei
            curr = i
            for _ in range(move_right):
                (_, next_spot), curr = neighbours[next_spot], next_spot
            end_spot = curr
            end_front_nei = neighbours[end_spot][1]
            neighbours[i] = [end_spot, end_front_nei]
            neighbours[end_front_nei][0] = i
            neighbours[end_spot][1] = i

        curr = 0
        end = [nums[curr]]
        for _ in range(amount - 1):
            curr = neighbours[curr][1]
            end.append(nums[curr])
        return end

    def part1_house(self, parsed_content) -> int:
        amount = len(parsed_content)
        nums = {i: v for i, v in enumerate(parsed_content)}
        neighbours = {i: [(i - 1) % amount, (i + 1) % amount] for i in range(amount)}
        end= self.mix(nums, neighbours)
        zeroth = end.index(0)
        acc = 0
        for i in range(1000, 4000, 1000):
            num = end[(zeroth + i) % len(parsed_content)]
            acc += num
        return acc

    def part2_house(self, parsed_content) -> int:
        amount = len(parsed_content)
        nums = {i: v * 811589153 for i, v in enumerate(parsed_content)}
        neighbours = {i: [(i - 1) % amount, (i + 1) % amount] for i in range(amount)}
        for _ in range(10):
            to_mix = self.mix(nums, neighbours)
        zeroth = to_mix.index(0)
        acc = 0
        for i in range(1000, 4000, 1000):
            num = to_mix[(zeroth + i) % len(parsed_content)]
            acc += num
        return acc

    def easy_mix(self, nums: list[int], n: int=1) -> list[int]:
        mod = len(nums) - 1
        worker = [i for i in range(len(nums))]
        for _ in range(n):
            for ix, v in enumerate(nums):
                if v == 0:
                    continue
                origin = worker.index(ix)
                elem = worker.pop(origin)
                new_ix = (origin + v) % mod
                worker.insert(new_ix, elem)
        return [nums[i] for i in worker]

    def part1(self, parsed_content):
        l = len(parsed_content)
        end = self.easy_mix(parsed_content)
        return sum(end[i] for i in [(end.index(0)+m)%l for m in [1000, 2000, 3000]])

    def part2(self, parsed_content):
        l = len(parsed_content)
        end = self.easy_mix([v * 811589153 for v in parsed_content], 10)
        return sum(end[i] for i in [(end.index(0)+m)%l for m in [1000, 2000, 3000]])


if __name__ == "__main__":
    input_content = """

1
2
-3
3
-2
0
4

"""
    d = Day20(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
