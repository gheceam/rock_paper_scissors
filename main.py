"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

from game import Game
from player import RandomPlayer, CyclePlayer, ReflectPlayer, HumanPlayer


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
