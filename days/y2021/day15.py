from common.aocdays import AOCDay, day

DEBUG = True

@day(15)
class Day15(AOCDay):
    test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 40, f'{p1} != 40'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 315, f'{p2} != 315'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        grid = [[int(x) for x in line] for line in input_data]
        rows = len(grid)
        columns = len(grid[0])

        nodes = [(x,y) for x in range(rows) for y in range(columns)]
        distances = {node: rows * columns + 1 for node in nodes}
        queue = [(0,0,0)]

        while len(queue) > 0:
            queue.sort(key=lambda x: x[2])
            (x,y, dist) = queue.pop(0)
            for (nx,ny) in self.neighbors(x,y,rows,columns):
                new_dist = dist + grid[nx][ny]
                if new_dist < distances[(nx,ny)]:
                    distances[(nx,ny)] = new_dist
                    queue.append((nx,ny,new_dist))

        yield distances[(rows-1, columns-1)]

    def part2(self, input_data):
        grid = [[int(x) for x in line] for line in input_data]

        large_grid = []
        for i in range(5):
            for line in grid:
                n = []
                for j in range(5):
                    n += list(map(lambda x: (x+i+j-1) % 9 + 1, line))
                large_grid.append(n)

        grid = large_grid

        rows = len(grid)
        columns = len(grid[0])

        nodes = [(x,y) for x in range(rows) for y in range(columns)]
        distances = {node: rows * columns + 1 for node in nodes}
        queue = [(0,0,0)]

        while len(queue) > 0:
            queue.sort(key=lambda x: x[2])
            (x,y, dist) = queue.pop(0)
            for (nx,ny) in self.neighbors(x,y,rows,columns):
                new_dist = dist + grid[nx][ny]
                if new_dist < distances[(nx,ny)]:
                    distances[(nx,ny)] = new_dist
                    queue.append((nx,ny,new_dist))

        yield distances[(rows-1, columns-1)]
    
    def neighbors(self, x, y, rows, columns):
        return [(u,v) for (u,v) in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if 0 <= u < rows and 0 <= v < columns]
