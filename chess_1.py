import chess
import chess.engine
import cv2
import random
# import chess.pgn
engine = chess.engine.SimpleEngine.popen_uci("stockfish-10-win\Windows\stockfish_10_x64.exe")
board=chess.Board()
while True:
    print()
    print(board)
    move=list(board.legal_moves)     
    print(move)
    board.push(random.choice(move))
         
    limit = chess.engine.Limit(time=0.1)
    engine.play(board, limit)
    
    if board.is_checkmate() is True:
        break
    if board.is_stalemate() is True:
        break
print(board.peek())


engine.quit()
