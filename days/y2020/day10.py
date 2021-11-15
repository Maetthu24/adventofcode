from common.aocdays import AOCDay, day

DEBUG = True

@day(10)
class Day10(AOCDay):
    test_input = """16
10
15
5
1
11
7
19
6
12
4""".split("\n")

    test_input_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 35, f'{p1} != 35'

        p1b = self.part1(self.test_input_2).__next__()
        assert p1b == 220, f'{p1b} != 220'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 8, f'{p2} != 8'

        p2b = self.part2(self.test_input_2).__next__()
        assert p2b == 19208, f'{p2b} != 19208'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        input_data = sorted([int(x) for x in input_data])
        input_data = [0] + input_data + [max(input_data) + 3]

        diff_1 = 0
        diff_3 = 0
        for i in range(len(input_data) - 1):
            diff = input_data[i+1] - input_data[i]
            assert diff in range(1, 4), f'Wrong adapter at index {i}'
            if diff == 1:
                diff_1 += 1
            elif diff == 3:
                diff_3 += 1
        
        yield diff_1 * diff_3

    visited = {}

    def part2(self, input_data):
        input_data = sorted([int(x) for x in input_data])
        input_data = [0] + input_data + [max(input_data) + 3]

        self.visited = {}
        yield self.paths_to_end(0, input_data)

    def paths_to_end(self, i, input_data):
        if i == len(input_data) - 1:
            return 1
        elif i in self.visited:
            return self.visited[i]
        else:
            paths = 0
            j = i+1
            while j < len(input_data) and input_data[j] - input_data[i] <= 3:
                paths += self.paths_to_end(j, input_data)
                j += 1
            self.visited[i] = paths
            return paths