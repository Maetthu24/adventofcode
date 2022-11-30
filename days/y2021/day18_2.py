from common.aocdays import AOCDay, day
import re
from functools import reduce

DEBUG = True

@day(18)
class Day18(AOCDay):
    test_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".split("\n")

    ti1 = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]""".split('\n')

    def test(self, input_data):
        m1 = self.magnitude(eval('[[1,2],[[3,4],5]]'))
        assert m1 == 143, f'{m1} != 143'
        m2 = self.magnitude(eval('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'))
        assert m2 == 3488, f'{m2} != 3488'

        p0 = self.part1(self.ti1).__next__()
        print(p0)

        p1 = self.part1(self.test_input).__next__()
        assert p1 == 4140, f'{p1} != 4140'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2, f'{p2} != 2'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        numbers = [eval(line) for line in input_data]

        

        number = input_data[0]

        
        for i in range(1,len(input_data)):
            number = '[' + number + ',' + input_data[i] + ']'
            is_reduced = False
            while not is_reduced:
                is_reduced = True
            
        yield 0
        # yield self.magnitude(number)

    def part2(self, input_data):
        yield 2

    def add_numbers(self, x, y):
        result = [x, y]

        is_reduced = False
        while not is_reduced:
            is_reduced = True
            if self.depth(result) >= 5:
                result = self.explode(result)

        return result

    def depth(self, number):
        if isinstance(number[0], int) and isinstance(number[1], int):
            return 1
        else:
            return max(self.depth(number[0]), self.depth(number[1])) + 1
    
    def explode(self, l, number, r, has_exploded):
        if self.depth(number) >= 5:
            if not has_exploded:
                return (number[0], 0, number[1], True)
            else:
                return
        

        return self.explode(l, number[0], r, True, has_exploded)
        if has_exploded:
            return (0, number, 0, is_left, has_exploded)
        elif self.depth(number) >= 5:
            return (number[0], 0, number[1], True)
        elif is_left and isinstance(number[0], int):
            return (0, [number[0]+l, number[1]], r, has_exploded)
        elif (not is_left) and isinstance(number[1], int):
            return (l, [number[0], number[1]+r], 0, has_exploded)
        else:
            return (l, number, r, has_exploded)
            
        stack = [number[1], number[0]]
        
        while len(stack) > 0:
            stack.pop()
        
        yield 1

    def magnitude(self, number):
        if isinstance(number[0], list):
            x = self.magnitude(number[0])
        else:
            x = number[0]
        if isinstance(number[1], list):
            y = self.magnitude(number[1])
        else:
            y = number[1]
        return 3 * x + 2 * y
    
    def first_nested_4(self, number):
        depth = 0
        for (i,c) in enumerate(number):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            if depth == 5:
                return i+1
        return -1
    
    def first_greater_than_10(self, number):
        for (i,c) in enumerate(number):
            if i > 0 and c.isnumeric() and number[i-1].isnumeric():
                return i-1
        return -1

    def is_reduced(self, number):
        return self.first_nested_4(number) == -1 and self.first_greater_than_10(number) == -1