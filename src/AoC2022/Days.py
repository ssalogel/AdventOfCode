from src.AoC2022.Day1 import Day1
from src.AoC2022.Day2 import Day2
from src.AoC2022.Day3 import Day3
from src.AoC2022.Day4 import Day4
from src.AoC2022.Day5 import Day5


def get_all_days():
    return [Day1, Day2, Day3, Day4, Day5]


def get_fast_days():
    fast = get_all_days()
    #  fast.remove(Day19)
    return fast
