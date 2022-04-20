# rock_paper_scissors

### Rock Paper Scissors Game
A rock paper scissors game with a retro terminal feel.
You can play as a human player against the computer,
or have two different style computer players go head to head.

Options are to play as:
- Human Player (User controls moves) - `HumanPlayer()`
- Random Player (Computer picks the move) - `RandomPlayer()`
- Rock Player (Computer always plays rock) - `RockPlayer()`
- Cycle Player (Computer plays rock, paper, scisscors in sequence) - `CyclePlayer()`
- Reflect Player (Computer will play the prior move the opponent played) - `ReflectPlayer()`

#### Changing Player Style
Update the 'game' object with any of the above player classes to modify style of play:

```
if __name__ == '__main__':
  game = Game(HumanPlayer(), RandomPlayer())
  game.play_game()
```
