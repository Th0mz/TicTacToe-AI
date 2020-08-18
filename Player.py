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

    def play(self, clicked, board, otherPlayer):
        """ Checks whether the player is AI or not, making 
              his move according to that information  """  

        return self.aiMove(board, otherPlayer) if self.AI else self.playerMove(clicked, board.size, board.position)

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

    def aiMove(self, board, otherPlayer):
        """ Choosing the best move using the minimax algorithm """
        def allBlankPositions(board):
            """ Returns all positions that the player can play """
            blankPositions = []

            for y in range(len(board.board)):
                for x in range(len(board.board[0])):
                    if board.emptyPosition((x, y)):
                        blankPositions += [(x, y)]
            
            return blankPositions

        def minimax(board, depth, myTurn):
            """ Minimax algorithm that finds the move with the best score """

            # Score Values for each terminal state
            scores = {self.symbol : 1,
                      otherPlayer.symbol : -1,
                      "Tie" : 0}
            
            # > Terminal States (one of the players win or its a tie)
            winner = board.checkVictory(board.board)
            if winner != None:
                return scores[winner]

            if board.checkTie():
                return scores["Tie"]

            # If its not a terminal state find all the possible moves and rate them
            if myTurn:
                bestScore = -999
                for position in allBlankPositions(board):
                    # Choose a free position and play in it
                    board.board[position[Y]][position[X]] = self.symbol
                    # Calculate the score of that move
                    score = minimax(board, depth+1, not myTurn)
                    # Undo the move
                    board.board[position[Y]][position[X]] = board.blankSpace
                    bestScore = max(score, bestScore)
                
                return bestScore
            else:
                bestScore = 999
                for position in allBlankPositions(board):
                    # Choose a free position and play in it
                    board.board[position[Y]][position[X]] = otherPlayer.symbol
                    # Calculate the score of that move
                    score = minimax(board, depth+1, not myTurn)
                    # Undo the move
                    board.board[position[Y]][position[X]] = board.blankSpace
                    bestScore = min(score, bestScore)
                
                return bestScore

 

        bestScore = -999
        bestMove = (0, 0)

        for position in allBlankPositions(board):
            # Choose a free position and play in it
            board.board[position[Y]][position[X]] = self.symbol
            # Calculate the score of that move
            score = minimax(board, 0, False)
            # Undo the move
            board.board[position[Y]][position[X]] = board.blankSpace
            
            if score > bestScore:
                bestScore = score
                bestMove = position

        return bestMove

        # Random approach
        #return (randrange(0, 3), randrange(0, 3))



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


def player1Render(screen, image, position):
    screen.blit(image, position)

def player1Renderr(screen, boardSize, boardWeight, position, color):
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
    
