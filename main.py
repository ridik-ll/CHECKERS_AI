import pygame
from checkers.constants import width, height, square_size
from checkers.board import Board
FPS = 60

disp = pygame.display.set_mode((width, height))


pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // square_size
    col = x // square_size
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(disp)
        pygame.display.update()


main()