import pygame
from .constants import red, white, blue, SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = red
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self.__init__(self.win)

    def select(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        elif self.selected:
            if self._move(row, col):
                self.change_turn()
            self.selected = None
            return True
        return False

    def _move(self, row, col):
        if (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            return True
        return False

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, blue,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        self.turn = white if self.turn == red else red

    def winner(self):
        return self.board.winner(WIN)

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()