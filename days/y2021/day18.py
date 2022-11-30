from common.aocdays import AOCDay, day
import re

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
        assert p2 == 3993, f'{p2} != 3993'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        yield self.add(input_data)

    def part2(self, input_data):
        sum_max = 0
        for x in range(len(input_data)):
            for y in range(len(input_data)):
                if x != y:
                    sum = self.add([input_data[x], input_data[y]])
                    if sum > sum_max:
                        sum_max = sum

        yield sum_max

    def add(self, input_data):
        number = input_data[0]

        for i in range(1,len(input_data)):
            number = '[' + number + ',' + input_data[i] + ']'
            is_reduced = False
            while not is_reduced:
                is_reduced = True
                nested_idx = self.first_nested_4(number)
                if nested_idx != -1: # explode
                    is_reduced = False
                    pair = re.finditer('\d+,\d+', number[nested_idx:]).__next__()
                    x = int(pair[0].split(',')[0])
                    y = int(pair[0].split(',')[1])

                    previous = [x for x in re.finditer('\d+', number[:nested_idx])]
                    if len(previous) > 0:
                        previous = previous.pop()
                        new_nr = str(x + int(number[previous.start():previous.end()]))
                        start = number[:previous.start()] + new_nr + number[previous.end():nested_idx]
                    else:
                        start = number[:nested_idx]
                    
                    next = [x for x in re.finditer('\d+', number[nested_idx+pair.end():])]
                    if len(next) > 0:
                        next = next[0]
                        end = number[nested_idx+pair.end()+1:nested_idx+pair.end()+next.start()] + str(y + int(number[nested_idx+pair.end()+next.start():nested_idx+pair.end()+next.end()])) + number[nested_idx+pair.end()+next.end():]
                    else:
                        end = number[nested_idx+pair.end()+1:]

                    number = start + '0' + end
                else:
                    res = [x for x in re.finditer('\d\d+', number)]
                    if len(res) > 0:
                        res = res[0]
                        is_reduced = False
                        n = int(number[res.start():res.end()])
                        iseven = n % 2 == 0
                        number = number[:res.start()] + '[' + str(int(n/2)) + ',' + (str(int(n/2)) if iseven else str(int(n/2)+1)) + ']' + number[res.end():]
                
        return self.magnitude(eval(number))
    
    def first_nested_4(self, number):
        depth = 0
        for (i,c) in enumerate(number):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            if depth == 5:
                return i
        return -1
    
    def first_greater_than_10(self, number):
        for (i,c) in enumerate(number):
            if i > 0 and c.isnumeric() and number[i-1].isnumeric():
                return i-1
        return -1

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
    
    # def magnitude(self, number):
    #     idx = number.find('[')
    #     while idx != -1:
    #         match = re.finditer('\[\d+,\d+\]', number).__next__()
    #         n1 = int(match[0].lstrip('[').rstrip(']').split(',')[0])
    #         n2 = int(match[0].lstrip('[').rstrip(']').split(',')[1])
    #         number = number[:match.start()] + str(3*n1 + 2*n2) + number[match.end():]
    #         idx = number.find('[')
        
    #     return int(number)
