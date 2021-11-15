from common.aocdays import AOCDay, day
from collections import Counter

DEBUG = True

@day(2)
class Day2(AOCDay):
    test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split("\n")

    def test(self, input_data):
        # Parse input
        self.input_data = []
        for line in self.test_input:
            parts = line.split(' ')
            lower = int(parts[0].split('-')[0])
            upper = int(parts[0].split('-')[1])
            letter = parts[1][0]
            self.input_data.append((lower, upper, letter, parts[2]))
        
        assert list(self.part1(self.input_data)) == [2], f'{list(self.part1(self.input_data))} != [2]'
        assert list(self.part2(self.input_data)) == [1], f'{list(self.part2(self.input_data))} != [1]'

    def common(self, input_data):
        # Parse input
        self.input_data = []
        for line in input_data:
            parts = line.split(' ')
            lower = int(parts[0].split('-')[0])
            upper = int(parts[0].split('-')[1])
            
            letter = parts[1][0]
            self.input_data.append((lower, upper, letter, parts[2]))

    def part1(self, input_data):
        c = 0
        for (lower, upper, l, w) in self.input_data:
            valid_range = range(lower, upper + 1)
            if Counter(w)[l] in valid_range:
                c += 1
        
        yield c

    def part2(self, input_data):
        c = 0
        for (lower, upper, l, w) in self.input_data:
            string = w[lower - 1] + w[upper - 1]
            if Counter(string)[l] == 1:
                c += 1
        
        yield c
