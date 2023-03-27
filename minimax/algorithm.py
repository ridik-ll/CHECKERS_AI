from copy import deepcopy
import pygame

red = (145, 48, 43)
white = (255, 255, 255)


def minimax(position, depth, max_player, game):
    if depth == 0:
        return position.evaluate(), position

    player = white if max_player else red
    best_move = None
    best_score = float('-inf') if max_player else float('inf')

    for move in get_all_moves(position, player, game):
        score, _ = minimax(move, depth - 1, not max_player, game)

        if max_player:
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_score, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves



