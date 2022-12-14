from src.AoC2022.Day1 import Day1
from src.AoC2022.Day2 import Day2
from src.AoC2022.Day3 import Day3
from src.AoC2022.Day4 import Day4
from src.AoC2022.Day5 import Day5
from src.AoC2022.Day6 import Day6
from src.AoC2022.Day7 import Day7
from src.AoC2022.Day8 import Day8
from src.AoC2022.Day9 import Day9
from src.AoC2022.Day10 import Day10
from src.AoC2022.Day11 import Day11
from src.AoC2022.Day12 import Day12
from src.AoC2022.Day13 import Day13


def get_all_days():
    return [Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13]


def get_fast_days():
    fast = get_all_days()
    #  fast.remove(Day19)
    return fast
