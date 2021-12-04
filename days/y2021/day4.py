from common.aocdays import AOCDay, day

DEBUG = True

@day(4)
class Day4(AOCDay):
    test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 4512, f'{p1} != 4512'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 1924, f'{p2} != 1924'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        parts = '\n'.join(input_data).split('\n\n')
        bingo_numbers = [int(x) for x in parts[0].split(',')]

        grids = []

        for part in parts[1:]:
            lines = part.split('\n')
            grids.append([[(int(x[0:2]), False), (int(x[3:5]), False), (int(x[6:8]), False), (int(x[9:11]), False), (int(x[12:14]), False)] for x in lines])
        
        winner_grid = None
        winner_number =  None
        for number in bingo_numbers:
            if winner_grid:
                break
            for idx, grid in enumerate(grids):
                if winner_grid:
                    break
                grids[idx] = self.mark_number(grid, number)
                if self.is_winner_grid(grids[idx]):
                    winner_grid = grids[idx]
                    winner_number = number

        yield self.sum_unmarked(winner_grid) * winner_number

    def part2(self, input_data):
        parts = '\n'.join(input_data).split('\n\n')
        bingo_numbers = [int(x) for x in parts[0].split(',')]

        grids = []

        for part in parts[1:]:
            lines = part.split('\n')
            grids.append([[(int(x[0:2]), False), (int(x[3:5]), False), (int(x[6:8]), False), (int(x[9:11]), False), (int(x[12:14]), False)] for x in lines])
        
        winner_grid = None
        winner_number =  None
        won_grids = set()
        for number in bingo_numbers:
            if len(won_grids) == len(grids):
                break
            for idx, grid in enumerate(grids):
                if len(won_grids) == len(grids):
                    break
                grids[idx] = self.mark_number(grid, number)
                if self.is_winner_grid(grids[idx]):
                    won_grids.add(idx)
                    winner_grid = grids[idx]
                    winner_number = number

        yield self.sum_unmarked(winner_grid) * winner_number

    def mark_number(self, grid, number):
        return [[(n, b) if n != number else (n, True) for (n, b) in line] for line in grid]

    def is_winner_grid(self, grid):
        for line in grid:
            winner = True
            for (n, b) in line:
                if b == False:
                    winner = False
                    break
            if winner:
                return True
        
        for x in range(len(grid[0])):
            winner = True
            for line in grid:
                (n, b) = line[x]
                if b == False:
                    winner = False
                    break
            if winner:
                return True
        
        return False
    
    def sum_unmarked(self, grid):
        sum = 0
        for line in grid:
            for (n, b) in line:
                if b == False:
                    sum += n
        
        return sum

