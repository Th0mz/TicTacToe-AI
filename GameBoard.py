import pygame
from pygame import gfxdraw

from time import sleep

_ = None

X = 0
Y = 1

class Board:
    def __init__(self, screen_size):

        # Board
        self.board = [[_, _, _],
                      [_, _, _],
                      [_, _, _]]
        
        # > Display stats board
        self.lineWeight = 5
        self.size = 180 

        # Centered with the screen
        self.position = (screen_size[X] // 2 - self.size // 2, \
                         screen_size[Y] // 2 - self.size // 2  )

        self.blankSpace = _


    def playerMove(self, player, position, game):
        """ Given a player and a position makes a move in the 
              board for that player in the position given """

        if position != None and self.emptyPosition(position):
            # Update board
            self.board[position[Y]][position[X]] = player.symbol
            game.updateScreen()

            # Passing the turn to the other player
            game.changeTurn()

    def emptyPosition(self, position):
        """ Checks whether the position passed as an argument is valid """
        return self.board[position[Y]][position[X]] == _


    def checkVictory(self, board):
        """ Check if any of the players won """

        def checkAllRow(board, winner):
            """ Checks all rows """
            if winner == None:
                for row in board:
                    winner = row[0]

                    # Checks if the elements of the row are all the same
                    if winner != None and winner == row[1] and winner == row[2]:
                        return winner
            else:
                return winner
            
        def checkAllColumn(board, winner):
            """ Checks all columns """
            if winner == None:
                for x in range(len(board[0])):
                    winner = board[0][x]

                    # Checks if the elements of the column are all the same
                    if winner != None and winner == board[1][x] and winner == board[2][x]:
                        return winner
            else:
                return winner

        def checkAllDiagonal(board, winner):
            """ Checks all diagonals"""
            if winner == None:
                # Check main diagonal
                winner = board[0][0]
                if winner != None and winner == board[1][1] and winner == board[2][2]:
                    return winner

                # Check secondary diagonal
                winner = board[0][2]
                if winner != None and winner == board[1][1] and winner == board[2][0]:
                    return winner
            else:
                return winner
        
        # Check victory
        winner = checkAllRow(board, None)
        winner = checkAllColumn(board, winner)
        winner = checkAllDiagonal(board, winner)

        return winner

    def checkTie(self):
        """ Check if it was a tie [has a blank space]"""
        for row in self.board:
            if _ in row:
                return False
        
        return True

    def restartGame(self, game):
        self.board = [[_, _, _],
                      [_, _, _],
                      [_, _, _]]

        game.updateScreen()