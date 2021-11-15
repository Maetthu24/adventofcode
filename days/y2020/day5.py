from common.aocdays import AOCDay, day

DEBUG = True

@day(5)
class Day5(AOCDay):
    test_input = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL""".split("\n")

    def test(self, input_data):
        p1 = self.get_seat_ids(self.test_input)
        assert max(p1) == 820, f'{max(p1)} != 820'

    def common(self, input_data):
        pass

    def part1(self, input_data):
        yield max(self.get_seat_ids(input_data))

    def part2(self, input_data):
        seat_ids = self.get_seat_ids(input_data)
        
        for id in seat_ids:
            if (id + 1) not in seat_ids and (id + 2) in seat_ids:
                yield (id + 1)
                return

    def get_seat_ids(self, input_data):
        return [int(line.translate(str.maketrans('FBLR', '0101')), 2) for line in input_data]

