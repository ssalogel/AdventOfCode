from src.AdventUtils.Day import Day
from functools import lru_cache
from itertools import combinations


Pos = tuple[int, int, int]

class Day19(Day):
    def __init__(self, content=None):
        super().__init__(day=19, year=2021, content=content)

    def parse_content(self, content: str) -> list[list[Pos]]:
        coords = [c.strip().split('\n') for c in content.strip().split('---')[1:] if 'scanner' not in c]
        return [[(int(s[:s.index(',')]), int(s[s.index(',')+1:s.rindex(',')]), int(s[s.rindex(',')+1:])) for s in scanner] for scanner in coords]

    def gen_all_orientation(self, start: Pos) -> list[Pos]:
        x, y, z = start
        return [(x, y, z), (x, -z, y), (x, -y, -z), (x, z, -y),
                (y, -x, z), (y, -z, -x), (y, x, -z), (y, z, x),
                (-x, -y, z), (-x, -z, -y), (-x, y, -z), (-x, z, y),
                (-y, x, z), (-y, -z, x), (-y, -x, -z), (-y, z, -x),
                (z, y, -x), (z, x, y), (z, -y, x), (z, -x, -y),
                (-z, y, x), (-z, -x, y), (-z, -y, -x), (-z, x, -y)]

    @lru_cache(8096)
    def check_fit(self, og_sc_bea: frozenset[Pos], rel_bea: frozenset[Pos]) -> tuple[int, Pos, set[Pos]]:
        orientations = [self.gen_all_orientation(b) for b in rel_bea]
        for ori in zip(*orientations):
            for ix, fixer in enumerate(ori[:-11]):
                # since, if fit, at least 12 bea will fit, skipping 11 will still guarantee we find the one orientation and pair to find all others
                for attempt in og_sc_bea:
                    new_sc_pos = (attempt[0]-fixer[0], attempt[1]-fixer[1], attempt[2]-fixer[2])
                    beacons = set()
                    for bea in ori:
                        beacons.add((new_sc_pos[0]+bea[0], new_sc_pos[1]+bea[1], new_sc_pos[2]+bea[2]))
                    inter = og_sc_bea.intersection(beacons)
                    if len(inter) >= 12:
                        return len(inter), new_sc_pos, beacons
        return -1, (0, 0, 0), set()

    def part1(self, parsed_content: list[list[Pos]]) -> int:
        scanners: dict[int, Pos] = {0: (0, 0, 0)}
        known_beacons = set(parsed_content[0])
        while len(scanners) < len(parsed_content):
            for sc, bea_list in enumerate(parsed_content):
                if sc in scanners:
                    continue
                overlap, pos, beacons = self.check_fit(frozenset(known_beacons), frozenset(bea_list))
                if overlap != -1:
                    scanners[sc] = pos
                    known_beacons = known_beacons.union(beacons)
        return len(known_beacons)

    def part2(self, parsed_content) -> int:
        scanners: dict[int, Pos] = {0: (0, 0, 0)}
        known_beacons = set(parsed_content[0])
        while len(scanners) < len(parsed_content):
            for sc, bea_list in enumerate(parsed_content):
                if sc in scanners:
                    continue
                overlap, pos, beacons = self.check_fit(frozenset(known_beacons), frozenset(bea_list))
                if overlap != -1:
                    scanners[sc] = pos
                    known_beacons = known_beacons.union(beacons)
        maxi = 0
        for a, b in combinations(scanners.values(), 2):
            maxi = max(maxi, abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]))
        return maxi


if __name__ == '__main__':
    input_content = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""
    input_content = None
    d = Day19(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
