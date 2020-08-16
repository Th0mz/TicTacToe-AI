from GameBoard import Board
from Player import Player

player1 = Player("X", "Player 1", False)
player2 = Player("O", "Player 2", True)

board = Board(player1, player2)

board.gameLoop()
