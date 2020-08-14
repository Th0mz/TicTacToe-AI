import pygame
from pygame import gfxdraw

from Player import player1Render, player2Render

_ = None

X = 0
Y = 1
WIDTH = 2
HEIGHT = 3

class Board:
    def __init__(self, player1, player2):
        # Screen
        self.screen_size = (600, 250)
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



    def gameLoop(self):
        """ Main render loop of the game """
        while self.a_correr:

            # Events
            for event in pygame.event.get():
                # Quit program (top right cross clicked)
                if event.type == pygame.QUIT:
                    self.a_correr = False          

            if self.update:
                self.update()
                self.update = False

            if self.player1Turn:
                

        print("saiu")


    def initGUI(self):
        # Init Pygame :
        pygame.init() 
        pygame.font.init()

    def quitGUI(self):
        pygame.quit()
        pygame.font.quit()  

    def update(self):
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



        
        # Background color
        self.screen.fill(backgroundColor)

        renderBoard()
        renderPlayers()

        pygame.display.update()

    def playerMove(self, player):
        # Get play position 
        position = player.playerMove()

        if self.validPosition(position):
            # Update board
            self.board[position[X]][position[Y]] = player.symbol
            self.update = True

            # Passing the turn to the other player
            self.player1Turn = not self.player1Turn

    def validPosition(self, position):
        """ Checks whether the position passed as an argument is valid """
        return self.board[position[X]][position[Y]] == _


    def checkVictory(self):
        return

    def checkTie(self):
        return

    def restartGame(self):
        return