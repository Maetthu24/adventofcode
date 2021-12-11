from common.aocdays import AOCDay, day
import numpy as np

DEBUG = True

@day(11)
class Day11(AOCDay):
    test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 1656, f'{p1} != 1656'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 195, f'{p2} != 195'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        grid = np.array([[int(x) for x in line] for line in input_data])

        sum = 0

        for i in range(100):
            (grid, flashes) = self.make_step(grid)
            sum += flashes
            # print(f'After step {i+1}: {sum} flashes (+{flashes})')
            # print(grid)
            # print('\n')

        yield sum

    def part2(self, input_data):
        grid = np.array([[int(x) for x in line] for line in input_data])

        i = 1
        while True:
            (grid, flashes) = self.make_step(grid)
            if flashes == 100:
                break
            i += 1

        yield i
    
    def make_step(self, grid):
        grid += 1
        flashes = np.where(grid > 9)
        flashes = list(zip(flashes[0], flashes[1]))
        
        count = 0
        flashed = set()
        for (x,y) in flashes:
            (grid, f, flashed) = self.flash(grid, flashed, x, y)
            count += f
        
        for (x,y) in flashed:
            grid[x][y] = 0
        
        return (grid, count)

    def flash(self, grid, old_flashed, x, y):
        to_flash = set()
        if (x,y) not in old_flashed:
            to_flash.add((x,y))
        flashed = set()
        while len(to_flash) > 0:
            (x,y) = to_flash.pop()
            flashed.add((x,y))
            neighbors = self.neighbors(x,y)
            for (x1,y1) in neighbors:
                grid[x1][y1] += 1
                if grid[x1][y1] > 9 and (x1,y1) not in flashed and (x1,y1) not in old_flashed:
                    to_flash.add((x1,y1))

        return (grid, len(flashed), flashed.union(old_flashed))
    
    def neighbors(self, x, y):
        neighbors = set()
        for u in range(max(x-1, 0), min(9, x+1) + 1):
            for v in range(max(y-1, 0), min(9, y+1) + 1):
                neighbors.add((u, v))
        return neighbors - {(x,y)}
