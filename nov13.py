# import chess
# import cv2
# import numpy as np


# board=chess.Board()
# board.legal_moves
# print(board.legal_moves)

# board = chess.Board("rnbqbnr/pppppppp/8/8/8/8/PPPkPPPP/RNBQKBNR")
# print(board.is_check())
# print(board)

import chess
import random
board=chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
print(board)
print(list(board.legal_moves))
move_1 = list(board.legal_moves)
# move = chess.Move.from_uci(move_1[0])
board.push(move_1[0])
print(board)
