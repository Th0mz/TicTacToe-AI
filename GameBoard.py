_ = " "

X = 0
Y = 1

class Board:
    def __init__(self, player1, player2):
        self.board = [[_] * 3] * 3

        self.player1 = player1
        self.player2 = player2


    def gameLoop(self):
        return

    def initGUI(self):
        return

    def endGUI(self):
        return

    def display(self):
        return

    def playerMove(self, player):
        # Get play position 
        position = player.playerMove()
        
        # Update board
        self.board[position[X]][position[Y]] = player.symbol


    def checkVictory(self):
        return

    def restartGame(self):
        return