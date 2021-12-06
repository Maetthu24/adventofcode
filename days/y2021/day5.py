from common.aocdays import AOCDay, day

DEBUG = True

@day(5)
class Day5(AOCDay):
    test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 5, f'{p1} != 5'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 12, f'{p2} != 12'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        points = {}

        for line in input_data:
            parts = line.split(' -> ')
            (x1, y1) = (int(parts[0].split(',')[0]), int(parts[0].split(',')[1]))
            (x2, y2) = (int(parts[1].split(',')[0]), int(parts[1].split(',')[1]))

            if x1 == x2:
                if y1 > y2:
                    temp = y2
                    y2 = y1
                    y1 = temp
                for y in range(y1, y2+1):
                    if (x1, y) not in points:
                        points[(x1, y)] = 1
                    else:
                        points[(x1, y)] += 1

            elif y1 == y2:
                if x1 > x2:
                    temp = x2
                    x2 = x1
                    x1 = temp
                for x in range(x1, x2+1):
                    if (x, y1) not in points:
                        points[(x, y1)] = 1
                    else:
                        points[(x, y1)] += 1
        
        yield len(list(filter(lambda x: x > 1, points.values())))


    def part2(self, input_data):
        points = {}

        for line in input_data:
            parts = line.split(' -> ')
            (x1, y1) = (int(parts[0].split(',')[0]), int(parts[0].split(',')[1]))
            (x2, y2) = (int(parts[1].split(',')[0]), int(parts[1].split(',')[1]))

            if x1 == x2:
                if y1 > y2:
                    temp = y2
                    y2 = y1
                    y1 = temp
                for y in range(y1, y2+1):
                    if (x1, y) not in points:
                        points[(x1, y)] = 1
                    else:
                        points[(x1, y)] += 1

            elif y1 == y2:
                if x1 > x2:
                    temp = x2
                    x2 = x1
                    x1 = temp
                for x in range(x1, x2+1):
                    if (x, y1) not in points:
                        points[(x, y1)] = 1
                    else:
                        points[(x, y1)] += 1
            
            else:
                if y1 > y2:
                    ystep = -1
                else:
                    ystep = 1
                if x1 > x2:
                    xstep = -1
                else:
                    xstep = 1
                
                for idx, x in enumerate(range(x1, x2+xstep, xstep)):
                    y = y1 + idx*ystep
                    if (x,y) not in points:
                        points[(x,y)] = 1
                    else:
                        points[(x,y)] += 1
        
        yield len(list(filter(lambda x: x > 1, points.values())))
