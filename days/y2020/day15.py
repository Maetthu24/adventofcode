from common.aocdays import AOCDay, day

DEBUG = True

@day(15)
class Day15(AOCDay):
    test_input = ["0,3,6"]

    ti_2 = ["3,1,2"]

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 436, f'{p1} != 436'

        p1b = self.part1(self.ti_2).__next__()
        assert p1b == 1836, f'{p1b} != 1836'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        input_data = [int(x) for x in input_data[0].split(',')]
        yield self.n_th_spoken_number(input_data, 2020)

    def part2(self, input_data):
        input_data = [int(x) for x in input_data[0].split(',')]
        yield self.n_th_spoken_number(input_data, 30000000)

    def n_th_spoken_number(self, input_data, n):
        last_spoken = {}
        newest_number = None

        i = 0

        for x in input_data:
            if newest_number is not None:
                last_spoken[newest_number] = i - 1
            i += 1
            newest_number = x
        
        while True:
            if newest_number in last_spoken:
                new = i - 1 - last_spoken[newest_number]
            else:
                new = 0
            
            last_spoken[newest_number] = i - 1
            newest_number = new

            i += 1

            if i == n:
                return newest_number
