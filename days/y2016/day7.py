from common.aocdays import AOCDay, day

DEBUG = True

@day(7)
class Day7(AOCDay):
    test_input = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""".split("\n")

    test_input_2 = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 2, f'{p1} != 2'

        p2 = self.part2(self.test_input_2).__next__()
        assert p2 == 3, f'{p2} != 3'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        count = 0

        for line in input_data:
            is_inside = False
            c = 0
            for i in range(len(line) - 3):
                is_abba = line[i] != line[i+1] and line[i] == line[i+3] and line[i+1] == line[i+2]
                if is_abba and is_inside:
                    c = 0
                    break
                elif is_abba:
                    c = 1
                if line[i] == '[':
                    is_inside = True
                elif line[i] == ']':
                    is_inside = False
            count += c


        yield count

    def part2(self, input_data):
        count = 0

        for line in input_data:
            is_inside = False
            aba_pairs = []
            bab_pairs = []

            for i in range(len(line) - 2):
                is_aba = line[i] != line[i+1] and line[i] == line[i+2]
                if is_aba:
                    if is_inside and (line[i+1], line[i]) not in bab_pairs:
                        bab_pairs.append((line[i+1], line[i]))
                    if (not is_inside) and (line[i], line[i+1]) not in aba_pairs:
                        aba_pairs.append((line[i], line[i+1]))
                if line[i] == '[':
                    is_inside = True
                elif line[i] == ']':
                    is_inside = False

            for tuple in aba_pairs:
                if tuple in bab_pairs:
                    count += 1
                    break

        yield count
