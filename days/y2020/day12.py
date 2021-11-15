from common.aocdays import AOCDay, day
import math

DEBUG = True

@day(12)
class Day12(AOCDay):
    test_input = """F10
N3
F7
R90
F11""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 25, f'{p1} != 25'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 286, f'{p2} != 286'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        input_data = [(x[0], int(x[1:])) for x in input_data]

        directions = {
            90: (1,0),
            180: (0,-1),
            270: (-1,0),
            0: (0,1)
        }

        degrees = 90
        x = 0
        y = 0

        for (action, number) in input_data:
            if action == 'F':
                dir = directions[degrees]
                x += dir[0] * number
                y += dir[1] * number
            elif action == 'N':
                y += number
            elif action == 'E':
                x += number
            elif action == 'S':
                y -= number
            elif action == 'W':
                x -= number
            elif action == 'L':
                degrees = (degrees + 360 - number) % 360
            elif action == 'R':
                degrees = (degrees + number) % 360

        yield abs(x) + abs(y)

    def part2(self, input_data):
        input_data = [(x[0], int(x[1:])) for x in input_data]

        x = 0
        y = 0

        w_x = 10
        w_y = 1

        for (action, number) in input_data:
            if action == 'F':
                x += w_x * number
                y += w_y * number
            elif action == 'N':
                w_y += number
            elif action == 'E':
                w_x += number
            elif action == 'S':
                w_y -= number
            elif action == 'W':
                w_x -= number
            elif action == 'L':
                angle = math.radians(number)
                s = math.sin(angle)
                c = math.cos(angle)
                old_x = w_x
                old_y = w_y
                w_x = round(old_x * c - old_y * s)
                w_y = round(old_x * s + old_y * c)
            elif action == 'R':
                angle = math.radians(-number)
                s = math.sin(angle)
                c = math.cos(angle)
                old_x = w_x
                old_y = w_y
                w_x = round(old_x * c - old_y * s)
                w_y = round(old_x * s + old_y * c)

        yield abs(x) + abs(y)
