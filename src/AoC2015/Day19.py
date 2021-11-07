from AdventUtils.Day import Day


class Day19(Day):
    def __init__(self, content=None):
        super().__init__(day=19, year=2015, content=content)

    def parse_content(self) -> tuple[list[list[str]], str]:
        rules, mol = self.content.strip().split('\n\n')
        return [d.split(' => ') for d in rules.strip().split('\n')], mol

    def part1(self):
        rules, mol = self.data_p1
        results = set()
        for src, dest in rules:
            part_mol = mol.split(src)
            for i in range(len(part_mol)-1):
                tmp_mol = part_mol[:i] + [dest.join(part_mol[i:i+2])] + part_mol[i+2:]
                results.add(src.join(tmp_mol))
        return len(results)

    def part2(self):
        """
        rules:
        X -> YZ         == 1 reduction
            from mol to e in len(mol)-1 steps
        X -> YRnLAr     == 3 reduction
            from mol to e in len(mol) - count(Rn) - count(Ar) - 1
            since VRnXAr -> X gets Rn and Ar for free.... CRnLRnMArAr -> CRnXAr -> D
                                                len(mol) = 7, count(Rn) = 2, count(Ar) 2 => 7 - 2 - 2 - 1 = 2
        X -> YRnLYLAr   == 5 reduction
            VRnLYLAr -> X each Y takes another with them for free
                len(mol) = 6, count(Rn) = 1, count(Ar) = 1, count(Y) = 1, freebie = count(Y)
                6 - 1 - 1 - 2*1 - 1 = 1
                   Rn  Ar  Y fre  ends with e
        X -> YRnLYLYLAr == 7 reduction
                same logic as above, each Y takes right next w/
                len(mol) - count(Rn) - count(Ar) - 2(count(Y)) - 1 = steps
        """
        _, mol = self.data_p2
        valid_id = {'Al', 'B', 'Ca', 'F', 'H', 'Mg', 'N', 'O', 'P', 'Si', 'Th', 'Ti', 'e', 'Rn', 'Ar', 'Y'}
        tot_atom = sum(mol.count(a) for a in valid_id)
        steps = tot_atom - mol.count('Rn') - mol.count('Ar') - (2 * mol.count('Y')) - 1
        return steps
