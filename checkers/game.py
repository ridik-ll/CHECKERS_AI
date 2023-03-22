import pygame
from .constants import red, white
from .board import Board

class Game:
    def __init__(self, disp):
        self._init()
        self.disp = disp

    def update(self):
        self.board.draw(self.disp)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = red
        self.valid_move = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self.move(row,col)
            if not result:
                self.selected = None
                self.select(row,col)

        else:
            piece = self.board.get_piece(row,col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_move = self.board.get_valid_moves(piece)

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            reeturn False

        return True

    def change_turn(self):
        if self.turn == red:
            self.turn = white
        else:
            self.turn = red
