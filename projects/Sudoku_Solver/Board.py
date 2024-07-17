class Board:
    def __init__(self, array):
        self.start_board = array

    def is_safe(self, number, row, column):
        not_in_row = number not in self.start_board[row]
        not_in_column = number not in [self.start_board[i][column] for i in range(9)]
        not_in_square = number not in [self.start_board[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3) for j in
                                       range((column // 3 * 3), (column // 3) * 3 + 3)]
        return not_in_row and not_in_column and not_in_square

    def solve(self, r=0, c=0):
        if r == 9:
            return True
        elif c == 9:
            return self.solve(r + 1, 0)
        elif self.start_board[r][c] != 0:
            return self.solve(r, c + 1)
        else:
            for k in range(1, 10):
                if self.is_safe(k, r, c):
                    self.start_board[r][c] = k
                    if self.solve(r, c + 1):
                        return True
                    self.start_board[r][c] = 0
            return False

    def is_valid_initial(self):
        for row in range(len(self.start_board)):
            for col in range(len(self.start_board[0])):
                num = self.start_board[row][col]
                if num != 0:
                    # Temporarily set the cell to 0 to avoid self-comparison
                    self.start_board[row][col] = 0
                    if not self.is_safe(num, row, col):
                        return False
                    # Restore the cell's value
                    self.start_board[row][col] = num
        return True

    def print_board(self):
        for row in self.start_board:
            print(" ".join(str(cell) for cell in row))