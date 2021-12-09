from functools import reduce
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

        yield reduce(lambda x1, y1: x1 + reduce(lambda x2, y2: x2 + 1 if len(y2) in [2,3,4,7] else x2, y1, 0), digits, 0)

    def part2(self, input_data):
        yield reduce(lambda x, y: x + self.solve_line(y), input_data, 0)
    
    def solve_line(self, line):
        patterns = [frozenset(x) for x in line.split(' | ')[0].split(' ')]
        digits = [frozenset(x) for x in line.split(' | ')[1].split(' ')]

        five_patterns = [p for p in patterns if len(p) == 5]
        six_patterns = [p for p in patterns if len(p) == 6]

        solutions = dict()
        solutions[1] = [p for p in patterns if len(p) == 2][0]
        solutions[4] = [p for p in patterns if len(p) == 4][0]
        solutions[7] = [p for p in patterns if len(p) == 3][0]
        solutions[8] = [p for p in patterns if len(p) == 7][0]
        solutions[3] = [p for p in five_patterns if p.issuperset(solutions[1])][0]
        solutions[9] = [p for p in six_patterns if p.issuperset(solutions[4])][0]
        solutions[6] = [p for p in six_patterns if len(p.intersection(solutions[1])) == 1][0]
        solutions[5] = [p for p in five_patterns if len(p.intersection(solutions[6])) == 5][0]
        solutions[2] = list(set(five_patterns).difference({solutions[3], solutions[5]}))[0]
        solutions[0] = list(set(six_patterns).difference({solutions[9], solutions[6]}))[0]

        mappings = {v: k for k, v in solutions.items()}
        number = ''.join([str(mappings[x]) for x in digits])
        return int(number)
