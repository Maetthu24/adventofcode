from functools import reduce
from common.aocdays import AOCDay, day
import math

DEBUG = True

@day(16)
class Day16(AOCDay):
    ti1 = """8A004A801A8002F478""".split("\n")
    ti2 = """620080001611562C8802118E34""".split("\n")
    ti3 = """C0015000016115A2E0802F182340""".split("\n")
    ti4 = """A0016C880162017C3686B18A3D4780""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.ti1).__next__()
        assert p1 == 16, f'{p1} != 16'
        
        p2 = self.part1(self.ti2).__next__()
        assert p2 == 12, f'{p2} != 12'

        p3 = self.part1(self.ti3).__next__()
        assert p3 == 23, f'{p3} != 23'

        p4 = self.part1(self.ti4).__next__()
        assert p4 == 31, f'{p4} != 31'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        binary = ''.join([bin(int(x, 16))[2:].zfill(4) for x in input_data[0]])
        packets = self.decode_packets(binary)
        yield packets[0].version_sum()

    def part2(self, input_data):
        binary = ''.join([bin(int(x, 16))[2:].zfill(4) for x in input_data[0]])
        packets = self.decode_packets(binary)
        yield packets[0].value()
    
    def decode_packets(self, binary):
        if len(binary) == 0 or binary.find('1') == -1:
            return []

        idx = 0
        version = int(binary[idx:idx+3], 2)
        idx += 3
        type_id = int(binary[idx:idx+3], 2)
        idx += 3

        if type_id == 4: # literal value
            literal = ''
            has_next = True
            while has_next:
                if binary[idx] == '0':
                    has_next = False
                literal += binary[idx+1:idx+5]
                idx += 5

            literal = int(literal, 2)
            p = Packet(version, type_id, [], literal)
            return [p] + self.decode_packets(binary[idx:])
                

        else: # operator value
            length_type_id = binary[idx]
            idx += 1
            if length_type_id == '0':
                l = int(binary[idx:idx+15], 2)
                idx += 15
                # subpackets are in binary[23:23+l]
                p = Packet(version, type_id, self.decode_packets(binary[idx:idx+l]), None)
                return [p] + self.decode_packets(binary[idx+l:])

            elif length_type_id == '1':
                n = int(binary[idx:idx+11], 2)
                idx += 11
                # binary[19:.....] contains n subpackets
                
                packets = self.decode_packets(binary[idx:])
                p = Packet(version, type_id, packets[:n], None)
                return [p] + packets[n:]
            else:
                print('Should not happen!')

class Packet:
    def __init__(self, version, type_id, subpackets, literal):
        self.version = version
        self.type_id = type_id
        self.subpackets = subpackets
        self.literal = literal

    def version_sum(self):
        return self.version + sum(map(lambda p: p.version_sum(), self.subpackets))

    def value(self):
        if self.type_id == 4:
            return self.literal
        elif self.type_id == 0:
            return sum(self.subvalues())
        elif self.type_id == 1:
            return math.prod(self.subvalues())
        elif self.type_id == 2:
            return min(self.subvalues())
        elif self.type_id == 3:
            return max(self.subvalues())
        elif self.type_id == 5:
            return 1 if self.subpackets[0].value() > self.subpackets[1].value() else 0
        elif self.type_id == 6:
            return 1 if self.subpackets[0].value() < self.subpackets[1].value() else 0
        elif self.type_id == 7:
            return 1 if self.subpackets[0].value() == self.subpackets[1].value() else 0
    
    def subvalues(self):
        return list(map(lambda p: p.value(), self.subpackets))