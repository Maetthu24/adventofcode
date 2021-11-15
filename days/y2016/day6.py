from common.aocdays import AOCDay, day

DEBUG = True

@day(6)
class Day6(AOCDay):
    test_input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 'easter', f'{p1} != easter'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 'advent', f'{p2} != advent'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        lines = input_data

        word = ''

        for column in range(len(lines[0])):
            dict = {}
            for row in range(len(lines)):
                char = lines[row][column]
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
            
            word += max(dict, key=dict.get)

        yield word

    def part2(self, input_data):
        lines = input_data

        word = ''

        for column in range(len(lines[0])):
            dict = {}
            for row in range(len(lines)):
                char = lines[row][column]
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
            
            word += min(dict, key=dict.get)

        yield word
