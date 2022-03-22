#!/usr/bin/env python3
import random
from os import system
import copy

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


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

"""
ReflectPlayer will play the first round like RandomPlayer,
once the 1st round is over it will mimic the opponent's prior move
"""
class ReflectPlayer(RandomPlayer):
    def move(self):
        if self.their_move_prior != None:
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
            index = random.randint(0,len(self.moves)-1)
            choice = self.moves.pop(index)
            return choice

    def refresh_moves(self):
        self.moves =  copy.deepcopy(Player.moves)
        random.shuffle(self.moves)
    
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


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
        if beats(move1, move2):
            return 'player1'
        else:
            return 'player2'

    def update_score(self, result):
        if result == 'player1':
            self.p1_score += 1
        elif result == 'player2':
            self.p2_score += 1

    def round_winner(self, round, result):
        separator = "=" * 50
        separator_newline = '\n' + separator + '\n'
        print(separator)
        if result == 'player1':
            return f"Player 1 wins round!{separator_newline}".upper()
        elif result == 'player2':
            return f"Player 2 wins round!{separator_newline}".upper()
        else:
            return f"It's a tie!{separator_newline}".upper()

    def final_winner(self):
        score1 = self.p1_score
        score2 = self.p2_score

        if score1 > score2:
            return 'Player 1 wins!!'
        elif score1 < score2:
            return 'Player 2 wins!'
        elif score1 == score2:
            return f'It\'s a tie'

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        game_result = self.winner(move1, move2)
        self.update_score(game_result)
        print(self.round_winner(round, game_result))
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play_game(self):

        system('clear')

        print("Game start!\n")
        for round in range(9):
            self.round = round
            print(f"Round {round}:")
            print('-' * 48)
            self.play_round(round)

        print(self.final_winner())
        print("\nGame over!\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
