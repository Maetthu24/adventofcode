from common.aocdays import AOCDay, day

DEBUG = True

@day(24)
class Day24(AOCDay):
    test_input = """""".split("\n")

    visited = set()
    memory = dict()
    instruction_sets = []
    vardict = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    index = dict(w=0, x=1, y=2, z=3)

    def test(self, input_data):
        # p1 = self.part1(self.test_input).__next__()
        # assert p1 == 1, f'{p1} != 1'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2, f'{p2} != 2'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        # yield self.dfs(input_data, True, [])
        self.instruction_sets = []
        s = []
        for i,line in enumerate(input_data):
            s.append(line)
            if i == len(input_data)-1 or input_data[i+1].startswith('inp'):
                self.instruction_sets.append(s)
                s = []

        print(self.is_valid_serial(39924989499969))
        print(self.is_valid_serial(16811412161117))
        yield 0
        # input = 99999999999999
        # self.visited = set()

        # c = 0
        # while True:
        #     c += 1
        #     if c % 10000 == 0:
        #         print(f'Trying {input}')
        #     if self.is_valid_serial(input):
        #         yield input
        #         break
        #     else:
        #         input -= 1
        #         while '0' in str(input):
        #             input -= 1

    def part2(self, input_data):
        yield 2

    def find_largest_serial(self, input_data):
        state = (0,0,0,0) # x,y,z,w
        i = 0
        nr = 9

        visited = set()


    def is_valid_serial(self, input):
        self.vardict['x'] = 0
        self.vardict['y'] = 0
        self.vardict['z'] = 0
        self.vardict['w'] = 0

        states = set()
        nr = str(input)
        for i in range(len(nr)):
            result, state = self.run_instructions(nr[i:], self.instruction_sets[i], i)
            if result == False:
                self.visited = self.visited.union(states)
                return False
            else:
                states.add(state)

        if self.vardict['z'] == 0:
            return True
        else:
            self.visited = self.visited.union(states)
            return False

    def run_instructions(self, nr, instructions, i):
        # key = (self.vardict['x'],self.vardict['y'],self.vardict['z'],self.vardict['w'],i)

        input_var = instructions[0].split(' ')[1]
        self.vardict[input_var] = int(nr[0])

        key = (self.vardict['z'],int(nr[0]),i)
        memkey = (self.vardict['z'],self.vardict['w'],int(nr[0]),i)
        if key in self.visited:
            return False, None
        
        if memkey in self.memory:
            mem = self.memory[memkey]
            self.vardict['x'] = mem[0]
            self.vardict['y'] = mem[1]
            self.vardict['z'] = mem[2]
            self.vardict['w'] = mem[3]
            return True, key
        
        for ins in instructions[1:]:
            parts = ins.split(' ')

            match parts[0]:
                case 'add':
                    if parts[2] in self.vardict:
                        self.vardict[parts[1]] += self.vardict[parts[2]]
                    else:
                        self.vardict[parts[1]] += int(parts[2])
                case 'mul':
                    if parts[2] in self.vardict:
                        self.vardict[parts[1]] *= self.vardict[parts[2]]
                    else:
                        self.vardict[parts[1]] *= int(parts[2])
                case 'div':
                    if parts[2] in self.vardict:
                        self.vardict[parts[1]] = self.vardict[parts[1]] // self.vardict[parts[2]]
                    else:
                        self.vardict[parts[1]] = self.vardict[parts[1]] // int(parts[2])
                case 'mod':
                    if parts[2] in self.vardict:
                        self.vardict[parts[1]] = self.vardict[parts[1]] % self.vardict[parts[2]]
                    else:
                        self.vardict[parts[1]] = self.vardict[parts[1]] % int(parts[2])
                case 'eql':
                    if parts[2] in self.vardict:
                        self.vardict[parts[1]] = 1 if self.vardict[parts[1]] == self.vardict[parts[2]] else 0
                    else:
                        self.vardict[parts[1]] = 1 if self.vardict[parts[1]] == int(parts[2]) else 0
        
        self.memory[memkey] = (self.vardict['x'],self.vardict['y'],self.vardict['z'],self.vardict['w'])
        
        return True, key


    def apply_arithmetic(self, lines, state, line_number):
        while line_number < len(lines) and not lines[line_number].startswith('inp'):
            operator, a, b = lines[line_number].split()
            idx = self.index[a]
            result = state[idx]
            value = state[self.index[b]] if b in self.index.keys() else int(b)
            match operator:
                case 'add': result += value
                case 'mul': result *= value
                case 'div': result //= value
                case 'mod': result %= value
                case 'eql': result = 1 if result == value else 0

            state = state[:idx] + (result, ) + state[idx+1:]
            line_number += 1

        return state, line_number


    def compute_next(self, lines, current, find_largest):
        state, line_number, number = current

        _, a = lines[line_number].split()
        idx = self.index[a]
        for i in range(1, 10) if find_largest else reversed(range(1, 10)):
            new_state = state[:idx] + (i, ) + state[idx+1:]

            result_state, result_line_number = self.apply_arithmetic(lines, new_state, line_number + 1)
            yield result_state, result_line_number, number * 10 + i


    def dfs(self, lines, find_largest, ignored_prefixes):
        s = [((0, 0, 0, 0), 0, 0)]

        visited = set()

        while s:
            state, line_number, input_number = s.pop()

            if input_number in ignored_prefixes:
                continue  # This is kind of a heck, but

            if line_number == len(lines):
                if state[self.index['z']] == 0:
                    return input_number
                else:
                    continue

            lookup = line_number, state[self.index['z']]
            if lookup in visited:
                continue
            visited.add(lookup)

            for result in self.compute_next(lines, (state, line_number, input_number), find_largest):
                s.append(result)


# with open('input') as f:
#     lines = f.readlines()
#     # ignored_prefixes: skip numbers that start with these prefixes
#     # Be aware, that the ignored_prefixes depend on the given input!
#     # For my personal input it turned out that the largest accepted
#     # number starts with a 2 and the smallest starts with 14.
#     print(f"\rPart 1: {dfs(find_largest=True, ignored_prefixes=[9, 8, 7, 6, 5, 4, 3])}")
#     print(f"\rPart 2: {dfs(find_largest=False, ignored_prefixes=[11, 12, 13])}")
