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
            blankPositions = []

            for y in range(len(board.board)):
                for x in range(len(board.board[0])):
                    if board.emptyPosition((x, y)):
                        blankPositions += [(x, y)]

            return blankPositions

        def minimax(board, myTurn, depth):
            player = self if myTurn else otherPlayer
            # Terminal Cases one of them won or was a tie
            winner = board.checkVictory(board.board)
            if winner == self.symbol:
                return 10 - depth

            if winner == otherPlayer.symbol:
                return - 10 + depth
            
            if board.checkTie():
                return 0

            # Otherwise make a move
            scores = []
            for position in allBlankPositions(board):
                # Make the move
                board.board[position[Y]][position[X]] = player.symbol
                # Check the move score
                moveScore = minimax(board, False, depth + 1)
                scores.append(moveScore)

                # Undo the move
                board.board[position[Y]][position[X]] = board.blankSpace

            if myTurn:
                return max(scores)
            else:
                return min(scores)

        
        bestScore = - 9999
        bestMove = (1, 1)

        for position in allBlankPositions(board):
            # Make the move
            board.board[position[Y]][position[X]] = self.symbol
            # Check the move score
            moveScore = minimax(board, False, 0)
            # Undo the move
            board.board[position[Y]][position[X]] = board.blankSpace

            # Check if the moveScore is the best seen until now
            if moveScore > bestScore:
                bestScore = moveScore
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
    
