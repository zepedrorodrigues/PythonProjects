import tkinter as tk
from tkinter import messagebox
from Board import Board

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.board_frame, width=2, font=("Arial", 24), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.entries[row][col] = entry

    def create_buttons(self):
        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        self.solve_button.pack(pady=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid)
        self.clear_button.pack(pady=10)

    def get_board(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                value = self.entries[row][col].get()
                if value.isdigit():
                    current_row.append(int(value))
                else:
                    current_row.append(0)
            board.append(current_row)
        return board

    def solve_puzzle(self):
        board = self.get_board()
        sudoku_board = Board(board)
        if not sudoku_board.is_valid_initial():
            messagebox.showerror("Error", "The initial board configuration is invalid.")
            return

        if sudoku_board.solve():
            self.display_solution(sudoku_board.start_board)
        else:
            messagebox.showerror("Error", "No solution exists for the given puzzle")

    def display_solution(self, solution):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, solution[row][col])

    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
