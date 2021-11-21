from common.aocdays import AOCDay, day

import numpy as np

DEBUG = True

@day(8)
class Day8(AOCDay):
    test_input = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1""".split("\n")

    is_test = False

    def test(self, input_data):
        self.is_test = True
        p1 = self.part1(self.test_input).__next__()
        self.is_test = False
        assert p1 == 6, f'{p1} != 6'

        self.is_test = True
        p2 = self.part2(self.test_input).__next__()
        self.is_test = False
        assert p2 == 'EFEYKFRFIJ', f'{p2} != "EFEYKFRFIJ"'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        if self.is_test:
            screen = np.full((3,7), '.')
        else:
            screen = np.full((6,50), '.')
        
        for line in input_data:
            words = line.split(' ')
            if words[0] == 'rect':
                x = int(words[1].split('x')[1])
                y = int(words[1].split('x')[0])
                screen[:x,:y] = '#'
            elif words[0] == 'rotate':
                if words[1] == 'row':
                    row = int(words[2].split('=')[1])
                    by = int(words[4])
                    screen[row,:] = np.roll(screen[row,:], by)
                else:
                    column = int(words[2].split('=')[1])
                    by = int(words[4])
                    screen[:,column] = np.roll(screen[:,column], by)

        for row in screen:
            print(''.join(row))

        yield (screen == '#').sum()

    def part2(self, input_data):
        # After manipulation, the screen prints this:

        ####.####.####.#...##..#.####.###..####..###...##.
        #....#....#....#...##.#..#....#..#.#......#.....#.
        ###..###..###...#.#.##...###..#..#.###....#.....#.
        #....#....#......#..#.#..#....###..#......#.....#.
        #....#....#......#..#.#..#....#.#..#......#..#..#.
        ####.#....####...#..#..#.#....#..#.#.....###..##..

        yield 'EFEYKFRFIJ'
