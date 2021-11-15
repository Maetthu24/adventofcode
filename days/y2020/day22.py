from common.aocdays import AOCDay, day
from collections import deque
from copy import deepcopy

DEBUG = True

@day(22)
class Day22(AOCDay):
    test_input = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 306, f'{p1} != 306'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 291, f'{p2} != 291'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        list1 = '\n'.join(input_data).split('\n\n')[0].split('\n')[1:]
        list2 = '\n'.join(input_data).split('\n\n')[1].split('\n')[1:]
        p1_deck = deque([int(x) for x in list1])
        p2_deck = deque([int(x) for x in list2])

        while not len(p1_deck) == 0 or len(p2_deck) == 0:
            if p1_deck[0] > p2_deck[0]:
                p1_deck.rotate(-1)
                p1_deck.append(p2_deck.popleft())
            else:
                p2_deck.rotate(-1)
                p2_deck.append(p1_deck.popleft())

        deck = p2_deck if len(p1_deck) == 0 else p1_deck
        yield self.deck_score(deck)

    def part2(self, input_data):
        list1 = '\n'.join(input_data).split('\n\n')[0].split('\n')[1:]
        list2 = '\n'.join(input_data).split('\n\n')[1].split('\n')[1:]
        p1_deck = deque([int(x) for x in list1])
        p2_deck = deque([int(x) for x in list2])

        is_1_the_winner = self.play_game(p1_deck, p2_deck)

        yield self.deck_score(p1_deck) if is_1_the_winner else self.deck_score(p2_deck)

    def deck_score(self, deck):
        score = 0
        deck.reverse()
        for i in range(len(deck)):
            score += (i+1) * deck[i]
        return score

    def play_game(self, deck1, deck2):
        history = []

        while self.deck_repr(deck1, deck2) not in history and len(deck1) > 0 and len(deck2) > 0:
            history.append(self.deck_repr(deck1, deck2))

            c1 = deck1.popleft()
            c2 = deck2.popleft()

            if len(deck1) >= c1 and len(deck2) >= c2:
                subdeck1 = deque(deepcopy(list(deck1)[:c1]))
                subdeck2 = deque(deepcopy(list(deck2)[:c2]))
                is_1_the_winner = self.play_game(subdeck1, subdeck2)
            else:
                is_1_the_winner = c1 > c2
            
            if is_1_the_winner:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)

        if self.deck_repr(deck1, deck2) in history:
            return True # Player 1 wins
        
        if len(deck1) == 0:
            return False # Player 2 wins
        else:
            return True # Player 1 wins


    def deck_repr(self, deck1, deck2):
        return ','.join(map(str, deck1)) + '/' + ','.join(map(str, deck2))
