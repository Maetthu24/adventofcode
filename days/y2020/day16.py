from common.aocdays import AOCDay, day

DEBUG = True

@day(16)
class Day16(AOCDay):
    test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 71, f'{p1} != 71'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')

        fields = {}
        for row in input_data[0].split('\n'):
            name = row.split(': ')[0]
            ranges = []
            for r in row.split(': ')[1].split(' or '):
                ranges.append(range(int(r.split('-')[0]), int(r.split('-')[1]) + 1))
            fields[name] = ranges

        invalid_sum = 0

        for row in input_data[2].split('\n')[1:]:
            numbers = [int(x) for x in row.split(',')]
            for n in numbers:
                valid = False
                for ranges in fields.values():
                    for r in ranges:
                        if n in r:
                            valid = True
                            break
                
                if not valid:
                    invalid_sum += n

        yield invalid_sum


    def part2(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')

        fields = {}
        for row in input_data[0].split('\n'):
            name = row.split(': ')[0]
            ranges = []
            for r in row.split(': ')[1].split(' or '):
                ranges.append(range(int(r.split('-')[0]), int(r.split('-')[1]) + 1))
            fields[name] = ranges

        valid_tickets = []

        for row in input_data[2].split('\n')[1:]:
            numbers = [int(x) for x in row.split(',')]
            valid_ticket = True
            for n in numbers:
                valid = False
                for ranges in fields.values():
                    for r in ranges:
                        if n in r:
                            valid = True
                            break
                
                if not valid:
                    valid_ticket = False
                    break
            
            if valid_ticket:
                valid_tickets.append(numbers)

        remaining_fields = list(fields.keys())

        field_assignments = {}

        while len(field_assignments) < len(fields):
            possible_names = [[] for x in range(len(fields))]

            for i in range(len(valid_tickets[0])):
                numbers = [x[i] for x in valid_tickets]
                
                possible = []
                for name in remaining_fields:
                    ranges = fields[name]
                    is_possible = True
                    for n in numbers:
                        pos = False
                        for r in ranges:
                            if n in r:
                                pos = True
                                break
                        
                        if not pos:
                            is_possible = False
                            break
                    
                    if is_possible:
                        possible.append(name)
            
                possible_names[i] = possible

            for i in range(len(possible_names)):
                if len(possible_names[i]) == 1:
                    found = possible_names[i][0]
                    field_assignments[found] = i
                    remaining_fields.remove(found)

                    break
            
        product = 1

        my_ticket = [int(x) for x in input_data[1].split('\n')[1].split(',')]

        for k, v in field_assignments.items():
            if 'departure' in k:
                product *= my_ticket[v]

        yield product
