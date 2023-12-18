from collections import Counter
from enum import Enum
from functools import total_ordering
from src.AdventUtils.Day import Day


@total_ordering
class Combo(Enum):
    HIGH = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        raise NotImplementedError


@total_ordering
class p1Hand:
    def __init__(self, cards: str, bid: int):
        self.bid = bid
        self.cards = cards
        self.combo = self.find_combo()
        self.values = '23456789TJQKA'

    def find_combo(self) -> Combo:
        ctr = Counter(self.cards)
        cmn = ctr.most_common()
        res = Combo.HIGH
        if cmn[0][1] == 5:
            res = Combo.FIVE_KIND
        elif cmn[0][1] == 4:
            res = Combo.FOUR_KIND
        elif cmn[0][1] == 3 and cmn[1][1] == 2:
            res = Combo.FULL_HOUSE
        elif cmn[0][1] == 3:
            res = Combo.THREE_KIND
        elif cmn[1][1] == 2:
            res = Combo.TWO_PAIR
        elif cmn[0][1] == 2:
            res = Combo.ONE_PAIR
        return res

    def __eq__(self, other):
        if isinstance(other, p1Hand):
            return self.cards == other.cards
        raise NotImplementedError

    def __lt__(self, other):
        if not isinstance(other, p1Hand):
            raise NotImplementedError
        if self.combo != other.combo:
            return self.combo < other.combo
        else:
            for x,y in zip(self.cards, other.cards):
                if x == y:
                    continue
                return self.values.find(x) < self.values.find(y)

    def __repr__(self):
        return str(self.cards) + " : " + str(self.bid) + " : " + str(self.combo)


@total_ordering
class p2Hand:
    def __init__(self, cards: str, bid: int):
        self.bid = bid
        self.cards = cards
        self.combo = self.find_combo()
        self.values = 'J23456789TQKA'

    def find_combo(self) -> Combo:
        ctr = Counter(self.cards.replace('J', ''))
        cmn = ctr.most_common()
        res = Combo.HIGH
        bonus = self.cards.count('J')
        # 254359888 is too low
        if bonus == 5 or cmn[0][1] + bonus == 5:
            res = Combo.FIVE_KIND
        elif cmn[0][1] + bonus == 4:
            res = Combo.FOUR_KIND
        elif cmn[0][1] + bonus == 3 and cmn[1][1] == 2:
            res = Combo.FULL_HOUSE
        elif cmn[0][1] + bonus == 3:
            res = Combo.THREE_KIND
        elif cmn[1][1] == 2:
            res = Combo.TWO_PAIR
        elif cmn[0][1] + bonus== 2:
            res = Combo.ONE_PAIR
        return res

    def __eq__(self, other):
        if isinstance(other, p2Hand):
            return self.cards == other.cards
        raise NotImplementedError

    def __lt__(self, other):
        if not isinstance(other, p2Hand):
            raise NotImplementedError
        if self.combo != other.combo:
            return self.combo < other.combo
        else:
            for x,y in zip(self.cards, other.cards):
                if x == y:
                    continue
                return self.values.find(x) < self.values.find(y)

    def __repr__(self):
        return str(self.cards) + " : " + str(self.bid) + " : " + str(self.combo)


class Day7(Day):
    def __init__(self, content=None):
        super().__init__(day=7, year=2023, content=content)

    def parse_content(self, content: str):
        hands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in content.splitlines()]
        return hands

    def part1(self, parsed_content) -> int:
        hands = []
        for hand, bid in parsed_content:
            hands.append(p1Hand(hand, bid))
        hands.sort()
        return sum([h.bid * (i+1) for i, h in enumerate(hands)])

    def part2(self, parsed_content) -> int:
        hands = []
        for hand, bid in parsed_content:
            hands.append(p2Hand(hand, bid))
        hands.sort()
        return sum([h.bid * (i + 1) for i, h in enumerate(hands)])


if __name__ == "__main__":
    input_content = """2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41
"""
    d = Day7(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
