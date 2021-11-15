from common.aocdays import AOCDay, day

DEBUG = True

@day(25)
class Day25(AOCDay):
    test_input = """5764801
17807724""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 14897079, f'{p1} != 14897079'

        # p2 = self.part2(self.test_input).__next__()
        # assert p2 == 2, f'{p2} != 2'

    def part1(self, input_data):
        card_pk = int(input_data[0])
        door_pk = int(input_data[1])

        v = 1
        sn = 7
        card_loopsize = 0
        while v != card_pk:
            card_loopsize += 1
            v = (v * sn) % 20201227
        
        v = 1
        door_loopsize = 0
        while v != door_pk:
            door_loopsize += 1
            v = (v * sn) % 20201227
        
        v = 1
        sn = door_pk
        for _ in range(card_loopsize):
            v = (v * sn) % 20201227

        yield v

    def part2(self, input_data):
        pass
