from collections import Counter, defaultdict
from common.aocdays import AOCDay, day

DEBUG = True

@day(14)
class Day14(AOCDay):
    test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 1588, f'{p1} != 1588'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2188189693529, f'{p2} != 2188189693529'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        # template = input_data[0]
        # rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in input_data[2:]}

        # for i in range(10):
        #     new = template[0]
        #     for j in range(0, len(template)-1):
        #         new += rules[template[j:j+2]] + template[j+1]
        #     template = new
        #     print(len(template))
        #     c = Counter(template)
        #     print(c)
        
        # c = Counter(template)
        # yield max(c.values()) - min(c.values())

        template = input_data[0]
        rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in input_data[2:]}

        pair_mappings = {k: [f'{k[0]}{v}', f'{v}{k[1]}'] for k, v in rules.items()}

        pair_counts = defaultdict(lambda: 0)

        for i in range(0, len(template)-1):
            pair_counts[template[i:i+2]] += 1

        for i in range(10):
            new_counts = defaultdict(lambda: 0)
            for pair, c in pair_counts.items():
                for mapped in pair_mappings[pair]:
                    new_counts[mapped] += c
            pair_counts = new_counts
        
        letter_counts = defaultdict(lambda: 0)

        for pair, c in pair_counts.items():
            letter_counts[pair[0]] += c
            letter_counts[pair[1]] += c
        letter_counts[template[0]] += 1
        letter_counts[template[-1]] += 1

        letter_counts = [int(x / 2) for x in letter_counts.values()]
        yield max(letter_counts) - min(letter_counts)

    def part2(self, input_data):
        template = input_data[0]
        rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in input_data[2:]}

        pair_mappings = {k: [f'{k[0]}{v}', f'{v}{k[1]}'] for k, v in rules.items()}

        pair_counts = defaultdict(lambda: 0)

        for i in range(0, len(template)-1):
            pair_counts[template[i:i+2]] += 1

        for i in range(40):
            new_counts = defaultdict(lambda: 0)
            for pair, c in pair_counts.items():
                for mapped in pair_mappings[pair]:
                    new_counts[mapped] += c
            pair_counts = new_counts
        
        letter_counts = defaultdict(lambda: 0)

        for pair, c in pair_counts.items():
            letter_counts[pair[0]] += c
            letter_counts[pair[1]] += c
        letter_counts[template[0]] += 1
        letter_counts[template[-1]] += 1

        letter_counts = [int(x / 2) for x in letter_counts.values()]
        yield max(letter_counts) - min(letter_counts)
