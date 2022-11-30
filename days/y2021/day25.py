from common.aocdays import AOCDay, day

DEBUG = True

@day(25)
class Day25(AOCDay):
    test_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 58, f'{p1} != 58'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2, f'{p2} != 2'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        grid = [[x for x in line] for line in input_data]

        steps = 0
        has_movement = True

        # print(f'Step = {steps}')
        # for line in grid:
        #     print(''.join(line))
        # print('\n')

        while has_movement:
            steps += 1
            has_movement = False
            new_grid = [[x for x in line] for line in grid]

            # East-facing
            for (x,_) in enumerate(grid):
                for (y,c) in enumerate(grid[x]):
                    if grid[x][y] == '>':
                        if y == len(grid[x])-1:
                            if grid[x][0] == '.':
                                new_grid[x][0] = '>'
                                new_grid[x][y] = '.'
                                has_movement = True
                        else:
                            if grid[x][y+1] == '.':
                                new_grid[x][y+1] = '>'
                                new_grid[x][y] = '.'
                                has_movement = True

            grid = [[x for x in line] for line in new_grid]

            # South-facing
            for (x,_) in enumerate(grid):
                for (y,c) in enumerate(grid[x]):
                    if grid[x][y] == 'v':
                        if x == len(grid)-1:
                            if grid[0][y] == '.':
                                new_grid[0][y] = 'v'
                                new_grid[x][y] = '.'
                                has_movement = True
                        else:
                            if grid[x+1][y] == '.':
                                new_grid[x+1][y] = 'v'
                                new_grid[x][y] = '.'
                                has_movement = True
            
            grid = [[x for x in line] for line in new_grid]

            # print(f'Step = {steps}')
            # for line in grid:
            #     print(''.join(line))
            # print('\n')

        yield steps

    def part2(self, input_data):
        yield 2
