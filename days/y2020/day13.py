from common.aocdays import AOCDay, day

DEBUG = True

@day(13)
class Day13(AOCDay):
    test_input = """939
7,13,x,x,59,x,31,19""".split("\n")

    ti_1 = """
17,x,13,19""".split('\n')

    ti_2 = """
67,7,59,61""".split('\n')

    ti_3 = """
67,x,7,59,61""".split('\n')

    ti_4 = """
67,7,x,59,61""".split('\n')

    ti_5 = """
1789,37,47,1889""".split('\n')

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 295, f'{p1} != 295'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 1068781, f'{p2} != 1068781'

        p3 = self.part2(self.ti_2).__next__()
        assert p3 == 754018, f'{p3} != 754018'

        p4 = self.part2(self.ti_3).__next__()
        assert p4 == 779210, f'{p4} != 779210'

        p5 = self.part2(self.ti_4).__next__()
        assert p5 == 1261476, f'{p5} != 1261476'

        p6 = self.part2(self.ti_5).__next__()
        assert p6 == 1202161486, f'{p6} != 1202161486'

        p7 = self.part2(self.ti_1).__next__()
        assert p7 == 3417, f'{p7} != 3417'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        ts = int(input_data[0])
        bus_ids = []
        for x in input_data[1].split(','):
            if x == 'x':
                continue
            else:
                bus_ids.append(int(x))

        min_waiting_time = None
        min_id = None
        for id in bus_ids:
            time = (id * (ts // id + 1)) - ts
            if min_waiting_time == None or time < min_waiting_time:
                min_waiting_time = time
                min_id = id

        yield min_waiting_time * min_id

    def part2(self, input_data):
        line_2 = input_data[1].split(',')
        bus_ids = []
        for i in range(len(line_2)):
            x = line_2[i]
            if x == 'x':
                continue
            else:
                bus_ids.append((int(x), i))

        ts = 0
        step = 1
        for (id, offset) in bus_ids:
            max_ts = step * id
            for i in range(ts, max_ts, step):
                if (i+offset) % id == 0:
                    ts = i
                    step = max_ts
                    break
        
        yield ts
