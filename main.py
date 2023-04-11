# import necessary libraries and modules
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, red, white
from checkers.game import Game
from minimax.algorithm import minimax
import sys

# set the frames per second for the game
FPS = 60

# initialize the game window and set its caption
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


# define a function to get the row and column of a square from the mouse position
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# define the main function to run the game
def main():
    # set the game loop flag and create a clock to manage the frame rate
    run = True
    clock = pygame.time.Clock()

    # create a new instance of the Game class
    game = Game(WIN)

    # start the game loop
    while run:
        # set the frame rate
        clock.tick(FPS)

        # use the minimax algorithm to get the best move for the AI player
        if game.turn == white:
            value, new_board = minimax(game.get_board(), 4, white, game)
            game.ai_move(new_board)

        # define a dictionary to map color integers to their names
        COLOR_NAMES = {
            red: 'Red',
            white: 'White'
        }

        # ...

        # check if there is a winner and display a message
        winner = game.winner()
        if winner is not None:
            # map the winner's color integer to its name
            winner_name = COLOR_NAMES[winner]

            # display the winner message
            font = pygame.font.SysFont(None, 60)
            text = font.render(f"{winner_name} wins!", True, red)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WIN.blit(text, text_rect)
            pygame.display.update()

            # wait for the user to close the window
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        # handle user input events
        for event in pygame.event.get():
            # check if the user wants to quit the game
            if event.type == pygame.QUIT:
                run = False

            # check if the user clicked the mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get the row and column of the clicked square and select the piece at that position
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        # update the game display
        game.update()

    # quit pygame when the game loop ends
    pygame.quit()


# run the main function
main()
