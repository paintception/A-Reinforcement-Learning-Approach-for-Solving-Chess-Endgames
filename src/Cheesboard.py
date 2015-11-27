
__author__ = 'yaron'
import sys
from Pieces import King, Rook, Piece
import random

class ChessBoard:
    NOTHING = 'PLAYING'
    BLACK_KING_CHECKED = 'BLACK_KING_CHECKED'
    BLACK_KING_CHECKMATE = 'BLACK_KING_CHECKMATE'
    DRAW = 'DRAW'

    def __init__(self,turn=Piece.WHITE, debug=None):
        self.pieces = []
        self.num_pieces = 0
        self.round = 1
        self.turn = turn
        self.state = ChessBoard.NOTHING
        self.debug = debug

    def is_valid_to_add(self,piece):
        """
        In case that the piece cannot be placed on the board
        this function returns false

        """
        for p in self.pieces:
            if piece.row == p.row and piece.col == p.col:
                return False

            if type(piece) is King and type(p) is King and (piece.row, piece.col) in p.restricted_positions():
                return False
        return True

    def add_piece(self, piece):
        """
        Add pieces to the list of pieces.
        """
        if self.is_valid_to_add(piece):
            self.pieces.append(piece)
            self.num_pieces += 1
            return True

        return False

    def get_w_king(self):
        for p in self.pieces:
            if type(p) is King and p.color is Piece.WHITE:
                return p
        return None

    def get_b_king(self):
        for p in self.pieces:
            if type(p) is King and p.color is Piece.BLACK:
                return p
        return None

    def get_w_rook(self):
        for p in self.pieces:
            if type(p) is Rook and p.color is Piece.WHITE:
                return p
        return None

    def update_state(self):
        kw = None
        kb = None
        rw = None
        for p in self.pieces:
            if type(p) is King and p.color is Piece.WHITE:
                kw = p
            if type(p) is King and p.color is Piece.BLACK:
                kb = p
            if type(p) is Rook  and p.color is Piece.WHITE:
                rw = p
        
        if rw is None:
            self.state = ChessBoard.DRAW
            return 

        restr = (set(kw.possible_moves()) | set(rw.possible_moves()))

        checked = (kb.row,kb.col) in rw.restricted_positions()

        if checked and set(kb.possible_moves()).issubset(restr):
            self.state = ChessBoard.BLACK_KING_CHECKMATE
        elif checked:
            self.state = ChessBoard.BLACK_KING_CHECKED
        elif not checked and (set(kb.possible_moves())).issubset(restr):
            self.state = ChessBoard.DRAW
        else:
            self.state = ChessBoard.NOTHING

    def change_turn(self):
        if self.turn == Piece.WHITE:
            self.turn = Piece.BLACK
        else:
            self.turn = Piece.WHITE
    
    def is_finished(self):
        if  self.state is  ChessBoard.BLACK_KING_CHECKMATE or  self.state is ChessBoard.DRAW:
            return True
        return False

    @staticmethod
    def get_random_chessboard():
        rboard = None
        while True:
            rboard = ChessBoard(debug= True)
            all_added = []
            all_added.append(rboard.add_piece(King(random.randint(0,7), random.randint(0,7), Piece.BLACK)))
            all_added.append(rboard.add_piece(King(random.randint(0,7), random.randint(0,7), Piece.WHITE)))
            all_added.append(rboard.add_piece(Rook(random.randint(0,7), random.randint(0,7), Piece.WHITE)))
            
            if all(all_added):
                rboard.update_state()
                if (rboard.state is not ChessBoard.BLACK_KING_CHECKMATE) and 
                (rboard.state is not ChessBoard.BLACK_KING_CHECKED):
                    break
        return rboard

# End of class ------

if __name__ == '__main__':
    
    # White plays first
    board = ChessBoard(Piece.WHITE, debug= True)

    board = ChessBoard.get_random_chessboard()
    rw = Rook(1,2,Piece.WHITE)
    kb = King(2,5,Piece.BLACK)
    kw = King(4,6,Piece.WHITE)
 
    board.manual_play()