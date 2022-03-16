#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


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
        if result == 'player1':
            return f"Player 1 wins round {round}!"
        elif result == 'player2':
            return f"Player 2 wins round {round}!"
        else:
            return "It's a tie!"

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
        print(self.round_winner(round, game_result), '\n')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n")
        for round in range(20):
            self.round = round
            print(f"Round {round}:")
            self.play_round(round)
        print(self.final_winner())
        print("\nGame over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
