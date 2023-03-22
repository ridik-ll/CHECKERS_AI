import pygame

from .constants import black, rows, cols, red, square_size, white, grey, crown

class Piece:

    padding = 15
    outline = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == red:
            self.direction = -1
        else:
            self.direction = 1
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = square_size * self.col + square_size // 2
        self.y = square_size * self.row + square_size // 2

    def make_king(self):
        self.king = True

    def draw(self, disp):
        radius = square_size//2 - self.padding
        pygame.draw.circle(disp, grey, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(disp, self.color, (self.x, self.y), radius)
        if self.king:
            disp.blit(crown, (self.x - crown.get_width() // 2, self.y - crown.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)




