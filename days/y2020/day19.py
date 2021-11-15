from common.aocdays import AOCDay, day

DEBUG = True

@day(19)
class Day19(AOCDay):
    test_input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".split("\n")

    ti_2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".split('\n')

    rules = {}

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 2, f'{p1} != 2'

        p1b = self.part1(self.ti_2).__next__()
        assert p1b == 3, f'{p1b} != 3'

        p2 = self.part2(self.ti_2).__next__()
        assert p2 == 12, f'{p2} != 12'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        self.rules = {}

        for line in '\n'.join(input_data).split('\n\n')[0].split('\n'):
            parts = line.split(': ')
            nr = int(parts[0])
            if parts[1].startswith('"'):
                self.rules[nr] = parts[1][1:-1]
            else:
                self.rules[nr] = []
                for p in parts[1].split(' | '):
                    self.rules[nr].append([int(x)for x in p.split(' ')])

        valid_strings = 0

        for string in '\n'.join(input_data).split('\n\n')[1].split('\n'):
            (valid, rest) = self.is_valid_string(string, 0)
            if valid and len(rest) == 0:
                valid_strings += 1

        yield valid_strings

    def part2(self, input_data):
        self.rules = {}

        for line in '\n'.join(input_data).split('\n\n')[0].split('\n'):
            parts = line.split(': ')
            nr = int(parts[0])
            if parts[1].startswith('"'):
                self.rules[nr] = parts[1][1:-1]
            else:
                self.rules[nr] = []
                for p in parts[1].split(' | '):
                    self.rules[nr].append([int(x)for x in p.split(' ')])

        self.rules[8] = [[42], [42, 8]]
        self.rules[11] = [[42, 31], [42, 11, 31]]

        valid_strings = 0

        for string in '\n'.join(input_data).split('\n\n')[1].split('\n'):
            remaining = string
            part1 = True
            found1 = 0
            while part1:
                found = False
                for i in range(2, len(remaining)+1):
                    (valid, rest) = self.is_valid_string(remaining[:i], 42)
                    if valid and len(rest) == 0:
                        found = True
                        found1 +=1
                        remaining = remaining[i:]
                        break
                if not found:
                    part1 = False

            part2 = True
            if found1 == 0:
                part2 = False
            found2 = 0
            while part2:
                found = False
                for i in range(2, len(remaining)+1):
                    (valid, rest) = self.is_valid_string(remaining[:i], 31)
                    if valid and len(rest) == 0:
                        found = True
                        found2 += 1
                        remaining = remaining[i:]
                        if len(remaining) == 0:
                            if found1 > found2:
                                valid_strings += 1
                            part2 = False
                        break
                if not found:
                    part2 = False
                        
        yield valid_strings

    def is_valid_string(self, string, nr):
        rule = self.rules[nr]
        if isinstance(rule, str):
            if string.startswith(rule):
                return (True, string[len(rule):])
            else:
                return (False, string)

        for nrs in rule:
            remaining = string
            possibly_valid = True
            for n in nrs:
                (valid, rest) = self.is_valid_string(remaining, n)
                if not valid:
                    possibly_valid = False
                    break
                else:
                    remaining = rest
            
            if possibly_valid:
                return (True, remaining)
        
        return (False, string)
