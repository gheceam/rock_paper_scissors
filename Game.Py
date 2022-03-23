from os import system


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
            return f"Round is a tie!{separator_newline}".upper()

    def final_winner(self):
        score1 = self.p1_score
        score2 = self.p2_score
        print('The final score is:')
        print(f'PLAYER 1 with: {score1}')
        print(f'PLAYER 2 with: {score2}\n')
        if score1 > score2:
            return f'PLAYER 1 Wins!!'
        elif score1 < score2:
            return 'PLAYER 2 Wins!!'
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

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_game(self):
        system('clear')
        num_rounds = int(input("How many rounds will be played?: "))
        system('clear')
        print("Start Game!\n")
        for round in range(num_rounds):
            self.round = round
            print(f"Round {round+1}:")
            print('-' * 48)
            self.play_round(round)

        print(self.final_winner())
        print("\n!!!GAME OVER!!!\n")
