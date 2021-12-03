from common.aocdays import AOCDay, day
import numpy as np

DEBUG = True

@day(3)
class Day3(AOCDay):
    test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")

    gamma = ''
    epsilon = ''

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 198, f'{p1} != 198'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 230, f'{p2} != 230'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        input = np.array([x for x in [list(y) for y in input_data]])
        input = np.transpose(input)

        for line in input:
            ones = np.count_nonzero(line == '1')
            zeroes = np.count_nonzero(line == '0')
            if ones > zeroes:
                self.gamma += '1'
                self.epsilon += '0'
            else:
                self.gamma += '0'
                self.epsilon += '1'

        yield int(self.gamma, base=2) * int(self.epsilon, base=2)

    def part2(self, input_data):
        remaining1 = input_data
        pos = 0
        while len(remaining1) > 1:
            most_common = self.most_common(remaining1, pos)
            if most_common == '':
                most_common = '1'
            remaining1 = [x for x in remaining1 if x[pos] == most_common]
            pos += 1
        
        pos = 0
        remaining2 = input_data
        while len(remaining2) > 1:
            most_common = self.least_common(remaining2, pos)
            if most_common == '':
                most_common = '0'
            remaining2 = [x for x in remaining2 if x[pos] == most_common]
            pos += 1

        oxygen_generator_rating = remaining1[0]
        co2_scrubber_rating = remaining2[0]

        yield int(oxygen_generator_rating, base=2) * int(co2_scrubber_rating, base=2)
    
    def most_common(self, array, pos):
        ones = 0
        zeroes = 0
        for line in array:
            if line[pos] == '0':
                zeroes += 1
            else:
                ones += 1
        
        if ones == zeroes:
            return ''
        elif ones > zeroes:
            return '1'
        else:
            return '0'
        
    def least_common(self, array, pos):
        ones = 0
        zeroes = 0
        for line in array:
            if line[pos] == '0':
                zeroes += 1
            else:
                ones += 1
        
        if ones == zeroes:
            return ''
        elif ones > zeroes:
            return '0'
        else:
            return '1'
