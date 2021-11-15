from common.aocdays import AOCDay, day
import re
import itertools

DEBUG = True

@day(14)
class Day14(AOCDay):
    test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split("\n")

    test_input_2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n')

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 165, f'{p1} != 165'

        p2 = self.part2(self.test_input_2).__next__()
        assert p2 == 208, f'{p2} != 208'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        memory = {}
        
        and_mask = bin(0)
        or_mask = bin(0)
        for line in input_data:
            if line.startswith('mask'):
                bitmask = line.split(' = ')[1]
                or_mask = int(''.join(['1' if x == '1' else '0' for x in bitmask]), 2)
                and_mask = int(''.join(['0' if x == '0' else '1' for x in bitmask]), 2)
            else:
                start = line.index('[') + 1
                end = line.index(']')
                index = int(line[start:end])
                number = int(line.split(' = ')[1])
                number = number | or_mask
                number = number & and_mask
                memory[index] = number
                
        yield sum(memory.values())

    def part2(self, input_data):
        memory = {}
        
        current_bitmask = ''
        or_mask = bin(0)
        for line in input_data:
            if line.startswith('mask'):
                bitmask = line.split(' = ')[1]
                current_bitmask = bitmask
                or_mask = int(''.join(['1' if x == '1' else '0' for x in bitmask]), 2)

            else:
                start = line.index('[') + 1
                end = line.index(']')
                index = int(line[start:end])
                index = index | or_mask
                number = int(line.split(' = ')[1])

                floating = [m.start() for m in re.finditer('X', current_bitmask)]

                if len(floating) == 0:
                    memory[index] = number
                else:
                    combinations = itertools.product('01', repeat=len(floating))
                    for comb in combinations:
                        b = ['0'] * len(list((bin(index))[2:])) + list((bin(index)))[2:]
                        for i in range(len(floating)):
                            b[-(36-floating[i])] = comb[i]
                        idx = int(''.join(b), 2)
                        memory[idx] = number
                
        yield sum(memory.values())
