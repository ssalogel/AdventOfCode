from AdventUtils.Day import Day
from itertools import product


class Day21(Day):
    def __init__(self, content=None):
        super().__init__(day=21, year=2015, content=content)
        self.weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
        self.armor = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
        self.rings = [(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
        self.hp = 100

    def parse_content(self):
        return tuple([int(d[-1]) for d in [da.split(' ') for da in self.content.split('\n')]])

    def get_equipment_combo(self):
        combos = [tuple(map(sum, zip(*p))) for p in product(self.weapons, self.armor, self.rings, self.rings)]
        combos.sort()
        return combos

    def play(self, hp: int, att: int, defence: int, boss_hp: int, boss_att: int, boss_def: int) -> bool:
        while hp > 0 and boss_hp > 0:
            boss_hp -= max(1, att - boss_def)
            if boss_hp <= 0:
                break
            hp -= max(1, boss_att - defence)
        return hp > 0

    def part1(self):
        boss_hp, boss_att, boss_def = self.data_p1
        for gold, att, defence in self.get_equipment_combo():
            if self.play(hp=self.hp, att=att, defence=defence, boss_hp=boss_hp, boss_att=boss_att, boss_def=boss_def):
                return gold

    def part2(self):
        boss_hp, boss_att, boss_def = self.data_p1
        for gold, att, defence in reversed(self.get_equipment_combo()):
            if not self.play(hp=self.hp, att=att, defence=defence, boss_hp=boss_hp, boss_att=boss_att, boss_def=boss_def):
                return gold
