from common.aocdays import AOCDay, day

DEBUG = True

@day(1)
class Day1(AOCDay):
    test_input = """199
200
208
210
200
207
240
269
260
263""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 7, f'{p1} != 7'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 5, f'{p2} != 5'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        input_data = [int(x) for x in input_data]
        x = input_data[0]
        count = 0
        for y in input_data[1:]:
            if y > x:
                count += 1
            x = y
        yield count

    def part2(self, input_data):
        input_data = [int(x) for x in input_data]
        x = sum(input_data[:3])
        count = 0
        for i in range(1, len(input_data)-2):
            y = sum(input_data[i:i+3])
            if y > x:
                count += 1
            x = y
        yield count
