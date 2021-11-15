from common.aocdays import AOCDay, day
from copy import deepcopy

DEBUG = True

@day(24)
class Day24(AOCDay):
    test_input = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split("\n")

    directions = {
        'e': (2, 0),
        'se': (1, 1),
        'sw': (-1, 1),
        'w': (-2, 0),
        'nw': (-1, -1),
        'ne': (1, -1)
    }

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 10, f'{p1} != 10'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 2208, f'{p2} != 2208'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        flipped_tiles = []

        for line in input_data:
            target_tile = self.move_to_tile(line)
            if target_tile in flipped_tiles:
                flipped_tiles.remove(target_tile)
            else:
                flipped_tiles.append(target_tile)

        yield len(flipped_tiles)

    def part2(self, input_data):
        flipped_tiles = {}

        for line in input_data:
            (x, y) = self.move_to_tile(line)
            if x not in flipped_tiles:
                flipped_tiles[x] = [y]
            elif y not in flipped_tiles[x]:
                flipped_tiles[x].append(y)
            else:
                flipped_tiles[x].remove(y)

        for _ in range(100):
            new_flipped = deepcopy(flipped_tiles)
            checked = set()
            for (x, ys) in flipped_tiles.items():
                for y in ys:
                    if (x, y) in checked:
                        continue
                    checked.add((x, y))
                    fn = self.flipped_neighbours(flipped_tiles, (x, y))
                    if fn == 0 or fn > 2:
                        new_flipped[x].remove(y)
                    
                    for neighbour in self.neighbours((x, y)):
                        if (neighbour[0], neighbour[1]) in checked or neighbour[0] in flipped_tiles and neighbour[1] in flipped_tiles[neighbour[0]]:
                            continue
                        checked.add((neighbour[0], neighbour[1]))
                        fn = self.flipped_neighbours(flipped_tiles, (neighbour[0], neighbour[1]))
                        if fn == 2:
                            if neighbour[0] not in new_flipped:
                                new_flipped[neighbour[0]] = [neighbour[1]]
                            else:
                                new_flipped[neighbour[0]].append(neighbour[1])
            
            flipped_tiles = new_flipped

        yield self.flipped_count(flipped_tiles)

    def move_to_tile(self, instruction):
        x = 0
        y = 0
        while len(instruction) > 0:
            for (k, v) in self.directions.items():
                if instruction.startswith(k):
                    x += v[0]
                    y += v[1]
                    instruction = instruction[len(k):]
                    break

        return (x, y)

    def neighbours(self, tile):
        neighbours = []
        x = tile[0]
        y = tile[1]
        for dir in self.directions.values():
            neighbours.append((x+dir[0], y+dir[1]))
        return neighbours

    def flipped_neighbours(self, tiles, tile):
        count = 0
        x = tile[0]
        y = tile[1]
        for dir in self.directions.values():
            if x+dir[0] in tiles and y+dir[1] in tiles[x+dir[0]]:
                count += 1
        return count

    def flipped_count(self, tiles):
        count = 0
        for ys in tiles.values():
            count += len(ys)
        return count