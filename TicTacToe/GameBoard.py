class GameBoard:
    def __init__(self):
        self.board = ['' for _ in range(9)]
        self.playerX = 'X'
        self.playerO = 'O'

    def makePlay(self, position, player):
        if self.checkAvailable(position):
            self.board[position] = player
        else:
            print("Invalid move")

    def checkAvailable(self, position):
        return self.board[position] == ''

    def checkWinner(self):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for positions in winning_positions:
            values = [self.board[position] for position in positions]
            if values[0] and all(value == values[0] for value in values):
                return values[0]
        return None

    def printGame(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i] or " "} | {self.board[i+1] or " "} | {self.board[i+2] or " "}')
            if i < 6:
                print('---------')
