from os import system
import random
import copy
from colorama import Fore, Back

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']
    P1_TITLE = "Player One"
    P2_TITLE = "Player Two"

    def __init__(self):
        self.their_move_prior = None

    def validate_play(self, play):
        return play.lower() in Player.moves

    def move(self):
        pass

    def learn(self, their_move):
        self.their_move_prior = their_move


class RockPlayer(Player):

    def move(self):
        return 'rock'


class HumanPlayer(Player):

    def move(self):
        play = input(f"What will you play (rock, paper, scissors): ")
        if self.validate_play(play):
            return play
        else:
            print("Please make a valid play....\n")
            return self.move()


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
        self.moves_index = 0

    def move(self):
        result = Player.moves[self.moves_index % 3]
        if self.moves_index > 2:
            self.moves_index = 0
        self.moves_index += 1
        return result


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def winner(self, move1, move2):
        # if both moves are the same its a tie
        if move1 == move2:
            return 'tie'
        if self.beats(move1, move2):
            return f'player1'
        else:
            return f'player2'

    def update_score(self, result):
        if result == 'player1':
            self.p1_score += 1
        elif result == 'player2':
            self.p2_score += 1

    def round_winner(self, round, result):
        sep = "=" * 50
        sep_nl = '\n' + sep + '\n'
        print(sep, Fore.YELLOW)
        # print(Fore.YELLOW)
        if result == 'player1':
            return f"{Player.P1_TITLE} wins round!{Fore.WHITE}{sep_nl}"
        elif result == 'player2':
            return f"{Player.P2_TITLE} wins round!{Fore.WHITE}{sep_nl}"
        else:
            return f"Round is a tie!{Fore.WHITE}{sep_nl}"

    def final_winner(self):
        score1 = self.p1_score
        score2 = self.p2_score
        print(f"Final Score\n{'-' * 20}")
        print(f'{Player.P1_TITLE}: {Fore.BLUE}{score1}{Fore.RESET}')
        print(f'{Player.P2_TITLE}: {Fore.BLUE}{score2}{Fore.RESET}\n')
        print(Fore.GREEN)
        if score1 > score2:
            return f'{Player.P1_TITLE} Wins Game!!{Fore.RESET}'
        elif score1 < score2:
            return f'{Player.P2_TITLE} Wins Game!!{Fore.RESET}'
        elif score1 == score2:
            return f'Game is a Tie'

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        fb = Fore.BLUE
        print(f"{Player.P1_TITLE} played: {fb}{move1}",
              f"\n{Fore.WHITE}{Player.P2_TITLE} played: {fb}{move2}",
              f"{Fore.WHITE}")
        print('-' * 48)
        game_result = self.winner(move1, move2)
        self.update_score(game_result)
        print(f"{Player.P1_TITLE} score: {fb}{self.p1_score}",
              f"\n{Fore.WHITE}{Player.P2_TITLE} score: {fb}{self.p2_score}",
              f"{Fore.WHITE}")
        print(f"{self.round_winner(round, game_result)}")
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play_multiple_rounds(self, num_rounds):
        for round in range(num_rounds):
            self.round = round
            print(f"{Fore.MAGENTA}Round {round+1}{Fore.RESET}")
            print('-' * 48)
            self.play_round(round)

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_game(self):
        system('clear')
        num_rounds = input("How many rounds will be played?: ")
        if num_rounds.isnumeric():
            num_rounds = int(num_rounds)
            system('clear')
            print(f"\n{Fore.GREEN}{Back.WHITE}START GAME",
                  f"\n{Fore.WHITE}{Back.RESET}")
            if num_rounds == 1:
                self.play_round(num_rounds)
            elif num_rounds > 1:
                self.play_multiple_rounds(num_rounds)
            print(self.final_winner())
            print(f"\n{Fore.RED}{Back.WHITE}GAME OVER",
                  f"{Fore.RESET}{Back.RESET}\n")
        else:
            self.play_game()


if __name__ == '__main__':
    game = Game(RandomPlayer(), RockPlayer())
    game.play_game()
