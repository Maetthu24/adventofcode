from common.aocdays import AOCDay, day

DEBUG = True

@day(18)
class Day18(AOCDay):
    test_input = """1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 26386, f'{p1} != 26386'

        r2 = 51 + 46 + 1445 + 669060 + 23340
        p2 = self.part2(self.test_input).__next__()
        assert p2 == r2, f'{p2} != {r2}'

    def part1(self, input_data):
        sum = 0

        for line in input_data:
            result = self.solve_equation(line.replace(' ', ''))
            sum += result
            print(f'{line} = {result}')

        yield sum

    def part2(self, input_data):
        sum = 0

        for line in input_data:
            result = self.solve_equation_2(list(line.replace(' ', '')))
            sum += result
            print(f'{line} = {result}')

        yield sum

    def solve_equation(self, equation):
        if len(equation) == 0:
            return 0
        if '*' not in equation and '+' not in equation:
            return int(equation)
        
        if '(' not in equation:
            i = 0
            while equation[i] not in ['*', '+']:
                i += 1
            result = int(equation[:i])
            equation = equation[i:]
            while len(equation) > 0:
                i = 1
                while i < len(equation) and equation[i] not in ['*', '+']:
                    i += 1
                
                if equation[0] == '*':
                    result *= int(equation[1:i])
                else:
                    result += int(equation[1:i])
                equation = equation[i:]

            return result
        else:
            (opening, closing) = self.parentheses_indices(equation)

            result = self.solve_equation(equation[opening+1:closing])
            equation = equation[:opening] + str(result) + equation[closing+1:]
            return self.solve_equation(equation)

    def solve_equation_2(self, equation):
        if len(equation) == 1:
            return int(equation[0])
        
        if '(' not in equation:
            while '+' in equation:
                idx = equation.index('+')
                equation = equation[:idx-1] + [int(equation[idx-1]) + int(equation[idx+1])] + equation[min(idx+2, len(equation)-1):]
            while '*' in equation:
                idx = equation.index('*')
                equation = equation[:idx-1] + [int(equation[idx-1]) * int(equation[idx+1])] + equation[min(idx+2, len(equation)-1):]
            return equation[0]
        else:
            (opening, closing) = self.parentheses_indices(equation)
            
            result = self.solve_equation_2(equation[opening+1:closing])
            equation = equation[:opening] + [str(result)] + equation[closing+1:]
            return self.solve_equation_2(equation)

    def parentheses_indices(self, equation):
        opening = None
        n = 0
        for i in range(len(equation)):
            if equation[i] == '(' and opening == None:
                opening = i
                n = 1
            elif equation[i] == '(':
                n += 1
            elif equation[i] == ')':
                if n == 1:
                    return (opening, i)
                else:
                    n -= 1
