from src.AdventUtils.Day import Day
from ast import literal_eval
from typing import Optional, Union
from math import ceil
from itertools import permutations


Elem = Union[int, 'Snailfish']


class Snailfish:
    def __init__(self, content: list, parent: Optional['Snailfish'] = None):
        left = content[0]
        right = content[1]
        self.left_end = False
        self.right_end = False
        self.parent = parent
        if self.parent is None:
            self.depth = 1
        else:
            self.depth = self.parent.depth + 1
        if isinstance(left, list):
            self.left: Elem = Snailfish(left, self)
        else:
            self.left = left
            self.left_end = True
        if isinstance(right, list):
            self.right: Elem = Snailfish(right, self)
        else:
            self.right = right
            self.right_end = True

    def __repr__(self) -> str:
        return [self.left.__repr__(), self.right.__repr__()].__repr__().replace('\'', '')

    def __add__(self, other: 'Snailfish') -> 'Snailfish':
        if self.parent is not None:
            raise Exception
        parent = Snailfish([0, 0])
        self.parent = parent
        other.parent = parent
        parent.left = self
        parent.left_end = False
        parent.right = other
        parent.right_end = False
        parent.adjust_depth()
        while parent.get_max_depth() > 4 or parent.get_max_value() > 9:
            parent.explode()
            parent.split()
        return parent

    def adjust_depth(self):
        if self.parent is None:
            self.depth = 1
        else:
            self.depth = self.parent.depth + 1
        if not self.left_end:
            self.left.adjust_depth()
        if not self.right_end:
            self.right.adjust_depth()

    def get_max_depth(self):
        maxi = self.depth
        if not self.right_end:
            maxi = max(maxi, self.right.get_max_depth())
        if not self.left_end:
            maxi = max(maxi, self.left.get_max_depth())
        return maxi

    def get_max_value(self):
        maxi = 0
        if self.right_end:
            maxi = max(maxi, self.right)
        else:
            maxi = max(maxi, self.right.get_max_value())
        if self.left_end:
            maxi = max(maxi, self.left)
        else:
            maxi = max(maxi, self.left.get_max_value())
        return maxi

    def explode(self):
        """explodes checks all children and explodes all of them"""
        if not self.left_end:
            self.left.explode()
        if not self.right_end:
            self.right.explode()
        if self.depth > 4:
            # explodes
            if not self.right_end or not self.left_end:
                raise Exception
            self.add_to_next_left(self.left)
            self.add_to_next_right(self.right)
            if self.parent.left is self:
                self.parent.left_end = True
                self.parent.left = 0
            if self.parent.right is self:
                self.parent.right_end = True
                self.parent.right = 0

    def split(self):
        """split splits the leftmost one that needs it and returns, multiple calls to split are necessary to split them all"""
        if not self.left_end:
            if not self.left.split():
                return False
        if self.left_end and self.left > 9:
            self.left_end = False
            self.left = Snailfish([self.left//2, ceil(self.left/2)], parent=self)
            return False
        if not self.right_end:
            if not self.right.split():
                return False
        if self.right_end and self.right > 9:
            self.right_end = False
            self.right = Snailfish([self.right//2, ceil(self.right/2)], parent=self)
            return False
        return True

    def add_to_next_left(self, to_add: int):
        s = self
        p = self.parent
        while p is not None and s is p.left:
            s = p
            p = p.parent
        if p is None:
            return
        if p.left_end:
            p.left += to_add
        else:
            p.left.get_right_most().right += to_add

    def add_to_next_right(self, to_add: int):
        s = self
        p = self.parent
        while p is not None and s is p.right:
            s = p
            p = p.parent
        if p is None:
            return
        if p.right_end:
            p.right += to_add
        else:
            p.right.get_left_most().left += to_add

    def get_left_most(self) -> 'Snailfish':
        c = self
        while not c.left_end:
            c = c.left
        return c

    def get_right_most(self) -> 'Snailfish':
        c = self
        while not c.right_end:
            c = c.right
        return c

    def get_magnitude(self) -> int:
        left_mag = 3 * (self.left if self.left_end else self.left.get_magnitude())
        right_mag = 2 * (self.right if self.right_end else self.right.get_magnitude())
        return left_mag + right_mag


class Day18(Day):
    def __init__(self, content=None):
        super().__init__(day=18, year=2021, content=content)

    def parse_content(self, content: str):
        return [literal_eval(c) for c in content.strip().split('\n')]

    def part1(self, parsed_content) -> int:
        num = Snailfish(parsed_content[0])
        for e in parsed_content[1:]:
            s = Snailfish(e)
            num = num + s
        return num.get_magnitude()

    def part2(self, parsed_content) -> int:
        maxi = 0
        for a, b in permutations(parsed_content, 2):
            maxi = max(maxi, (Snailfish(a) + Snailfish(b)).get_magnitude())
        return maxi


if __name__ == '__main__':
    input_content = None
    input_content = """[1,1]\n[2,2]\n[3,3]\n[4,4]"""
    input_content = """[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]"""
    input_content = """[[[[[9,8],1],2],3],4]"""
    input_content = """[[6,[5,[4,[3,2]]]],1]"""
    input_content = """[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"""
    input_content = """[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"""
    input_content = """[[[[4,3],4],4],[7,[[8,4],9]]]\n[1,1]"""
    input_content = """[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]"""
    input_content = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
    input_content = """[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"""
    input_content = None
    input_content = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    d = Day18(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
