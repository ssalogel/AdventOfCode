from src.AdventUtils.Day import Day
import re

class Day5(Day):
    def __init__(self, content=None):
        super().__init__(day=5, year=2023, content=content)

    def parse_content(self, content: str):
        groups = content.split("\n\n")
        res = []
        res.append(list(map(int, re.findall(r"(\d+)", groups[0]))))
        s2s = []
        for group in groups[1:]:
            subres = []
            for line in group.splitlines()[1:]:
                subres.append(list(map(int, re.findall(r"(\d+)", line))))
            res.append(subres)
        return res

    def part1(self, parsed_content) -> int:
        seeds = [[x] for x in parsed_content[0]]
        maps = parsed_content[1:]
        for map in maps:
            spans = []
            for rang in map:
                spans.append((rang[1], rang[1]+rang[2], rang[0]-rang[1]))
            spans = sorted(spans, key=lambda x: x[0])
            for i, seed in enumerate(seeds):
                cur_v = seed[-1]
                for start, end, chng in spans:
                    if cur_v < start:
                        seeds[i].append(cur_v)
                        break
                    if start <= cur_v < end:
                        seeds[i].append(cur_v+chng)
                        break
                else:
                    seeds[i].append(cur_v)
        return min([x[-1] for x in seeds])

    def part2(self, parsed_content) -> int:
        seeds = sorted([(x, x + d_x) for x, d_x in zip(parsed_content[0][::2], parsed_content[0][1::2])])
        res = []
        maps = parsed_content[1:]
        for map in maps:
            spans = []
            for rang in map:
                spans.append((rang[1], rang[1] + rang[2], rang[0] - rang[1]))
            spans = sorted(spans, key=lambda x: x[0])
            tmp = []
            res.append(seeds)
            for i, (seed_start, seed_end) in enumerate(seeds):
                for start, end, chng in spans:
                    if seed_start < start:
                        if seed_end < start:
                            tmp.append((seed_start, seed_end))
                            break
                        else:
                            tmp.append((seed_start, start-1))
                            seed_start = start
                    if start <= seed_start < end:
                        if seed_end < end:
                            tmp.append((seed_start+chng, seed_end+chng))
                            break
                        else:
                            tmp.append((seed_start+chng, end-1+chng))
                            seed_start = end
                else:
                    tmp.append((seed_start, seed_end))
            seeds = sorted(tmp)
        return seeds[0][0]


if __name__ == "__main__":
    input_content = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
    d = Day5(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
