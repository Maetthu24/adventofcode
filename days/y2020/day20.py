from common.aocdays import AOCDay, day
import numpy as np
import math
from copy import deepcopy

DEBUG = True

@day(20)
class Day20(AOCDay):
    test_input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...""".split("\n")

    tiles = []
    matching_sides_ids = {}
    found_ids = []

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 20899048083289, f'{p1} != 20899048083289'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 273, f'{p2} != 273'

    def part1(self, input_data):
        self.tiles = []
        self.matching_sides_ids = {}
        self.found_ids = []

        for tiledata in '\n'.join(input_data).split('\n\n'):
            lines = tiledata.split('\n')
            id = int(lines[0].split(' ')[1][:-1])

            a = []
            for line in lines[1:]:
                a.append([x for x in line])
            tile = np.array(a)
            sides = self.get_sides(tile)
            self.tiles.append((id, tile, sides))

        result = 1

        for (id, tile, sides) in self.tiles:
            count = 0
            for (id2, _, sides2) in self.tiles:
                if id == id2:
                    continue
                if self.has_matching_side(sides, sides2):
                    count += 1
                    continue
            
            if count not in self.matching_sides_ids:
                self.matching_sides_ids[count] = [id]
            else:
                self.matching_sides_ids[count].append(id)

            if count == 2:
                result *= id

        yield result

    def part2(self, input_data):
        corner_1_id = self.matching_sides_ids[2].pop()
        gridsize = int(math.sqrt(len(self.tiles)))
        image = [[None for _ in range(gridsize)] for _ in range(gridsize)]
        corner_1 = list(filter(lambda x: x[0] == corner_1_id, self.tiles))[0]
        tile_1 = corner_1[1]
        tile_length = len(tile_1[0])

        self.found_ids.append(corner_1_id)

        i = 0
        while True:
            right = self.find_matching_tile(self.get_side(tile_1, 1), 1, self.tiles)
            bottom = self.find_matching_tile(self.get_side(tile_1, 2), 2, self.tiles)
            if (right is None or bottom is None):
                tile_1 = np.rot90(tile_1)
                i += 1
                if i == 4:
                    tile_1 = np.flipud(tile_1)
            else:
                break
        
        right_tile = np.flipud(right[1])
        image[0][0] = tile_1
        image[0][1] = right_tile
        self.found_ids.append(right[0])

        next_side = np.rot90(right_tile)[0]
        for i in range(gridsize):
            if i % 2 == 0:
                r = range(gridsize)
            else:
                r = range(gridsize-1, -1, -1)
            for j in r:
                if (i,j) == (0,0) or (i,j) == (0,1):
                    continue
                
                if (i % 2 == 0 and j == 0) or (i % 2 == 1 and j == gridsize-1):
                    rotatenr = 2
                elif i % 2 == 0:
                    rotatenr = 1
                else:
                    rotatenr = 3
                
                result = self.find_matching_tile(next_side, rotatenr, self.tiles)
                
                if (i % 2 == 0 and j == 0) or (i % 2 == 1 and j == gridsize-1):
                    result_tile = np.flipud(result[1])
                else:
                    result_tile = np.flipud(result[1])
                
                image[i][j] = result_tile
                self.found_ids.append(result[0])

                if (i % 2 == 0 and j == gridsize-1) or (i % 2 == 1 and j == 0):
                    next_side = np.rot90(result_tile, k=2)[0]
                elif i % 2 == 0:
                    next_side = np.rot90(result_tile, k=1)[0]
                else:
                    next_side = np.rot90(result_tile, k=3)[0]

        for i in range(gridsize):
            for j in range(gridsize):
                tile = image[i][j]
                tile = [t[1:tile_length-1] for t in tile][1:tile_length-1]
                image[i][j] = tile
        
        tile_length -=2

        final_image = []
        for line in range(len(image[0]) * tile_length):
            linearray = []
            for i in range(len(image[0])):
                tile = image[line // tile_length][i]
                linearray.extend(tile[line % tile_length])
            final_image.append(linearray)

        for _ in range(8):
            points = self.sea_monster_points(final_image)
            if len(points) == 0:
                final_image = np.rot90(final_image)    
            else:
                count = 0
                for i in range(len(final_image)):
                    for j in range(len(final_image[0])):
                        if final_image[i][j] == '#' and (i,j) not in points:
                            count += 1
                yield count
                return
                
        yield 0

    def sea_monster_points(self, image):
        sea_monster = [
            (1,1),
            (3,0),
            (1,-1),
            (1,0),
            (1,1),
            (3,0),
            (1,-1),
            (1,0),
            (1,1),
            (3,0),
            (1,-1),
            (1,-1),
            (0,1),
            (1,0)
        ]

        points = set()
        for i in range(len(image[0])-20):
            for j in range(1, len(image)-1):
                if image[i][j] != '#':
                    continue
                possible_points = [(i,j)]
                x = i
                y = j
                valid = True
                for (px, py) in sea_monster:
                    x += px
                    y += py
                    if image[x][y] != '#':
                        valid = False
                        break
                    else:
                        possible_points.append((x,y))
                
                if not valid:
                    continue
                else:
                    for p in possible_points:
                        points.add(p)

        return points

    def get_sides(self, tile):
        sides = []
        sides.append(tile[0])
        tile = np.rot90(tile)
        sides.append(tile[0])
        tile = np.rot90(tile)
        sides.append(tile[0])
        tile = np.rot90(tile)
        sides.append(tile[0])
        tile = np.rot90(tile)
        return sides
    
    def has_matching_side(self, sides, sides2):
        for s1 in sides:
            for s2 in sides2:
                if np.array_equal(s1, s2) or np.array_equal(s1, np.flip(s2)):
                    return True
        return False
    
    def find_matching_tile(self, side, rotatenr, tiles):
        for (id, tile, _) in deepcopy(tiles):
            if id in self.found_ids:
                continue
            for _ in range(5):
                s2 = tile[0]
                if np.array_equal(side, s2):
                    return (id, np.rot90(tile, k=rotatenr))
                tile = np.rot90(tile)
            tile = np.flipud(tile)
            for _ in range(5):
                s2 = tile[0]
                if np.array_equal(side, s2):
                    return (id, np.rot90(tile, k=rotatenr))
                tile = np.rot90(tile)
        
        return None
    
    def get_side(self, tile, sidenr):
        assert sidenr in range(4), f'sidenr {sidenr} is invalid (must be in range(0,4))'
        return np.rot90(tile, k=sidenr)[0]

    def print_image(self, image, tile_length):
        print('\n')
        for line in range(len(image[0]) * tile_length):
            linestr = ' | '
            for i in range(len(image[0])):
                tile = image[line // tile_length][i]
                if tile is None:
                    linestr += '           | '
                else:
                    l = tile[line % tile_length]
                    linestr += ''.join(l) + ' | '
            print(f'{linestr}')
            if (line+1) % tile_length == 0:
                print('')
        print('\n')
