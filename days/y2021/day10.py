from common.aocdays import AOCDay, day

DEBUG = True

@day(10)
class Day10(AOCDay):
    test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 26397, f'{p1} != 26397'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 288957, f'{p2} != 288957'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        error_score = dict()
        error_score[')'] = 3
        error_score[']'] = 57
        error_score['}'] = 1197
        error_score['>'] = 25137

        openings = ['(', '[', '{', '<']
        closings = [')', ']', '}', '>']

        matches = dict()
        matches[')'] = '('
        matches[']'] = '['
        matches['}'] = '{'
        matches['>'] = '<'

        error_sum = 0
        for line in input_data:
            open = []
            for c in line:
                if c in openings:
                    open.append(c)
                elif c in closings:
                    if matches[c] == open[-1]:
                        open.pop()
                    else:
                        error_sum += error_score[c]
                        break

        yield error_sum

    def part2(self, input_data):
        score = dict()
        score[')'] = 1
        score[']'] = 2
        score['}'] = 3
        score['>'] = 4

        openings = ['(', '[', '{', '<']
        closings = [')', ']', '}', '>']

        matches = dict()
        matches[')'] = '('
        matches[']'] = '['
        matches['}'] = '{'
        matches['>'] = '<'

        openmatches = {v: k for k, v in matches.items()}

        sums = []
        for line in input_data:
            open = []
            corrupt = False
            for c in line:
                if c in openings:
                    open.append(c)
                elif c in closings:
                    if matches[c] == open[-1]:
                        open.pop()
                    else:
                        corrupt = True
                        break
            if corrupt:
                continue
            elif len(open) > 0:
                s = 0
                while len(open) > 0:
                    last = open.pop()
                    s = s*5 + score[openmatches[last]]
                sums.append(s)
        
        sums = sorted(sums)
        yield sums[int(len(sums) / 2)]
