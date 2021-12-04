from AdventUtils.Day import Day
import json


# TODO better typing hints
class Day12(Day):
    def __init__(self, content=None):
        super().__init__(day=12, year=2015, content=content)

    def parse_content(self, content: str):
        return json.loads(content)

    def part1(self, parsed_content) -> int:
        iterables = [parsed_content]
        res = 0
        while len(iterables) > 0:
            iterable = iterables.pop()
            if isinstance(iterable, dict):
                for item in iterable.values():
                    if isinstance(item, str):
                        continue
                    if hasattr(item, '__iter__'):
                        iterables.append(item)
                    elif isinstance(item, int):
                        res += item
            else:
                for elem in iterable:
                    if isinstance(elem, str):
                        continue
                    if hasattr(elem, '__iter__'):
                        iterables.append(elem)
                    elif isinstance(elem, int):
                        res += elem
        return res

    def part2(self, parsed_content) -> int:
        iterables = [parsed_content]
        res = 0
        while len(iterables) > 0:
            iterable = iterables.pop()
            if isinstance(iterable, dict):
                if 'red' in iterable.values():
                    continue
                for item in iterable.values():
                    if isinstance(item, str):
                        continue
                    if hasattr(item, '__iter__'):
                        iterables.append(item)
                    elif isinstance(item, int):
                        res += item
            else:
                for elem in iterable:
                    if isinstance(elem, str):
                        continue
                    if hasattr(elem, '__iter__'):
                        iterables.append(elem)
                    elif isinstance(elem, int):
                        res += elem
        return res
