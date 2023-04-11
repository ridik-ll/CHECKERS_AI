import pygame
from copy import deepcopy

RED = (145, 48, 43)
WHITE = (255, 255, 255)

def minimax(position, depth, is_maximizing_player, game):
    """
    Use minimax algorithm to find the best move for the current player.
    """
    if depth == 0:
        return position.evaluate(), position

    player = WHITE if is_maximizing_player else RED
    best_move = None
    best_score = float('-inf') if is_maximizing_player else float('inf')

    for move in get_all_moves(position, player, game):
        score, _ = minimax(move, depth - 1, not is_maximizing_player, game)

        if is_maximizing_player:
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_score, best_move


def simulate_move(piece, move, board, game, skip):
    """
    Simulate a move by moving a piece on a copy of the board.
    """
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    """
    Get all valid moves for a color on the board.
    """
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves
