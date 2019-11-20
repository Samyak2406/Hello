# import chess
# import chess.engine
# import cv2

# import random
# board=chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
# print(board)
# print(list(board.legal_moves))
# while True:
#     move_1 = list(board.legal_moves)
#     board.push(random.choice(move_1))
# #board.pop()
#     print(board)
#     print()
#     print()
#     print()
#     cv2.waitKey(1800)
# the above code is  for random movement of chess elements



import chess
import chess.engine
import cv2
import random
engine = chess.engine.SimpleEngine.popen_uci("stockfish-10-win\Windows\stockfish_10_x64.exe")
board=chess.Board()
while True:
    print()
    print(board)
    move=list(board.legal_moves)     
    board.push(random.choice(move))
    print()
    # for i in move:
    #     if i==board.peek()
    #         print('perfect')

    if board.is_checkmate() is True:
        break


#limit = chess.engine.Limit(time=2.0)
#engine.play(board,limit)
engine.quit()
