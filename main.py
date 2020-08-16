from Game import Game
from Player import Player

player1 = Player("X", "Player 1", False)
player2 = Player("O", "Player 2", True)

game = Game(player1, player2)

game.gameLoop()
