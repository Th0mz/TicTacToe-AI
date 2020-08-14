import pygame
from pygame import gfxdraw

from random import randrange


X = 0
Y = 1

class Player:
    def __init__(self, symbol, name, AI):
        self.symbol = symbol
        self.name = name
        self.wins = 0

        self.AI = AI

    def play(self, clicked, boardSize, boardPosition):
        """ Checks whether the player is AI or not, making 
              his move according to that information  """  

        return self.aiMove() if self.AI else self.playerMove(clicked, boardSize, boardPosition)

    def playerMove(self, clicked, boardSize, boardPosition):
        mousePosition = pygame.mouse.get_pos()
        def insideBoard(position):
            """ Checks if the mouse is inside the board """
            return  boardPosition[X] <= mousePosition[X] <= boardPosition[X] + boardSize and \
                    boardPosition[Y] <= mousePosition[Y] <= boardPosition[Y] + boardSize

        if clicked and insideBoard(mousePosition):
            squareSize = boardSize // 3
            
            x = (mousePosition[X] - boardPosition[X]) // squareSize
            y = (mousePosition[Y] - boardPosition[Y]) // squareSize

            return (x, y)

            
    def aiMove(self):
        # Random approach
        return (randrange(0, 3), randrange(0, 3))



def player2Render(screen, boardSize, boardWeight, position, color, backgroundColor):
    """ Renders a cross on the screen [Player1 symbol] """

    radius = boardSize // 9
    thickness = boardWeight

    # Outside circle                
    gfxdraw.aacircle(screen, position[X], position[Y], \
                     radius, color)

    gfxdraw.filled_circle(screen, position[X], position[Y], \
                          radius, color)

    # Inside Circle
    gfxdraw.aacircle(screen, position[X], position[Y], \
                     radius - thickness, backgroundColor)

    gfxdraw.filled_circle(screen, position[X], position[Y], \
                          radius - thickness, backgroundColor)


def player1Render(screen, boardSize, boardWeight, position, color):
    """ Renders a circle on the screen [Player2 symbol] """
    
    # Size of the squere that contains the player symbol
    squareSize = boardSize // 3
    offset = boardSize // 11
    pygame.draw.line(screen, color, (position[X] - squareSize // 2 + offset, position[Y] - squareSize // 2 + offset), \
                     (position[X] + squareSize // 2 - offset, position[Y] + squareSize // 2 - offset), \
                     boardWeight + 2)

    pygame.draw.line(screen, color, (position[X] + squareSize // 2 - offset, position[Y] - squareSize // 2 + offset), \
                     (position[X] - squareSize // 2 + offset, position[Y] + squareSize // 2 - offset), \
                     boardWeight + 2)
    
