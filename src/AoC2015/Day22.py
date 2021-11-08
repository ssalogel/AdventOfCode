from AdventUtils.Day import Day


class Day22(Day):
    def __init__(self, content=None):
        super().__init__(day=22, year=2015, content=content)

    def parse_content(self):
        return tuple([int(d) for d in self.content.replace('Hit Points: ', '').replace('Damage: ', '').split('\n')])

    def sim(self, boss_hp, boss_att, hp, mana, my_turn, p_t, r_t, s_t, depth, hard):
        if hard and my_turn:
            hp -= 1
        if boss_hp <= 0:
            return 0

        hp = min(hp, 50)

        if depth == 0 or hp <= 0:
            return float('inf')

        ns_t = max(0, s_t - 1)
        np_t = max(0, p_t - 1)
        nr_t = max(0, r_t - 1)

        if not my_turn:
            if p_t > 0:
                boss_hp -= 3

            armor = 0 if s_t == 0 else 7

            if r_t > 0:
                mana += 101

            if boss_hp <= 0:
                return 0
            else:
                hp -= max(1, 8 - armor)

            return self.sim(hp=hp, mana=mana, boss_hp=boss_hp, boss_att=boss_att, s_t=ns_t, p_t=np_t, r_t=nr_t,
                            my_turn=not my_turn, depth=depth - 1, hard=hard)
        else:
            if p_t > 0:
                boss_hp -= 3

            if boss_hp <= 0:
                return 0

            if r_t > 0:
                mana += 101

            mi = float('inf')

            if mana < 53:
                return float('inf')

            if mana >= 53:
                mi = min(mi, 53 + self.sim(hp=hp, mana=mana - 53, boss_hp=boss_hp - 4, boss_att=boss_att, s_t=ns_t,
                                           p_t=np_t, r_t=nr_t, my_turn=not my_turn, depth=depth - 1, hard=hard))

            if mana >= 73:
                mi = min(mi, 73 + self.sim(hp=hp + 2, mana=mana - 73, boss_hp=boss_hp - 2, boss_att=boss_att,
                                           s_t=ns_t, p_t=np_t, r_t=nr_t, my_turn=not my_turn, depth=depth - 1, hard=hard))

            if mana >= 113 and ns_t == 0:
                mi = min(mi, 113 + self.sim(hp=hp, mana=mana - 113, boss_hp=boss_hp, boss_att=boss_att, s_t=6,
                                            p_t=np_t, r_t=nr_t, my_turn=not my_turn, depth=depth - 1, hard=hard))

            if mana >= 173 and np_t == 0:
                mi = min(mi, 173 + self.sim(hp=hp, mana=mana - 173, boss_hp=boss_hp, boss_att=boss_att, s_t=ns_t,
                                            p_t=6, r_t=nr_t, my_turn=not my_turn, depth=depth - 1, hard=hard))

            if mana >= 229 and nr_t == 0:
                mi = min(mi, 229 + self.sim(hp=hp, mana=mana - 229, boss_hp=boss_hp, boss_att=boss_att, s_t=ns_t,
                                            p_t=np_t, r_t=5, my_turn=not my_turn, depth=depth - 1, hard=hard))

            return mi

    def part1(self):
        return self.sim(boss_hp=self.data_p1[0], boss_att=self.data_p1[1], hp=50, mana=500, my_turn=True,
                        p_t=0, r_t=0, s_t=0, depth=20, hard=False)

    def part2(self):
        return self.sim(boss_hp=self.data_p2[0], boss_att=self.data_p2[1], hp=50, mana=500, my_turn=True,
                        p_t=0, r_t=0, s_t=0, depth=20, hard=True)
