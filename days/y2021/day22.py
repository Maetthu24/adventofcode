from common.aocdays import AOCDay, day
from collections import defaultdict

DEBUG = True

@day(22)
class Day22(AOCDay):
    test_input = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 590784, f'{p1} != 590784'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2758514936282235, f'{p2} != 2758514936282235'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        steps = []
        for line in input_data:
            split = line.split(' ')
            nrs = split[1].split(',')
            x = nrs[0].lstrip('x=').split('..')
            x1 = int(x[0])
            x2 = int(x[1])
            y = nrs[1].lstrip('y=').split('..')
            y1 = int(y[0])
            y2 = int(y[1])
            z = nrs[2].lstrip('z=').split('..')
            z1 = int(z[0])
            z2 = int(z[1])
            steps.append((split[0] == 'on', (x1,x2), (y1,y2), (z1,z2)))

        cubes = defaultdict(lambda _: False)

        for (on, xc, yc, zc) in steps:
            if xc[0] not in range(-50,51) or xc[1] not in range(-50,51) or yc[0] not in range(-50,51) or yc[1] not in range(-50,51) or zc[0] not in range(-50,51) or zc[1] not in range(-50,51):
                break

            for x in range(xc[0],xc[1]+1):
                for y in range(yc[0],yc[1]+1):
                    for z in range(zc[0],zc[1]+1):
                        cubes[(x,y,z)] = on

        yield len([x for x in cubes.values() if x])

    def part2(self, input_data):
        steps = []
        for line in input_data:
            split = line.split(' ')
            nrs = split[1].split(',')
            x = nrs[0].lstrip('x=').split('..')
            x1 = int(x[0])
            x2 = int(x[1])
            y = nrs[1].lstrip('y=').split('..')
            y1 = int(y[0])
            y2 = int(y[1])
            z = nrs[2].lstrip('z=').split('..')
            z1 = int(z[0])
            z2 = int(z[1])
            steps.append((split[0] == 'on', (x1,x2), (y1,y2), (z1,z2)))

        cubes = defaultdict(lambda _: False)

        for (on, xc, yc, zc) in steps:
            for x in range(xc[0],xc[1]+1):
                for y in range(yc[0],yc[1]+1):
                    for z in range(zc[0],zc[1]+1):
                        cubes[(x,y,z)] = on

        yield len([x for x in cubes.values() if x])
