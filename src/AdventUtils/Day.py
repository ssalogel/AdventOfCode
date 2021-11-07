from abc import ABC, abstractmethod
from time import time
import os
import requests
from typing import Optional


class Day(ABC):
    def __init__(self, day: int, year: int, content: Optional[str] = None):
        self.day = day
        self.year = year
        if content:
            self.content = content
        else:
            cookie = os.environ.get("COOKIE", "test")
            if not os.path.exists(f"data/{year}day{day}.txt"):
                r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": cookie})
                with open(f'data/{year}day{day}.txt', 'wb') as f:
                    f.write(r.content)
            self.content = open(f'data/{year}day{day}.txt').read().strip()
        self.data_p1 = self.parse_content()
        self.data_p2 = self.parse_content()
        self.res = None

    @abstractmethod
    def parse_content(self):
        pass

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

    def run(self):
        print(f'starting day {self.day} of {self.year}\n')
        t0 = time()
        self.res = self.part1()
        t1 = time()
        print(f"Part1 : {t1 - t0:.3} seconds\n{self.res}\n")
        res = self.part2()
        t2 = time()
        print(f"Part2 : {t2 - t1:.3} seconds\n{res}\n")
