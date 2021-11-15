from common.aocdays import AOCDay, day
import itertools

DEBUG = True

@day(9)
class Day9(AOCDay):
    test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")

    preamble_length = 25

    def test(self, input_data):
        self.preamble_length = 5
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 127, f'{p1} != 127'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 62, f'{p2} != 62'

    def common(self, input_data):
        self.preamble_length = 25
        input_data = self.test_input

    def part1(self, input_data):
        input_data = [int(x) for x in input_data]
        for i in range(self.preamble_length, len(input_data)):
            x = input_data[i]
            valid = False
            for comb in itertools.combinations(input_data[i-self.preamble_length:i], 2):
                if comb[0] + comb[1] == x:
                    valid = True
                    break
            
            if not valid:
                yield x
                return

    def part2(self, input_data):
        input_data = [int(x) for x in input_data]
        goal = self.part1(input_data).__next__()

        numbers = []
        index = 0

        while sum(numbers) != goal:
            if sum(numbers) > goal:
                numbers = numbers[1:]
            elif sum(numbers) < goal:
                numbers.append(input_data[index])
                index += 1

        yield min(numbers) + max(numbers)
