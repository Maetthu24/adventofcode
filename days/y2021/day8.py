from common.aocdays import AOCDay, day

DEBUG = True

@day(8)
class Day8(AOCDay):
    test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 26, f'{p1} != 26'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 61229, f'{p2} != 61229'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        digits = [[x for x in y.split(' | ')[1].split(' ')] for y in input_data]

        sum = 0
        for line in digits:
            for d in line:
                if len(d) in [2,3,4,7]:
                    sum += 1
        
        yield sum

    def part2(self, input_data):
        sum = 0
        for line in input_data:
            sum += self.solve_line(line)
        yield sum
    
    def solve_line(self, line):
        pattern = [x for x in line.split(' | ')[0].split(' ')]
        digits = [x for x in line.split(' | ')[1].split(' ')]

        mapping = {k: ['a', 'b', 'c', 'd', 'e', 'f', 'g'] for k in range(7)}
        
        one = set(next(filter(lambda x: len(x) == 2, pattern)))
        seven = set(next(filter(lambda x: len(x) == 3, pattern)))
        four = set(next(filter(lambda x: len(x) == 4, pattern)))
        eight = set(next(filter(lambda x: len(x) == 7, pattern)))
        
        mapping[0] = list(seven - one)
        mapping[1] = list(four - one)
        mapping[3] = list(four - one)
        mapping[2] = list(one)
        mapping[5] = list(one)

        one_1 = list(one)[0]
        one_2 = list(one)[1]

        res1 = list(filter(lambda x: one_1 in x and one_2 not in x, pattern))
        res2 = list(filter(lambda x: one_1 not in x and one_2 in x, pattern))

        if len(res2) == 1:
            temp = res2
            res2 = res1
            res1 = temp
        
        two = set(res1[0])
        five = set(res2[0])
        six = set(res2[1])

        if len(five) > len(six):
            temp = six
            six = five
            five = temp
        
        mapping[4] = list(six - five)

        mapping[6] = list(next(filter(lambda x: x not in mapping[0]
        and x not in mapping[1]
        and x not in mapping[2]
        and x not in mapping[4], mapping[6])))

        nine = set(next(filter(lambda x: len(x) == 6 and mapping[4][0] not in x, pattern)))

        remaining = list(filter(lambda x: set(x) not in [one, two, four, five, six, seven, eight, nine], pattern))
        three = set(next(filter(lambda x: len(x) == 5, remaining)))
        zero = set(next(filter(lambda x: len(x) == 6, remaining)))

        sum = ''
        for digit in digits:
            s = set(digit)
            if s == zero:
                sum += '0'
            elif s == one:
                sum += '1'
            elif s == two:
                sum += '2'
            elif s == three:
                sum += '3'
            elif s == four:
                sum += '4'
            elif s == five:
                sum += '5'
            elif s == six:
                sum += '6'
            elif s == seven:
                sum += '7'
            elif s == eight:
                sum += '8'
            elif s == nine:
                sum += '9'

        return int(sum)
