from common.aocdays import AOCDay, day

DEBUG = True

@day(7)
class Day7(AOCDay):
    test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")

    test_input_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split('\n')

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 4, f'{p1} != 4'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 32, f'{p2} != 32'

        p2b = self.part2(self.test_input_2).__next__()
        assert p2b == 126, f'{p2b} != 126'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        contained_in = {}

        for line in input_data:
            no_bags = line.find(' bags contain no other bags')
            if no_bags != -1:
                continue
            else:
                container = line.split(' ')[0] + ' ' + line.split(' ')[1]

                start_index = line.find('contain ')
                last_part = line[(start_index + 8):].split(',')
                for part in last_part:
                    parts = part.strip().split(' ')
                    key = parts[1] + ' ' + parts[2]
                    if key in contained_in:
                        contained_in[key].append((container, int(parts[0])))
                    else:
                        contained_in[key] = [(container, int(parts[0]))]

        colors = set()
        to_check = ['shiny gold']

        while len(to_check) > 0:
            key = to_check[0]
            if key in contained_in:
                for (color, count) in contained_in[key]:
                    if color not in to_check:
                        to_check.append(color)
                    colors.add(color)
            
            to_check.remove(key)
        
        yield len(colors)


    def part2(self, input_data):
        contains = {}

        for line in input_data:
            no_bags = line.find(' bags contain no other bags')
            if no_bags != -1:
                continue
            else:
                key = line.split(' ')[0] + ' ' + line.split(' ')[1]

                start_index = line.find('contain ')
                last_part = line[(start_index + 8):].split(',')
                contains[key] = []
                for part in last_part:
                    parts = part.strip().split(' ')
                    bag = parts[1] + ' ' + parts[2]
                    contains[key].append((bag, int(parts[0])))
        
        yield self.bag_count(contains, 'shiny gold') - 1

    def bag_count(self, contains, key):
        if key not in contains:
            return 1
        else:
            sum = 1
            for (bag, count) in contains[key]:
                sum += count * self.bag_count(contains, bag)
            return sum
