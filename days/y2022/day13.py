from common.aocdays import AOCDay, day
import json

DEBUG = True

@day(13)
class Day13(AOCDay):
    test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 13, f'{p1} != 13'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 140, f'{p2} != 140'

    def common(self, input_data):
        yield 0

    def compare(self, left, right):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            elif left > right:
                return False
            else:
                return None
        elif isinstance(left, int):
            return self.compare([left], right)
        elif isinstance(right, int):
            return self.compare(left, [right])
        else:
            # Both are lists
            for i in range(len(left)):
                left_el = left[i]
                if i > len(right) - 1:
                    return False
                else:
                    right_el = right[i]
                    res = self.compare(left_el, right_el)
                    if res == None:
                        continue
                    else:
                        return res
            if len(right) > len(left):
                return True
            return None

    def part1(self, input_data):
        correct = 0
        for idx, line in enumerate('\n'.join(input_data).split('\n\n')):
            p1 = json.loads(line.split('\n')[0])
            p2 = json.loads(line.split('\n')[1])
            res = self.compare(p1, p2)
            print(res)
            if res:
                correct += idx + 1

        yield correct

    def part2(self, input_data):
        lines = []
        for line in input_data:
            if len(line) == 0:
                continue
            lines.append(json.loads(line))
        lines.append([[2]])
        lines.append([[6]])

        print(lines)
        print("--------")
        n = len(lines)
        # optimize code, so if the array is already sorted, it doesn't need
        # to go through the entire process
        swapped = False
        # Traverse through all array elements
        for i in range(n-1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.
            # Last i elements are already in place
            for j in range(0, n-i-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                res = self.compare(lines[j], lines[j+1])
                if not res:
                    swapped = True
                    lines[j], lines[j + 1] = lines[j + 1], lines[j]
            
            if not swapped:
                # if we haven't needed to make a single swap, we
                # can just exit the main loop.
                return

        # for i in range(len(lines) + 1):
        #     for j in range(1, len(lines) - 1):
        #         res = self.compare(lines[j-1], lines[j])
        #         if not res:
        #             temp = lines[j-1]
        #             lines[j-1] = lines[j]
        #             lines[j] = temp

        print(lines)

        yield (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)
