from common.aocdays import AOCDay, day
from itertools import permutations, product
from collections import defaultdict

DEBUG = True

@day(19)
class Day19(AOCDay):
    test_input = """--- scanner 0 ---
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
30,-46,-14""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 79, f'{p1} != 79'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2, f'{p2} != 2'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        scanners = [x.split('\n')[1:] for x in '\n'.join(input_data).split('\n\n')]
        scanners = [list(map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1]), int(x.split(',')[2])), points)) for points in scanners]

        # alignments = [(permutation, signs) for permutation in permutations(range(3)) for signs in product([-1, 1], repeat=3)]
        alignments = [
            ((0,1,2),(1,1,1)),
            ((0,1,2),(1,-1,-1)),
            ((0,1,2),(-1,1,-1)),
            ((0,1,2),(-1,-1,1)),
            ((0,2,1),(-1,-1,-1)),
            ((0,2,1),(1,-1,1)),
            ((0,2,1),(-1,1,1)),
            ((0,2,1),(1,1,-1)),
            ((1,0,2),(-1,-1,-1)),
            ((1,0,2),(1,1,-1)),
            ((1,0,2),(1,-1,1)),
            ((1,0,2),(-1,1,1)),
            ((1,2,0),(1,1,1)),
            ((1,2,0),(-1,-1,1)),
            ((1,2,0),(1,-1,-1)),
            ((1,2,0),(-1,1,-1)),
            ((2,0,1),(1,-1,-1)),
            ((2,0,1),(-1,1,-1)),
            ((2,0,1),(1,1,-1)),
            ((2,0,1),(-1,-1,1)),
            ((2,1,0),(-1,1,1)),
            ((2,1,0),(1,1,-1)),
            ((2,1,0),(1,-1,1)),
            ((2,1,0),(-1,-1,-1))
        ]

        def variants(points, idx):
            p,s = alignments[idx]
            return [(s[0]*point[p[0]],s[1]*point[p[1]],s[2]*point[p[2]]) for point in points]

        def distances(points):
            distances = []
            for i in range(len(points)-1):
                p1 = points[i]
                for j in range(i+1,len(points)):
                    p2 = points[j]
                    d = (p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2])
                    distances.append((i,j,d))
            return distances

        matched_scanners = {0: (0, (0,0,0), 0)} # alignments[7] is (0,1,2) / (1,1,1)
        to_search = [0]

        while len(matched_scanners) < len(scanners):
            print(f'There are {len(scanners)-len(matched_scanners)} unmatched scanners left.')
            while len(to_search) > 0:
                ref = to_search.pop()
                print(f'Trying with matched scanner {ref}...')
                for i in range(len(scanners)):
                    if i in matched_scanners:
                        continue
                    print(f'   ... to match with scanner {i}:')

                    v = matched_scanners[ref]

                    points_ref = scanners[ref]
                    dist_ref = set(distances(points_ref))

                    for idx in range(len(alignments)):
                        points_i = variants(scanners[i],idx)
                        dist_i = set(distances(points_i))
                        index_count = set()
                        index_pairs = set()
                        for ps1,ps2,ds in dist_ref:
                            for pi1,pi2,di in dist_i:
                                if ds == di:
                                    index_count.add(ps1)
                                    index_count.add(ps2)
                                    index_pairs.add((ps1,pi1))
                                    index_pairs.add((ps2,pi2))
                        if len(index_count) >= 12:
                            # Find a common beacon of scanners ref and i,
                            # and from the beacon's position, determine the position of scanner i
                            idx_ref, idx_i = index_pairs.pop()
                            common_beacon_ref = points_ref[idx_ref]
                            common_beacon_i = points_i[idx_i]
                            pos_i = (v[1][0]+(common_beacon_ref[0]-common_beacon_i[0]),v[1][1]+(common_beacon_ref[1]-common_beacon_i[1]),v[1][2]+(common_beacon_ref[2]-common_beacon_i[2]))
                            # pos_i = (common_beacon[0]+v[1][0], common_beacon[1]+v[1][1], common_beacon[2]+v[1][2])
                            # p,a = alignments[idx]
                            # pos_i = ((beacon[0][0]-a[0]*beacon[1][p[0]]), (beacon[0][1]-a[1]*beacon[1][p[1]]), (beacon[0][2]-a[2]*beacon[1][p[2]]))
                            # pos_i = (pos_i[0]+v[1][0], pos_i[1]+v[1][1], pos_i[2]+v[1][2])
                            print(f'      Match, scanner {i} is at {pos_i}.')
                            matched_scanners[i] = (idx, pos_i, ref)
                            to_search.append(i)

                            for idx,p in enumerate(scanners[i]):
                                scanners[i][idx] = (p[0])

                            break

            # for ref, v in matched_scanners.items():
            #     print(f'Trying to match scanner {ref}...')
            #     for i in range(len(scanners)):
            #         if i in matched_scanners or i in tried[ref]:
            #             continue
            #         print(f'   ... with scanner {i}:')

            #         # tried[ref].append(i)

            #         points_s = variants(scanners[ref],v[0])
            #         dist_s = set(distances(points_s))

            #         for idx in range(len(alignments)):
            #             points_i = variants(scanners[i],idx)
            #             dist_i = set(distances(points_i))
            #             index_count = set()
            #             points_both = set()
            #             for ps1,ps2,ds in dist_s:
            #                 for pi1,pi2,di in dist_i:
            #                     if ds == di:
            #                         index_count.add(ps1)
            #                         index_count.add(ps2)
            #                         points_both.add((points_s[ps1],scanners[i][pi1]))
            #                         points_both.add((points_s[ps2],scanners[i][pi2]))
            #             if len(index_count) >= 12:
            #                 beacon = points_both.pop()
            #                 p,a = alignments[idx]
            #                 pos_i = ((beacon[0][0]-a[0]*beacon[1][p[0]]), (beacon[0][1]-a[1]*beacon[1][p[1]]), (beacon[0][2]-a[2]*beacon[1][p[2]]))
            #                 pos_i = (pos_i[0]+v[1][0], pos_i[1]+v[1][1], pos_i[2]+v[1][2])
            #                 print(f'      Match, scanner {i} is at {pos_i}.')
            #                 found.append((i, idx, pos_i, ref))

            #                 break
            # for k, idx, pos, reference in found:
            #     matched_scanners[k] = (idx, pos, reference)

        beacons = set()
        
        for i,scanner in enumerate(scanners):
            idx, pos, _ = matched_scanners[i]
            for point in variants(scanner, idx):
                x = pos[0] + point[0]
                y = pos[1] + point[1]
                z = pos[2] + point[2]
                beacons.add((x,y,z))

        print('\n')
        for b in sorted(beacons, key=lambda x: x[0]):
            print(b)
        print('\n')

        yield len(beacons)

    def part2(self, input_data):
        yield 2
