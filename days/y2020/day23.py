from common.aocdays import AOCDay, day

DEBUG = True

@day(23)
class Day23(AOCDay):
    test_input = """389125467"""

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == '67384529', f'{p1} != "67384529"'

        # p2 = self.part2(self.test_input).__next__()
        # assert p2 == 149245887792, f'{p2} != 149245887792'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        circle = deque([int(x) for x in input_data])
        
        current = circle[0]
        for i in range(100):
            print(f'-- move {i+1} --')

            cups = 'cups: '
            for n in circle:
                if n == current:
                    cups += f'({n})'
                else:
                    cups += f' {n} '
            print(cups)

            circle.rotate(-1)

            removed = [circle.popleft(), circle.popleft(), circle.popleft()]

            print(f'pick up: {removed[0]}, {removed[1]}, {removed[2]}')
            
            destination = current - 1
            while destination in removed:
                destination -= 1
            if destination not in circle:
                destination = max(circle)
            
            print(f'destination: {destination}\n')

            destination_idx = circle.index(destination)
            circle.insert(destination_idx+1, removed[0])
            circle.insert(destination_idx+2, removed[1])
            circle.insert(destination_idx+3, removed[2])

            current = circle[0]

        circle.rotate(-(circle.index(1)+1))
        yield ''.join([str(x) for x in list(circle)[:-1]])

    def part2(self, input_data):
        circle = [int(x) for x in input_data]
        circle.extend(list(range(10, 1000001)))

        ll = [0] * 1000001
        for i in range(len(circle)):
            if i == len(circle) - 1:
                ll[circle[i]] = circle[0]
            else:
                ll[circle[i]] = circle[i+1]

        current = circle[0]
        for i in range(10000000):
            if i % 10000 == 0:
                print(f'{i // 10000}/1000 of moves done')
            
            a = ll[current]
            b = ll[a]
            c = ll[b]

            ll[current] = ll[c]

            destination = current - 1
            while destination in [a, b, c]:
                destination -= 1
                if destination < 1:
                    destination = max(circle)

            temp = ll[destination]
            ll[destination] = a
            ll[c] = temp

            current = ll[current]

        yield ll[1] * ll[ll[1]]
