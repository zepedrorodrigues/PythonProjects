import tkinter as tk
from tkinter import messagebox
from GameBoard import GameBoard
class TicTacToeGUI:
    def __init__(self, root):
        self.game = GameBoard()
        self.root = root
        self.root.title("Tic Tac Toe")
        self.buttons = []
        self.current_player = self.game.playerX
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font='normal 20 bold', width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.game.checkAvailable(index):
            self.game.makePlay(index, self.current_player)
            self.update_button(index)
            winner = self.game.checkWinner()
            if winner:
                self.end_game(winner)
            else:
                self.switch_player()
        else:
            messagebox.showwarning("Invalid move", "This position is already taken!")

    def update_button(self, index):
        self.buttons[index].config(text=self.current_player)

    def switch_player(self):
        self.current_player = self.game.playerO if self.current_player == self.game.playerX else self.game.playerX

    def end_game(self, winner):
        messagebox.showinfo("Game Over", f"The winner is {winner}!")
        self.root.destroy()

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    game_gui = TicTacToeGUI(root)
    root.mainloop()