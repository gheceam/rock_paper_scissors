import random
import copy

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.their_move_prior = None

    def validate_play(self, play):
        return play.lower() in Player.moves

    def move(self):
        pass

    def learn(self, their_move):
        self.their_move_prior = their_move


class HumanPlayer(Player):

    def move(self):
        play = input(f"What will you play (rock, paper, scissors): ")
        if self.validate_play(play):
            return play
        else:
            print("Please make a valid play....\n")
            self.move()


class RandomPlayer(Player):
    def move(self):
        return random.choice(Player.moves)


# ReflectPlayer will play the first round like RandomPlayer,
# once the 1st round is over it will mimic the opponent's prior move
class ReflectPlayer(RandomPlayer):
    def move(self):
        if self.their_move_prior is not None:
            return self.their_move_prior
        else:
            return RandomPlayer.move(self)


class CyclePlayer(Player):
    def __init__(self):
        self.moves = []
        self.refresh_moves()

    def move(self):
        if len(self.moves) == 1:
            choice = self.get_choice()
            self.refresh_moves()
            return choice
        else:
            return self.get_choice()

    def get_choice(self):
        index = random.randint(0, len(self.moves)-1)
        choice = self.moves.pop(index)
        return choice

    def refresh_moves(self):
        self.moves = copy.deepcopy(Player.moves)
        random.shuffle(self.moves)
