import pygame
from .constants import black, rows, cols, red, square_size, white
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_king = 0
        self.create_board()

    def draw_squares(self, disp):
        disp.fill(black)
        for row in range(rows):
            for col in range(row % 2, cols, 2):
                pygame.draw.rect(disp, white, (row *square_size, col * square_size, square_size, square_size))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == rows or row == 0:
            piece.make_king()
            if piece.color == white:
                self.white_king += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, white))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, red))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, disp):
        self.draw_squares(disp)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(disp)