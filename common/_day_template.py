from common.aocdays import AOCDay, day

DEBUG = True

@day(0)
class DayTemplate(AOCDay):
    test_input = """""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 1, f'{p1} != 1'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2, f'{p2} != 2'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        yield 1

    def part2(self, input_data):
        yield 2
