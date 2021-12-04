from abc import ABC, abstractmethod
from time import perf_counter
import os
import requests
from typing import Optional


class Day(ABC):
    def __init__(self, day: int, year: int, content: Optional[str] = None):
        self.day = day
        self.year = year
        if content:
            self.text = content
        else:
            cookie = os.environ.get("COOKIE", "test")
            if not os.path.exists(f"data/{year}day{day}.txt"):
                r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": cookie})
                with open(f'data/{year}day{day}.txt', 'wb') as f:
                    f.write(r.content)
            self.text = open(f'data/{year}day{day}.txt').read().strip()
        self.res = None

    @abstractmethod
    def parse_content(self, content: str):
        pass

    @abstractmethod
    def part1(self, parsed_content):
        pass

    @abstractmethod
    def part2(self, parsed_content):
        pass

    def run(self):
        print(f'starting day {self.day} of {self.year}\n')
        t0 = perf_counter()
        self.res = self.part1(self.parse_content(self.text))
        t1 = perf_counter()
        print(f"Part1 : {t1 - t0:.3} seconds\n{self.res}\n")
        res = self.part2(self.parse_content(self.text))
        t2 = perf_counter()
        print(f"Part2 : {t2 - t1:.3} seconds\n{res}\n")
