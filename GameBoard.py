import pygame
from pygame import gfxdraw

from time import sleep

from Player import player1Render, player2Render

_ = None

X = 0
Y = 1
WIDTH = 2
HEIGHT = 3

class Board:
    def __init__(self, player1, player2):
        # Screen
        self.screen_size = (700, 250)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Board
        self.board = [[_, _, _],
                      [_, _, _],
                      [_, _, _]]
        
        # > Display stats board
        self.boardWeight = 5
        self.boardSize = 180 

        # Centered with the screen
        self.boardPosition = (self.screen_size[X] // 2 - self.boardSize // 2, \
                              self.screen_size[Y] // 2 - self.boardSize // 2  )

        # Players
        self.player1 = player1
        self.player2 = player2

        # Game Loop variables
        self.player1Turn = True
        self.a_correr = True
        
        # When true updates the screen
        self.update = True

        # Fonts
        self.initGUI()
        self.winsFont = pygame.font.SysFont("Comic Sans MS", 20)




    def gameLoop(self):
        """ Main render loop of the game """
        clicked = False
        while self.a_correr:

            # Events
            for event in pygame.event.get():
                # Quit program (top right cross clicked)
                if event.type == pygame.QUIT:
                    self.a_correr = False 

                # Mouse was released
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = True        

            # The player that is playing makes a move
            if self.player1Turn:
                self.playerMove(self.player1, clicked, self.boardSize, self.boardPosition)
            else:
                self.playerMove(self.player2, clicked, self.boardSize, self.boardPosition)

            # Updates the screen board with the new player move
            if self.update:
                self.display()
                self.update = False


            # Cheks if someone won
            winner = self.checkVictory()
            if winner != None:
                sleep(0.5)
                if winner == self.player1.symbol:
                    self.player1.wins += 1
                else:
                    self.player2.wins += 1

                self.restartGame()

            if self.checkTie():
                sleep(0.5)
                self.restartGame()

            clicked = False
        
        self.quitGUI()


    def initGUI(self):
        # Init Pygame :
        pygame.init() 
        pygame.font.init()

    def quitGUI(self):
        pygame.quit()
        pygame.font.quit()  

    def display(self):
        """ Updates the contents of the screen
           [ game board, player status ...] """

        # Colors
        backgroundColor = (20, 189, 172)
        boardColor = (13, 161, 146)
        player1Color = (84, 84, 84)
        player2Color = (242, 235, 211)
        
        def renderBoard():
            """ Renders the tic tac toe board """
            # Position and size of board lines
            linePositions = [(self.boardSize // 3 + self.boardPosition[X] - self.boardWeight // 2, self.boardPosition[Y], self.boardWeight, self.boardSize), \
                             ((2 * self.boardSize) // 3 + self.boardPosition[X] - self.boardWeight // 2, self.boardPosition[Y], self.boardWeight, self.boardSize), \
                             (self.boardPosition[X], self.boardSize // 3 + self.boardPosition[Y] - self.boardWeight // 2, self.boardSize, self.boardWeight), \
                             (self.boardPosition[X], (2 * self.boardSize) // 3 + self.boardPosition[Y] - self.boardWeight // 2, self.boardSize, self.boardWeight)]

            # Render board
            for position in linePositions:
                rectangle = pygame.Rect(position[X], position[Y], position[WIDTH], position[HEIGHT])
                pygame.draw.rect(self.screen, boardColor, rectangle)

        def renderPlayers():
            """ Renders the plays of the players """
            # Center position of the first place of the board
            firstPos = (self.boardPosition[X] + self.boardSize // 6, self.boardPosition[Y] + self.boardSize // 6)
            
            for y in range(len(self.board)):
                for x in range(len(self.board[0])):
                    if self.board[y][x] == self.player1.symbol:
                        position = (firstPos[X] + (x * self.boardSize // 3), firstPos[Y] + (y * self.boardSize // 3))
                        player1Render(self.screen, self.boardSize, self.boardWeight, position, player1Color)
                    elif self.board[y][x] == self.player2.symbol:
                        position = (firstPos[X] + (x * self.boardSize // 3), firstPos[Y] + (y * self.boardSize // 3))
                        player2Render(self.screen, self.boardSize, self.boardWeight, position, player2Color, backgroundColor)
        
        def renderWins():
            # Render Player symbol
            player1Position = (self.boardPosition[X] // 2 - 50, self.screen_size[Y] // 3)
            player1Render(self.screen, self.boardSize, self.boardWeight, player1Position, player1Color)

            # Render text
            winsText = "Wins : {}".format(self.player1.wins)
            player1Wins = self.winsFont.render(winsText, True, (0, 0, 0))

            text_width, text_height = self.winsFont.size(winsText)
            textPosition = (player1Position[X] -text_width // 2, player1Position[Y] + 40 - text_height // 2)
            self.screen.blit(player1Wins, textPosition)
            
            # Render Player symbol
            player2Position = (self.screen_size[X] - player1Position[X], self.screen_size[Y] // 3)
            player2Render(self.screen, self.boardSize, self.boardWeight, player2Position, player2Color, backgroundColor)

            # Render text
            winsText = "Wins : {}".format(self.player2.wins)
            player2Wins = self.winsFont.render(winsText, True, (0, 0, 0))

            text_width, text_height = self.winsFont.size(winsText)
            textPosition = (player2Position[X] -text_width // 2, player2Position[Y] + 40 - text_height // 2)
            self.screen.blit(player2Wins, textPosition)
        
        # Background color
        self.screen.fill(backgroundColor)

        renderBoard()
        renderPlayers()
        renderWins()

        pygame.display.update()

    def playerMove(self, player, clicked, boardSize, boardPosition):
        # Get play position 
        position = player.play(clicked, boardSize, boardPosition)

        if position != None and self.validPosition(position):
            # Update board
            self.board[position[Y]][position[X]] = player.symbol
            self.update = True

            # Passing the turn to the other player
            self.player1Turn = not self.player1Turn

    def validPosition(self, position):
        """ Checks whether the position passed as an argument is valid """
        return self.board[position[Y]][position[X]] == _


    def checkVictory(self):
        """ Check if any of the players won """

        def checkAllRow(board, winner):
            """ Checks all rows """
            if winner == None:
                for row in board:
                    winner = row[0]

                    # Checks if the elements of the row are all the same
                    if winner == row[1] and winner == row[2]:
                        return winner
            else:
                return winner
            
        def checkAllColumn(board, winner):
            """ Checks all columns """
            if winner == None:
                for x in range(len(board[0])):
                    winner = board[0][x]

                    # Checks if the elements of the column are all the same
                    if winner == board[1][x] and winner == board[2][x]:
                        return winner
            else:
                return winner

        def checkAllDiagonal(board, winner):
            """ Checks all diagonals"""
            if winner == None:
                # Check main diagonal
                winner = board[0][0]
                if winner == board[1][1] and winner == board[2][2]:
                    return winner

                # Check secondary diagonal
                winner = board[0][2]
                if winner == board[1][1] and winner == board[2][0]:
                    return winner
            else:
                return winner
        
        # Check victory
        winner = checkAllRow(self.board, None)
        winner = checkAllColumn(self.board, winner)
        winner = checkAllDiagonal(self.board, winner)

        return winner

    def checkTie(self):
        """ Check if it was a tie [has a blank space]"""
        for row in self.board:
            if _ in row:
                return False
        
        return True

    def restartGame(self):
        self.board = [[_, _, _],
                      [_, _, _],
                      [_, _, _]]

        self.update = True