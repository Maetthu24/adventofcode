from common.aocdays import AOCDay, day

DEBUG = True

@day(3)
class Day3(AOCDay):
    test_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")

    def test(self, input_data):
        self.input_data = self.test_input

        assert list(self.part1(self.input_data)) == [7], f'{list(self.part1(self.input_data))} != [7]'
        assert list(self.part2(self.input_data)) == [336], f'{list(self.part2(self.input_data))} != [336]'

    def common(self, input_data):
        self.input_data = input_data

    def part1(self, input_data):
        forest_width = len(self.input_data[0])

        trees = 0
        pos = (0, 0)
        slope = (1, 3)

        while pos[0] + slope[0] < len(self.input_data):
            pos = (pos[0] + slope[0], (pos[1] + slope[1]) % forest_width)
            if self.input_data[pos[0]][pos[1]] == '#':
                trees += 1
        
        yield trees

    def part2(self, input_data):
        slopes = [
            (1, 1),
            (1, 3),
            (1, 5),
            (1, 7),
            (2, 1)
        ]

        result = 1
        for slope in slopes:
            result *= self.check_tree_encounters(self.input_data, slope)
        
        yield result

    def check_tree_encounters(self, input_data, slope):
        forest_width = len(input_data[0])

        trees = 0
        pos = (0, 0)

        while pos[0] + slope[0] < len(input_data):
            pos = (pos[0] + slope[0], (pos[1] + slope[1]) % forest_width)
            if input_data[pos[0]][pos[1]] == '#':
                trees += 1
        
        return trees
