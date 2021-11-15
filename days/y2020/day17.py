from common.aocdays import AOCDay, day
from copy import deepcopy

DEBUG = True

@day(17)
class Day17(AOCDay):
    test_input = """.#.
..#
###""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 112, f'{p1} != 112'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 848, f'{p2} != 848'

    def part1(self, input_data):
        active = {}
        for x in range(len(input_data)):
            line = input_data[x]
            for y in range(len(line)):
                if line[y] == '#':
                    if x not in active:
                        active[x] = {y: [0]}
                    else:
                        active[x][y] = [0]

        for _ in range(6):
            new_active = deepcopy(active)
            checked = set()
            for (x, ys) in active.items():
                for (y, zs) in ys.items():
                    for z in zs:
                        if (x,y,z) in checked:
                            continue
                        checked.add((x,y,z))
                        an = self.active_neighbours(active, (x,y,z))
                        if an not in range(2,4):
                            new_active[x][y].remove(z)
                        
                        for n in self.get_neighbours((x,y,z)):
                            if (n in checked) or (n[0] in active and n[1] in active[n[0]] and n[2] in active[n[0]][n[1]]):
                                continue
                            checked.add(n)
                            an = self.active_neighbours(active, n)
                            if an == 3:
                                if n[0] not in new_active:
                                    new_active[n[0]] = {n[1]: [n[2]]}
                                else:
                                    if n[1] not in new_active[n[0]]:
                                        new_active[n[0]][n[1]] = [n[2]]
                                    else:
                                        new_active[n[0]][n[1]].append(n[2])

            active = new_active

        count = 0
        for ys in active.values():
            for zs in ys.values():
                count += len(zs)

        yield count

    def part2(self, input_data):
        active = {}
        for x in range(len(input_data)):
            line = input_data[x]
            for y in range(len(line)):
                if line[y] == '#':
                    if x not in active:
                        active[x] = {y: {0: [0]}}
                    else:
                        active[x][y] = {0: [0]}

        for _ in range(6):
            new_active = deepcopy(active)
            checked = set()
            for (x, ys) in active.items():
                for (y, zs) in ys.items():
                    for (z, ws) in zs.items():
                        for w in ws:
                            if (x,y,z,w) in checked:
                                continue
                            checked.add((x,y,z,w))
                            an = self.active_neighbours_2(active, (x,y,z,w))
                            if an not in range(2,4):
                                new_active[x][y][z].remove(w)
                            
                            for n in self.get_neighbours_2((x,y,z,w)):
                                if (n in checked) or (n[0] in active and n[1] in active[n[0]] and n[2] in active[n[0]][n[1]] and n[3] in active[n[0]][n[1]][n[2]]):
                                    continue
                                checked.add(n)
                                an = self.active_neighbours_2(active, n)
                                if an == 3:
                                    if n[0] not in new_active:
                                        new_active[n[0]] = {n[1]: {n[2]: [n[3]]}}
                                    else:
                                        if n[1] not in new_active[n[0]]:
                                            new_active[n[0]][n[1]] = {n[2]: [n[3]]}
                                        else:
                                            if n[2] not in new_active[n[0]][n[1]]:
                                                new_active[n[0]][n[1]][n[2]] = [n[3]]
                                            else:
                                                new_active[n[0]][n[1]][n[2]].append(n[3])

            active = new_active

        yield self.count_active(active)

    def active_neighbours(self, active, point):
        count = 0
        for n in self.get_neighbours(point):
            if n[0] in active and n[1] in active[n[0]] and n[2] in active[n[0]][n[1]]:
                count += 1
        return count
    
    def active_neighbours_2(self, active, point):
        count = 0
        for n in self.get_neighbours_2(point):
            if n[0] in active and n[1] in active[n[0]] and n[2] in active[n[0]][n[1]] and n[3] in active[n[0]][n[1]][n[2]]:
                count += 1
        return count

    def get_neighbours(self, point):
        neighbours = []
        
        for x in range(point[0]-1, point[0]+2):
            for y in range(point[1]-1, point[1]+2):
                for z in range(point[2]-1, point[2]+2):
                    if (x,y,z) == point:
                        continue
                    neighbours.append((x,y,z))

        return neighbours

    def get_neighbours_2(self, point):
        neighbours = []
        
        for x in range(point[0]-1, point[0]+2):
            for y in range(point[1]-1, point[1]+2):
                for z in range(point[2]-1, point[2]+2):
                    for w in range(point[3]-1, point[3]+2):
                        if (x,y,z,w) == point:
                            continue
                        neighbours.append((x,y,z,w))

        return neighbours

    def count_active(self, active):
        count = 0
        for ys in active.values():
            for zs in ys.values():
                for ws in zs.values():
                    count += len(ws)
        return count
