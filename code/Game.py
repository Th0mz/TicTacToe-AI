import pygame
from pygame import gfxdraw

from Player import player1Render, player2Render
from time import sleep

from GameBoard import Board

# Global Variables
X = 0
Y = 1
WIDTH = 2
HEIGHT = 3


class Game:
    def __init__(self, player1, player2):
        # Screen
        self.screen_size = (700, 250)
        self.screen = pygame.display.set_mode(self.screen_size)
        
        # Players
        self.player1 = player1
        self.player2 = player2

        # Board
        self.board = Board(self.screen_size)

        # Game Loop variables
        self.player1Turn = True
        self.running = True

        #  > When true updates the screen
        self.update = True

        # Fonts
        self.initGUI()
        self.winsFont = pygame.font.Font("../assets/winFont.ttf", 20)


    def gameLoop(self):
        """ Main render loop of the game """
        clicked = False
        while self.running:

            # Events
            for event in pygame.event.get():
                # Quit program (top right cross clicked)
                if event.type == pygame.QUIT:
                    self.running = False 

                # Mouse was released
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = True        

            # The player that is playing makes a mov
            playingPlayer = self.player1 if self.player1Turn else self.player2
            otherPlayer = self.player1 if not self.player1Turn else self.player2

            #   > Get play position 
            position = playingPlayer.play(clicked, self.board, otherPlayer)
            self.board.playerMove(playingPlayer, position, self)

            # Updates the screen board with the new player move
            if self.update:
                self.display(self.board)
                self.update = False


            # Cheks if someone won
            winner = self.board.checkVictory(self.board.board)
            if winner != None:
                sleep(0.4)
                if winner == self.player1.symbol:
                    self.player1.wins += 1
                else:
                    self.player2.wins += 1

                self.board.restartGame(self)

            if self.board.checkTie():
                sleep(0.4)
                self.board.restartGame(self)

            clicked = False
        
        self.quitGUI()

    def initGUI(self):
        # Init Pygame :
        pygame.init() 
        pygame.font.init()

        self.player1Symbol = pygame.image.load("../assets/cross.png")

    def quitGUI(self):
        pygame.quit()
        pygame.font.quit()

    def changeTurn(self):
        self.player1Turn = not self.player1Turn

    def updateScreen(self):
        self.update = True

    
    def display(self, board):
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
            linePositions = [(board.size // 3 + board.position[X] - board.lineWeight // 2, board.position[Y], board.lineWeight, board.size), \
                             ((2 * board.size) // 3 + board.position[X] - board.lineWeight // 2, board.position[Y], board.lineWeight, board.size), \
                             (board.position[X], board.size // 3 + board.position[Y] - board.lineWeight // 2, board.size, board.lineWeight), \
                             (board.position[X], (2 * board.size) // 3 + board.position[Y] - board.lineWeight // 2, board.size, board.lineWeight)]

            # Render board
            for position in linePositions:
                rectangle = pygame.Rect(position[X], position[Y], position[WIDTH], position[HEIGHT])
                pygame.draw.rect(self.screen, boardColor, rectangle)

        def renderPlayers():
            """ Renders the plays of the players """
            # Center position of the first place of the board
            firstPos = (board.position[X] + board.size // 6, board.position[Y] + board.size // 6)
            
            for y in range(len(board.board)):
                for x in range(len(board.board[0])):
                    if board.board[y][x] == self.player1.symbol:
                        position = (firstPos[X] + (x * board.size // 3) - self.player1Symbol.get_width() // 2, firstPos[Y] + (y * board.size // 3) - self.player1Symbol.get_height() // 2)
                        player1Render(self.screen, self.player1Symbol, position)
                    elif board.board[y][x] == self.player2.symbol:
                        position = (firstPos[X] + (x * board.size // 3), firstPos[Y] + (y * board.size // 3))
                        player2Render(self.screen, board.size, board.lineWeight, position, player2Color, backgroundColor)
        
        def renderWins():

            winsText = "Wins : {}".format(self.player1.wins)
            text_width, text_height = self.winsFont.size(winsText)

            # Render Player symbol
            player1PositionCenter = (board.position[X] // 2 - 50 // 2, self.screen_size[Y] // 2 - text_height // 2)
            player1PositionCorner = (player1PositionCenter[X] - self.player1Symbol.get_width() // 2, player1PositionCenter[Y] - self.player1Symbol.get_height() // 2)
            player1Render(self.screen, self.player1Symbol, player1PositionCorner)
            # Render text
            player1Wins = self.winsFont.render(winsText, True, player1Color)

            textPosition = (player1PositionCenter[X] -text_width // 2, player1PositionCenter[Y] + 40 - text_height // 2 - 4)
            self.screen.blit(player1Wins, textPosition)
            


            winsText = "Wins : {}".format(self.player2.wins)
            text_width, text_height = self.winsFont.size(winsText)

            # Render Player symbol
            player2Position = (self.screen_size[X] - player1PositionCenter[X], self.screen_size[Y] // 2 - text_height // 2)
            player2Render(self.screen, board.size, board.lineWeight, player2Position, player2Color, backgroundColor)

            # Render text
            player2Wins = self.winsFont.render(winsText, True, player2Color)

            textPosition = (player2Position[X] -text_width // 2, player2Position[Y] + 40 - text_height // 2)
            self.screen.blit(player2Wins, textPosition)
        
        # Background color
        self.screen.fill(backgroundColor)

        renderBoard()
        renderPlayers()
        renderWins()

        pygame.display.update()




