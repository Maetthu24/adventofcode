from common.aocdays import AOCDay, day

DEBUG = True

@day(1)
class Day1(AOCDay):
    test_input = """1721
979
366
299
675
1456""".split("\n")

    def test(self, input_data):
        self.input_data = list(map(int, self.test_input))
        assert list(self.part1(self.input_data)) == [514579], f'{list(self.part1(self.input_data))} != [514579]'
        assert list(self.part2(self.input_data)) == [241861950], f'{list(self.part2(self.input_data))} != [241861950]'

    def common(self, input_data):
        self.input_data = list(map(int, input_data))

    def part1(self, input_data):
        for x in range(len(self.input_data)):
            for y in range(x + 1, len(self.input_data)):
                if self.input_data[x] + self.input_data[y] == 2020:
                    yield self.input_data[x] * self.input_data[y]
                    return

    def part2(self, input_data):
        for x in range(len(self.input_data)):
            for y in range(x + 1, len(self.input_data)):
                for z in range(y + 1, len(self.input_data)):
                    if self.input_data[x] + self.input_data[y] + self.input_data[z] == 2020:
                        yield self.input_data[x] * self.input_data[y] * self.input_data[z]
                        return
