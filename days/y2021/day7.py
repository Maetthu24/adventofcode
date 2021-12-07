from functools import reduce
from common.aocdays import AOCDay, day

DEBUG = True

@day(7)
class Day7(AOCDay):
    test_input = """16,1,2,0,4,2,7,1,2,14""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 37, f'{p1} != 37'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 168, f'{p2} != 168'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        positions = list(map(int, input_data[0].split(',')))
        positions = sorted(positions)
        
        median = positions[int(len(positions) / 2)]

        yield self.sum_distance(positions, median)

    def part2(self, input_data):
        positions = list(map(int, input_data[0].split(',')))
        positions = sorted(positions)

        guesses = []

        for i in range(min(positions), max(positions)+1):
            guesses.append(self.sum_weighted_distance(positions, i))
        
        yield min(guesses)

    def sum_distance(self, positions, from_pos):
        return reduce(lambda x, y: x + abs(y - from_pos), positions, 0)
    
    def sum_weighted_distance(self, positions, from_pos):
        return reduce(lambda x, y: x + int(abs(y - from_pos) * (abs(y - from_pos) + 1) / 2), positions, 0)
