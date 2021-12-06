from common.aocdays import AOCDay, day

DEBUG = True

@day(6)
class Day6(AOCDay):
    test_input = """3,4,3,1,2""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 5934, f'{p1} != 5934'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 26984457539, f'{p2} != 26984457539'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        fish = {}
        for nr in input_data[0].split(','):
            nr = int(nr)
            if nr not in fish:
                fish[nr] = 1
            else:
                fish[nr] += 1

        for i in range(80):
            new = {k: 0 for k in range(9)}
            for (k,v) in fish.items():
                if k == 0:
                    new[8] += v
                    new[6] += v
                else:
                    new[k-1] += v
                fish = new

        yield sum(fish.values())

    def part2(self, input_data):
        fish = {}
        for nr in input_data[0].split(','):
            nr = int(nr)
            if nr not in fish:
                fish[nr] = 1
            else:
                fish[nr] += 1

        for i in range(256):
            new = {k: 0 for k in range(9)}
            for (k,v) in fish.items():
                if k == 0:
                    new[8] += v
                    new[6] += v
                else:
                    new[k-1] += v
                fish = new

        yield sum(fish.values())
