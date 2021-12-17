from common.aocdays import AOCDay, day

DEBUG = True

@day(17)
class Day17(AOCDay):
    test_input = """target area: x=20..30, y=-10..-5""".split("\n")

    target = None

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 45, f'{p1} != 45'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 112, f'{p2} != 112'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        part = input_data[0].split(': ')[1]
        xvalues = part.split(', ')[0].lstrip('x=')
        yvalues = part.split(', ')[1].lstrip('y=')

        x0 = int(xvalues.split('..')[0])
        x1 = int(xvalues.split('..')[1])
        y0 = int(yvalues.split('..')[0])
        y1 = int(yvalues.split('..')[1])
        self.target = (x0 if x0 < x1 else x1, y0 if y0 < y1 else y1, x1 if x1 > x0 else x0, y1 if y1 > y0 else y0)

        successful_shots = []

        for x in range(150):
            for y in range(170):
                shot = self.shoot(x,y)
                if shot is not None:
                    successful_shots.append(shot)
        
        max_y = 0
        for t in successful_shots:
            for (_,y) in t:
                if y > max_y:
                    max_y = y

        yield max_y

    def part2(self, input_data):
        part = input_data[0].split(': ')[1]
        xvalues = part.split(', ')[0].lstrip('x=')
        yvalues = part.split(', ')[1].lstrip('y=')

        x0 = int(xvalues.split('..')[0])
        x1 = int(xvalues.split('..')[1])
        y0 = int(yvalues.split('..')[0])
        y1 = int(yvalues.split('..')[1])
        self.target = (x0 if x0 < x1 else x1, y0 if y0 < y1 else y1, x1 if x1 > x0 else x0, y1 if y1 > y0 else y0)

        successful_shots = []

        for x in range(150):
            for y in range(-170, 170):
                shot = self.shoot(x,y)
                if shot is not None:
                    successful_shots.append(shot)

        yield len(successful_shots)
    
    def shoot(self, x, y):
        trajectory = []
        pos = (0,0)
        trajectory.append(pos)

        miss = False
        hit = False
        while not miss and not hit:
            pos = (pos[0]+x, pos[1]+y)
            trajectory.append(pos)
            if x != 0:
                x = x-1 if x > 0 else x+1
            y -= 1

            if self.target[0] <= pos[0] <= self.target[2] and self.target[1] <= pos[1] <= self.target[3]:
                hit = True
            elif (x == 0 and (pos[0] < self.target[0] or pos[0] > self.target[2])) or (pos[1] < self.target[1]):
                miss = True

        if hit:
            return trajectory
        else:
            return None
