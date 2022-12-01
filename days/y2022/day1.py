from common.aocdays import AOCDay, day

DEBUG = True

@day(1)
class Day1(AOCDay):
    test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 24000, f'{p1} != 24000'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 45000, f'{p2} != 45000'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        packets = '\n'.join(input_data).split('\n\n')
        calories_sums = map(lambda x: sum([int(y) for y in x.split('\n')]), packets)
        yield max(calories_sums)

    def part2(self, input_data):
        packets = '\n'.join(input_data).split('\n\n')
        calories_sums = list(map(lambda x: sum([int(y) for y in x.split('\n')]), packets))
        calories_sums.sort(reverse=True)
        yield sum(calories_sums[:3])
