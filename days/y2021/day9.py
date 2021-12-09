from common.aocdays import AOCDay, day

DEBUG = True

@day(9)
class Day9(AOCDay):
    test_input = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 15, f'{p1} != 15'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 1134, f'{p2} != 1134'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        heatmap = [[int(x) for x in line] for line in input_data]

        sum = 0
        for x in range(len(heatmap)):
            for y in range(len(heatmap[x])):
                sum += self.risk_level(heatmap, x, y)

        yield sum

    def part2(self, input_data):
        heatmap = [[int(x) for x in line] for line in input_data]
        lowpoints = []

        # Find all low points
        for x in range(len(heatmap)):
            for y in range(len(heatmap[x])):
                if self.is_lowpoint(heatmap, x, y):
                    lowpoints.append((x,y))

        # Each basin starts from a low point, so we recursively find all basin sizes
        basin_sizes = []
        for (x,y) in lowpoints:
            basin_sizes.append(self.basin_size(heatmap, [], x, y))
        
        # Sort the basin sizes and multiply the three largest
        basin_sizes = sorted(basin_sizes, reverse=True)
        yield basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    def risk_level(self, heatmap, x, y):
        return heatmap[x][y] + 1 if self.is_lowpoint(heatmap, x, y) else 0
    
    def is_lowpoint(self, heatmap, x, y):
        point = heatmap[x][y]
        is_lowpoint = True
        if x > 0 and heatmap[x-1][y] <= point:
            is_lowpoint = False
        if x < len(heatmap) - 1 and heatmap[x+1][y] <= point:
            is_lowpoint = False
        if y > 0 and heatmap[x][y-1] <= point:
            is_lowpoint = False
        if y < len(heatmap[0]) - 1 and heatmap[x][y+1] <= point:
            is_lowpoint = False

        return is_lowpoint
    
    def basin_size(self, heatmap, already_found, x, y):
        point = heatmap[x][y]
        size = 1
        if x > 0 and (x-1,y) not in already_found and point < heatmap[x-1][y] < 9:
            already_found.append((x-1,y))
            size += self.basin_size(heatmap, already_found, x-1, y)
        if x < len(heatmap)-1 and (x+1,y) not in already_found and point < heatmap[x+1][y] < 9:
            already_found.append((x+1,y))
            size += self.basin_size(heatmap, already_found, x+1, y)
        if y > 0 and (x,y-1) not in already_found and point < heatmap[x][y-1] < 9:
            already_found.append((x,y-1))
            size += self.basin_size(heatmap, already_found, x, y-1)
        if y < len(heatmap[x])-1 and (x,y+1) not in already_found and point < heatmap[x][y+1] < 9:
            already_found.append((x,y+1))
            size += self.basin_size(heatmap, already_found, x, y+1)
        return size
