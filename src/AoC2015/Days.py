from AoC2015.Day1 import Day1
from AoC2015.Day2 import Day2
from AoC2015.Day3 import Day3
from AoC2015.Day4 import Day4
from AoC2015.Day5 import Day5
from AoC2015.Day6 import Day6
from AoC2015.Day7 import Day7
from AoC2015.Day8 import Day8
from AoC2015.Day9 import Day9
from AoC2015.Day10 import Day10


def get_all_days():
    return [Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10]


def get_fast_days():
    fast = get_all_days()
    fast.remove(Day4)
    fast.remove(Day6)
    fast.remove(Day10)
    return fast
