from GameBoard import Board
from Player import Player

player1 = Player("X", "Player 1", False)
player2 = Player("O", "Player 2", False)

board = Board(player1, player2)

board.initGUI()
board.gameLoop()

board.quitGUI()
