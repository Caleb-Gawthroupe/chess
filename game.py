"""
@author: Caleb Gawthroupe
"""

import pygame

import board
from pieces import Piece

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (75, 115, 153)
BEIGE = (234, 233, 210)
GREY = (48, 46, 43)

dark_square_color = BLUE
light_square_color = BEIGE

class Visualizer:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.square_height = self.screen.get_height() / 8
        self.indent = (self.screen.get_width()-self.screen.get_height())/2
        pygame.display.set_caption("Chess")

    def draw_board(self):
        """
        Draws the chess board on the screen
        :return:
        """


        for row in range(8):
            for col in range(8):
                rect = pygame.Rect((col*self.square_height)+self.indent,
                                   row*self.square_height,
                                   self.square_height,
                                   self.square_height)
                if (row + col) % 2 == 0: pygame.draw.rect(self.screen, light_square_color, rect)
                if (row + col) % 2 == 1: pygame.draw.rect(self.screen, dark_square_color, rect)

    def draw_piece(self, piece: Piece) -> None:
        """
        Draws the chess piece on the screen
        :param piece: Piece to draw
        :return:
        """
        location = piece.location
        if piece.color == 0: file_name = "w"
        else: file_name = "b"

        file_name = f"{file_name}{piece.name}.svg"

        svg_surface = pygame.image.load(f"assets/{file_name}")
        svg_surface = pygame.transform.scale(svg_surface,
                                        (self.screen.get_height()/8, self.screen.get_height()/8))

        x_pos = (location[1]*self.square_height)+self.indent
        y_pos = (location[0]*self.square_height)


        self.screen.blit(svg_surface, (x_pos, y_pos))

visualizer = Visualizer()
pygame.init()
clock = pygame.time.Clock()
running = True
game_board = board.Board()
game_board.generate_board()
print(game_board)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    visualizer.screen.fill(GREY)
    visualizer.draw_board()
    for piece in game_board.piece_list:
        visualizer.draw_piece(piece)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
