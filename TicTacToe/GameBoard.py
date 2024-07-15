class GameBoard():
    board = []  # 9 spaces
    playerX = 'X'
    playerO = 'O'

    def __init__(self,board):
        self.board = board

    def makePlay(self, position, player):
        if self.checkAvailable(position):
            self.board[position] = player
        else:
            print("Invalid move")

    def checkAvailable(self, position):
        if self.board[position]['value'] == '':
            return True
        else:
            return False
        
    def checkWinner(self):
        winning_positions =[   
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]]             # diagonals
        for positions in winning_positions: #runs every way
            for position in positions:      #runs every position in every way
                values = [self.board[position]['value']] #Creates "values"
                for value in values:
                    if all(value == self.playerX): #if value equals this
                        return self.playerX #returns the winner
                    elif all(value == self.playerO for value in values):
                        return self.playerO #or this winner
        return False
    
    def printGame(self,board):
        for number in range(9):
            print(board[number]['value']+'|',end='')
            if(number==2 | (number-3)%2==0): 
                print(board[number]['value'])
                print('_______')     
    


    