from common.aocdays import AOCDay, day

DEBUG = True

@day(6)
class Day6(AOCDay):
    test_input = """abc

a
b
c

ab
ac

a
a
a
a

b""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 11, f'{p1} != 11'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 6, f'{p2} != 6'

    def common(self, input_data):
        pass

    def part1(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')

        sum = 0
        for string in input_data:
            sum += len(set(string.replace('\n', '')))

        yield sum

    def part2(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')

        sum = 0
        for string in input_data:
            possible = set('abcdefghijklmnopqrstuvwxyz')
            for line in string.split('\n'):
                possible = possible.intersection(line)
            sum += len(possible)

        yield sum
