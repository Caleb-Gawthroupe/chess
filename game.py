"""
@author: Caleb Gawthroupe
"""

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (75, 115, 153)
BEIGE = (234, 233, 210)
GREY = (48, 46, 43)

dark_square_color = BLUE
light_square_color = BEIGE

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
running = True

def draw_board(screen):
    """
    Draws the chess board on the screen
    :param screen:
    :return:
    """
    height = screen.get_height() / 8
    indent = (screen.get_width()-screen.get_height())/2

    for row in range(8):
        for col in range(8):
            rect = pygame.Rect((col*height)+indent, row*height, height, height)
            if (row + col) % 2 == 0: pygame.draw.rect(screen, light_square_color, rect)
            if (row + col) % 2 == 1: pygame.draw.rect(screen, dark_square_color, rect)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(GREY)
    draw_board(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
