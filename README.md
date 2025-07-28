# Tic-Tac-Toe-game.py
A simple Python GUI Tic-Tac-Toe game where you play against a basic AI. Built using Tkinter.

## Features

- Play as "X" against the computer ("O")
- Smart AI: tries to win or block your moves
- Detects win, loss, or draw
- Restart option after each game

## Requirements

- Python 3.x
Tkinter comes pre-installed with most Python distributions.

## How to Run

1. Save the code as `tictakgame.py`.
2. Open a terminal and navigate to the file's directory.
3. Run:

   ```sh
   python tictakgame.py
   ```

## How to Play

- Click on any empty square to make your move.
- The AI will respond automatically.  
- The game ends when someone wins or it's a draw.
- Click "Restart" to play again.

  Tic-Tac-Toe game is a Python application using the Tkinter library for the graphical user interface. Here’s a breakdown of how it works:

## Features
1.Player vs AI: You play as "X", and the computer (AI) plays as "O".
2.Graphical Board: The board is a 3x3 grid of buttons.
3.AI Logic: The AI tries to win if possible, blocks your winning moves, or picks a random empty spot.
4.Game End: The game announces if you win, the AI wins, or if it’s a draw. You can restart the game.
## How it Works
1.Initialization:
The TicTacToeAI class sets up the window, board, and buttons.

2.Player Move:
When you click a button, human_move is called. If the spot is empty, it marks "X" and checks for a win or draw. If the game continues, the AI moves after a short delay.

3.AI Move:
The AI checks if it can win in the next move. If not, it tries to block you. If neither is possible, it picks a random empty spot.

4.Win/Draw Check:
After each move, check_winner checks all possible winning combinations.

5.Game Over:
If someone wins or it’s a draw, a message is shown and a restart button appears.
6.Restart:
Clicking "Restart" resets the board and removes the result message.
