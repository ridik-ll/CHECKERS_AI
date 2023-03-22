import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
red = (145, 48, 43)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
grey = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))