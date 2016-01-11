import   matplotlib.pyplot as plt
import numpy as np
import random
from Cheesboard import  ChessBoard
from Pieces import King, Rook, Piece
import time
def play_random(board):

    while True:
#        board.draw() 
        piece = None
        moves = None
        move = None
        isValidMove = False 

        while not isValidMove :
        
            if board.turn is Piece.WHITE:
                if random.randint(0,1):
                    # Play King
                    piece = board.get_wking()
                else:
                    # Play Rook
                    piece = board.get_wrook()
            else:
                piece = board.get_bking()

            moves = piece.possible_moves() 
            move = moves[random.randint(0,len(moves)-1)]
            isValidMove =  board.play_move(move[0],move[1],realPiece=piece)
            #time.sleep(1)

        board.update_state()
        board.change_turn()
        if( board.turn == Piece.WHITE):
            board.round += 1
        if board.is_finished():
            #board.draw()
            return board.state




if __name__ == '__main__':
    
    draw = 0
    win = 0
    total = 1000.0
    lit = []
    for t in range(0,10):

        draw = 0
        win = 0
        for i in range(0,int(total)):
            board = ChessBoard.get_random_chessboard()
            if i % 1000 == 0:
                print i
            if play_random(board) is  ChessBoard.DRAW:
                draw += 1
            else:
                win += 1

        lit.append((win,draw))


    print lit
    print np.mean(np.array(lit))
    print np.std(np.array(lit))


