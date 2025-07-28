

import tkinter as tk
import random

class TicTacToeAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe vs AI")
        self.board = [" "]*9
        self.buttons = []
        self.create_board()
        self.game_over = False

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Helvetica", 32), width=5, height=2,
                               command=lambda i=i: self.human_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def human_move(self, index):
        if self.board[index] == " " and not self.game_over:
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_winner("X"):
                self.end_game("You win!")
            elif " " not in self.board:
                self.end_game("It's a draw!")
            else:
                self.root.after(500, self.ai_move)  # Delay for realism

    def ai_move(self):
        index = self.best_move()
        self.board[index] = "O"
        self.buttons[index].config(text="O")
        if self.check_winner("O"):
            self.end_game("AI wins!")
        elif " " not in self.board:
            self.end_game("It's a draw!")

    def best_move(self):
        # Win if possible
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                if self.check_winner("O"):
                    self.board[i] = " "
                    return i
                self.board[i] = " "
        # Block if player can win
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "X"
                if self.check_winner("X"):
                    self.board[i] = " "
                    return i
                self.board[i] = " "
        return random.choice([i for i in range(9) if self.board[i] == " "])

    def check_winner(self, player):
        win_combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for combo in win_combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def end_game(self, result):
        self.game_over = True
        result_label = tk.Label(self.root, text=result, font=("Helvetica", 24))
        result_label.grid(row=3, column=0, columnspan=3)
        restart_button = tk.Button(self.root, text="Restart", command=self.reset)
        restart_button.grid(row=4, column=0, columnspan=3)

    def reset(self):
        self.board = [" "]*9
        for button in self.buttons:
            button.config(text=" ")
        self.game_over = False
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.destroy()

root = tk.Tk()
game = TicTacToeAI(root)
root.mainloop()