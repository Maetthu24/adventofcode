from common.aocdays import AOCDay, day

DEBUG = True

@day(2)
class Day2(AOCDay):
    test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 150, f'{p1} != 150'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 900, f'{p2} != 900'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        h = 0
        d = 0

        for line in input_data:
            parts = line.split(' ')
            if parts[0] == 'forward':
                h += int(parts[1])
            elif parts[0] == 'up':
                d -= int(parts[1])
            elif parts[0] == 'down':
                d += int(parts[1])

        yield d * h

    def part2(self, input_data):
        h = 0
        d = 0
        a = 0

        for line in input_data:
            parts = line.split(' ')
            if parts[0] == 'forward':
                h += int(parts[1])
                d += a * int(parts[1])
            elif parts[0] == 'up':
                a -= int(parts[1])
            elif parts[0] == 'down':
                a += int(parts[1])

        yield d * h
