from collections import defaultdict
from common.aocdays import AOCDay, day

DEBUG = True

@day(20)
class Day20(AOCDay):
    test_input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".split("\n")

    image = dict()
    empty_nr = 0

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 35, f'{p1} != 35'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 3351, f'{p2} != 3351'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        mapping = {i: x for (i,x) in enumerate(input_data[0])}
        self.image = dict()
        self.empty_nr = 0
        
        for (x,line) in enumerate(input_data[2:]):
            for (y,c) in enumerate(line):
                self.image[(x,y)] = c

        all_x = list(map(lambda k: k[0], self.image.keys()))
        all_y = list(map(lambda k: k[1], self.image.keys()))
        min_x = min(all_x)
        max_x = max(all_x)
        min_y = min(all_y)
        max_y = max(all_y)

        # self.draw_image()
        
        for i in range(2):
            new_image = dict()
            all_x = list(map(lambda k: k[0], self.image.keys()))
            all_y = list(map(lambda k: k[1], self.image.keys()))
            min_x = min(all_x)
            max_x = max(all_x)
            min_y = min(all_y)
            max_y = max(all_y)

            for (x,y) in self.image:
                new_image[(x,y)] = mapping[self.neighbor_number(x,y)]
            
            for x in range(min_x-1, max_x+2):
                new_image[(x,min_y-1)] = mapping[self.neighbor_number(x,min_y-1)]
                new_image[(x,max_y+1)] = mapping[self.neighbor_number(x,max_y+1)]
            for y in range(min_y-1,max_y+2):
                new_image[(min_x-1,y)] = mapping[self.neighbor_number(min_x-1,y)]
                new_image[(max_x+1,y)] = mapping[self.neighbor_number(max_x+1,y)]
            
            self.image = new_image
            # self.draw_image()

            if mapping[0] == '#':
                self.empty_nr = 1 if self.empty_nr == 0 else 0

        yield len([x for x in self.image.values() if x == '#'])

    def part2(self, input_data):
        mapping = {i: x for (i,x) in enumerate(input_data[0])}
        self.image = dict()
        self.empty_nr = 0
        
        for (x,line) in enumerate(input_data[2:]):
            for (y,c) in enumerate(line):
                self.image[(x,y)] = c

        all_x = list(map(lambda k: k[0], self.image.keys()))
        all_y = list(map(lambda k: k[1], self.image.keys()))
        min_x = min(all_x)
        max_x = max(all_x)
        min_y = min(all_y)
        max_y = max(all_y)

        # self.draw_image()
        
        for i in range(50):
            new_image = dict()
            all_x = list(map(lambda k: k[0], self.image.keys()))
            all_y = list(map(lambda k: k[1], self.image.keys()))
            min_x = min(all_x)
            max_x = max(all_x)
            min_y = min(all_y)
            max_y = max(all_y)

            for (x,y) in self.image:
                new_image[(x,y)] = mapping[self.neighbor_number(x,y)]
            
            for x in range(min_x-1, max_x+2):
                new_image[(x,min_y-1)] = mapping[self.neighbor_number(x,min_y-1)]
                new_image[(x,max_y+1)] = mapping[self.neighbor_number(x,max_y+1)]
            for y in range(min_y-1,max_y+2):
                new_image[(min_x-1,y)] = mapping[self.neighbor_number(min_x-1,y)]
                new_image[(max_x+1,y)] = mapping[self.neighbor_number(max_x+1,y)]
            
            self.image = new_image
            # self.draw_image()

            if mapping[0] == '#':
                self.empty_nr = 1 if self.empty_nr == 0 else 0

        yield len([x for x in self.image.values() if x == '#'])
    
    def neighbor_number(self, x, y):
        nr = ''
        for x1 in range(x-1,x+2):
            for y1 in range(y-1,y+2):
                if (x1,y1) in self.image:
                    nr += '1' if self.image[(x1,y1)] == '#' else '0'
                else:
                    nr += str(self.empty_nr)
        
        return int(nr, 2)
    
    def draw_image(self):
        all_x = list(map(lambda k: k[0], self.image.keys()))
        all_y = list(map(lambda k: k[1], self.image.keys()))
        min_x = min(all_x)
        max_x = max(all_x)
        min_y = min(all_y)
        max_y = max(all_y)

        img = [['.' for _ in range(min_y-5,max_y+6)] for _ in range(min_x-5,max_x+6)]
        for (k,v) in self.image.items():
            img[k[0]+5][k[1]+5] = v
        
        print('\n')
        for line in img:
            print(''.join(line))
        print('\n')
                

