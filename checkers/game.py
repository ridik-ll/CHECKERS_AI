import pygame
from .constants import red, white, blue, SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
import sys

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = None  # Initialize turn as None
        self.valid_moves = {}
        self.win = win

        # Add code to choose first move
        font = pygame.font.SysFont(None, 30)
        text = font.render("Choose first move: 'r' for red, 'w' for white", True, white)
        text_rect = text.get_rect(center=(WIDTH // 2, 30))
        self.win.blit(text, text_rect)
        pygame.display.update()

        while self.turn is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.turn = white
                    elif event.key == pygame.K_w:
                        self.turn = red

        # Set the turn of the game after choosing first move
        self.change_turn()

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
        winner = self.board.winner(WIN)
        return winner

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
