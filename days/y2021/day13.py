from common.aocdays import AOCDay, day

DEBUG = True

@day(13)
class Day13(AOCDay):
    test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 17, f'{p1} != 17'

        # p2 = self.part2(self.test_input).__next__()
        # assert p2 == 2, f'{p2} != 2'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')
        points = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in input_data[0].split('\n')]
        
        fold_instructions = [(x.split(' ')[2].split('=')[0], int(x.split(' ')[2].split('=')[1])) for x in input_data[1].split('\n')]
        
        new_points = set()
        is_horizontal = fold_instructions[0][0] == 'y'
        fold = fold_instructions[0][1]
        for (x,y) in points:
            if (is_horizontal and y < fold) or ((not is_horizontal) and x < fold):
                new_points.add((x,y))
            elif is_horizontal:
                new_points.add((x, y - 2*(y-fold)))
            else:
                new_points.add((x - 2*(x-fold), y))

        yield len(new_points)

    def part2(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')
        points = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in input_data[0].split('\n')]
        
        fold_instructions = [(x.split(' ')[2].split('=')[0], int(x.split(' ')[2].split('=')[1])) for x in input_data[1].split('\n')]
        
        for i in range(len(fold_instructions)):
            new_points = set()
            is_horizontal = fold_instructions[i][0] == 'y'
            fold = fold_instructions[i][1]
            for (x,y) in points:
                if (is_horizontal and y < fold) or ((not is_horizontal) and x < fold):
                    new_points.add((x,y))
                elif is_horizontal:
                    new_points.add((x, y - 2*(y-fold)))
                else:
                    new_points.add((x - 2*(x-fold), y))
            points = new_points

        max_x = max(new_points, key=lambda x: x[0])[0]
        max_y = max(new_points, key=lambda y: y[1])[1]
        
        result = [['.' if (x,y) not in new_points else '#' for x in range(max_x+1)] for y in range(max_y+1)]
        for line in result:
            print(''.join(line)) # This prints AHPRPAUZ in Ascii letters

        yield 'AHPRPAUZ'
