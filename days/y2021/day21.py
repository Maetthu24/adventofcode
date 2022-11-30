from common.aocdays import AOCDay, day

DEBUG = True

@day(21)
class Day21(AOCDay):
    test_input = """Player 1 starting position: 4
Player 2 starting position: 8""".split("\n")

    memory = dict()

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 739785, f'{p1} != 739785'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 444356092776315, f'{p2} != 444356092776315'

    def common(self, input_data):
        yield 0

    def part1(self, input_data):
        pos_1 = int(input_data[0].split(' ')[-1])
        pos_2 = int(input_data[1].split(' ')[-1])

        score_1 = 0
        score_2 = 0

        die = 0

        turn = 1
        moves = 0
        while score_1 < 1000 and score_2 < 1000:
            move = 0
            for _ in range(3):
                die += 1
                if die == 101:
                    die = 1
                move += die
                moves += 1
            if turn == 1:
                pos_1 = (pos_1 + move - 1) % 10 + 1
                score_1 += pos_1
            else:
                pos_2 = (pos_2 + move - 1) % 10 + 1
                score_2 += pos_2
            
            turn = 2 if turn == 1 else 1
        
        losing_score = score_1 if score_2 >= 1000 else score_2

        yield losing_score * moves

    def part2(self, input_data):
        pos_1 = int(input_data[0].split(' ')[-1])
        pos_2 = int(input_data[1].split(' ')[-1])

        score_1 = 0
        score_2 = 0

        wins_1 = 0
        wins_2 = 0

        self.memory = dict()

        for x in range(1,4):
            for y in range(1,4):
                for z in range(1,4):
                    w1, w2 = self.play(pos_1,pos_2,score_1,score_2,x+y+z,1)
                    wins_1 += w1
                    wins_2 += w2
        
        yield max(wins_1, wins_2)
    
    def play(self, pos_1, pos_2, score_1, score_2, move, turn):
        if (pos_1, pos_2, score_1, score_2, move, turn) in self.memory:
            return self.memory[(pos_1, pos_2, score_1, score_2, move, turn)]

        if turn == 1:
            pos_1 = (pos_1 + move - 1) % 10 + 1
            score_1 += pos_1
        else:
            pos_2 = (pos_2 + move - 1) % 10 + 1
            score_2 += pos_2

        if score_1 >= 21:
            self.memory[(pos_1, pos_2, score_1, score_2, move, turn)] = (1,0)
            return (1,0)
        elif score_2 >= 21:
            self.memory[(pos_1, pos_2, score_1, score_2, move, turn)] = (0,1)
            return (0,1)
        else:
            turn = 2 if turn == 1 else 1
            wins1 = 0
            wins2 = 0
            for x in range(1,4):
                for y in range(1,4):
                    for z in range(1,4):
                        m = x+y+z
                        if (pos_1,pos_2,score_1,score_2,m,turn) in self.memory:
                            w1, w2 = self.memory[(pos_1,pos_2,score_1,score_2,m,turn)]
                        else:
                            w1, w2 = self.play(pos_1,pos_2,score_1,score_2,m,turn)
                            self.memory[(pos_1,pos_2,score_1,score_2,m,turn)] = (w1,w2)
                        wins1 += w1
                        wins2 += w2
            
            return (wins1, wins2)
