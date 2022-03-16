
class Game:
    # object is passed two player objects at initialization
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # starts the round and prints the round information
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            # plays one round
            self.play_round()
        print("Game over!")
