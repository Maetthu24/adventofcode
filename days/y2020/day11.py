from common.aocdays import AOCDay, day
import copy

DEBUG = True

@day(11)
class Day11(AOCDay):
    test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 37, f'{p1} != 37'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 26, f'{p2} != 26'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        input_data = [list(x) for x in input_data]
        grid = input_data

        while True:
            new_grid = copy.deepcopy(grid)
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == '.':
                        continue
                    occupied = self.occupied_neighbours(grid, x, y)
                    if grid[x][y] == 'L' and occupied == 0:
                        new_grid[x][y] = '#'
                    elif grid[x][y] == '#' and occupied >= 4:
                        new_grid[x][y] = 'L'
            
            if grid == new_grid:
                count = 0
                for line in grid:
                    count += ''.join(line).count('#')
                yield count
                return
            
            grid = copy.deepcopy(new_grid)

    def part2(self, input_data):
        input_data = [list(x) for x in input_data]
        grid = input_data

        while True:
            new_grid = copy.deepcopy(grid)
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == '.':
                        continue
                    occupied = self.occupied_neighbours_seen(grid, x, y)
                    if grid[x][y] == 'L' and occupied == 0:
                        new_grid[x][y] = '#'
                    elif grid[x][y] == '#' and occupied >= 5:
                        new_grid[x][y] = 'L'
            
            self.print_grid(new_grid)
            if grid == new_grid:
                count = 0
                for line in grid:
                    count += ''.join(line).count('#')
                yield count
                return
            
            grid = copy.deepcopy(new_grid)

    def occupied_neighbours(self, grid, x, y):
        occupied = 0
        for i in range(max(0, x-1), min(len(grid), x+2)):
            for j in range(max(0, y-1), min(len(grid[0]), y+2)):
                if grid[i][j] == '#':
                    occupied += 1
        
        if grid[x][y] == '#':
            occupied -= 1
        
        return occupied

    def occupied_neighbours_seen(self, grid, x, y):
        occupied = 0
        dirs = [
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1)
        ]
        for (i, j) in dirs:
            seen_occupied = False
            pos = (x + i, y + j)
            while pos[0] in range(0, len(grid)) and pos[1] in range(0, len(grid[0])):
                if grid[pos[0]][pos[1]] == '#':
                    seen_occupied = True
                    break
                elif grid[pos[0]][pos[1]] == 'L':
                    break
                pos = (pos[0]+i, pos[1]+j)
            
            if seen_occupied:
                occupied += 1
        
        return occupied
    
    def print_grid(self, grid):
        for line in grid:
            print(''.join(line))
        print('\n')
