from typing import DefaultDict
from common.aocdays import AOCDay, day

DEBUG = True

@day(12)
class Day12(AOCDay):
    test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")

    edges = dict()

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 10, f'{p1} != 10'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 36, f'{p2} != 36'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        self.edges = dict()

        for line in input_data:
            n1 = line.split('-')[0]
            n2 = line.split('-')[1]
            if n1 not in self.edges:
                self.edges[n1] = [n2]
            else:
                self.edges[n1].append(n2)
            if n2 not in self.edges:
                self.edges[n2] = [n1]
            else:
                self.edges[n2].append(n1)

        yield self.count_paths('start', [])

    def part2(self, input_data):
        self.edges = dict()

        for line in input_data:
            n1 = line.split('-')[0]
            n2 = line.split('-')[1]
            if n1 not in self.edges:
                self.edges[n1] = [n2]
            else:
                self.edges[n1].append(n2)
            if n2 not in self.edges:
                self.edges[n2] = [n1]
            else:
                self.edges[n2].append(n1)

        yield self.count_paths_2('start', [], None)
    
    def count_paths(self, start_node, path):
        sum = 0
        for neighbor in self.edges[start_node]:
            if neighbor == 'end':
                sum += 1
            elif neighbor in path and neighbor.islower():
                continue
            else:
                sum += self.count_paths(neighbor, path + [start_node])
        return sum
    
    def count_paths_2(self, start_node, path, special_node):
        if special_node == 'start' or special_node == 'end':
            return 0
        
        sum = 0
        for neighbor in self.edges[start_node]:
            if neighbor == 'end':
                sum += 1
            elif neighbor.islower():
                if special_node is None:
                    if neighbor in path:
                        sum += self.count_paths_2(neighbor, path + [start_node], neighbor)
                    else:
                        sum += self.count_paths_2(neighbor, path + [start_node], None)
                else:
                    if special_node == neighbor:
                        if path.count(neighbor) <= 1:
                            sum += self.count_paths_2(neighbor, path + [start_node], neighbor)
                        else:
                            continue
                    else:
                        if neighbor in path:
                            continue
                        else:
                            sum += self.count_paths_2(neighbor, path + [start_node], special_node)
            else:
                sum += self.count_paths_2(neighbor, path + [start_node], special_node)
        return sum
