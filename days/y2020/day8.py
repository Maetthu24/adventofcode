from common.aocdays import AOCDay, day

DEBUG = True

@day(8)
class Day8(AOCDay):
    test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 5, f'{p1} != 5'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 8, f'{p2} != 8'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        acc = 0
        pointer = 0
        visited = set()

        while pointer not in visited:
            visited.add(pointer)
            line = input_data[pointer].split(' ')
            operation = line[0]
            number = int(line[1])

            if operation == 'nop':
                pointer += 1
            elif operation == 'acc':
                acc += number
                pointer += 1
            elif operation == 'jmp':
                pointer += number

        yield acc

    def part2(self, input_data):
        for i in range(len(input_data) - 1):
            operation = input_data[i].split(' ')[0]
            if operation == 'acc':
                continue
            elif operation == 'nop':
                input_data[i] = input_data[i].replace('nop', 'jmp')
                result = self.run_instructions(input_data)
                if result == False:
                    input_data[i] = input_data[i].replace('jmp', 'nop')
                else:
                    yield result
                    break
            elif operation == 'jmp':
                input_data[i] = input_data[i].replace('jmp', 'nop')
                result = self.run_instructions(input_data)
                if result == False:
                    input_data[i] = input_data[i].replace('nop', 'jmp')
                else:
                    yield result
                    break
    
    def run_instructions(self, input_data):
        acc = 0
        pointer = 0
        visited = set()

        while pointer not in visited:
            if pointer == len(input_data):
                return acc

            visited.add(pointer)
            line = input_data[pointer].split(' ')
            operation = line[0]
            number = int(line[1])

            if operation == 'nop':
                pointer += 1
            elif operation == 'acc':
                acc += number
                pointer += 1
            elif operation == 'jmp':
                pointer += number

        return False
