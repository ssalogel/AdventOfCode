from src.AoC2015.Day1 import Day1
from src.AoC2015.Day2 import Day2
from src.AoC2015.Day3 import Day3
from src.AoC2015.Day4 import Day4
from src.AoC2015.Day5 import Day5
from src.AoC2015.Day6 import Day6
from src.AoC2015.Day7 import Day7
from src.AoC2015.Day8 import Day8
from src.AoC2015.Day9 import Day9
from src.AoC2015.Day10 import Day10
from src.AoC2015.Day11 import Day11
from src.AoC2015.Day12 import Day12
from src.AoC2015.Day13 import Day13
from src.AoC2015.Day14 import Day14
from src.AoC2015.Day15 import Day15
from src.AoC2015.Day16 import Day16
from src.AoC2015.Day17 import Day17
from src.AoC2015.Day18 import Day18
from src.AoC2015.Day19 import Day19
from src.AoC2015.Day20 import Day20
from src.AoC2015.Day21 import Day21
from src.AoC2015.Day22 import Day22
from src.AoC2015.Day23 import Day23
from src.AoC2015.Day24 import Day24
from src.AoC2015.Day25 import Day25


def get_all_days():
    return [Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13,
            Day14, Day15, Day16, Day17, Day18, Day19, Day20, Day21, Day22, Day23, Day24, Day25]


def get_fast_days():
    fast = get_all_days()
    fast.remove(Day4)
    fast.remove(Day6)
    fast.remove(Day10)
    fast.remove(Day20)
    fast.remove(Day22)
    return fast
