
__author__ = 'yaron'
import sys
from Pieces import King, Rook, Piece
import random
import copy


class ChessBoard:
    NOTHING = 'PLAYING'
    BLACK_KING_CHECKED = 'BLACK_KING_CHECKED'
    BLACK_KING_CHECKMATE = 'BLACK_KING_CHECKMATE'
    DRAW = 'DRAW'

    def __init__(self,wk=None,wr=None,bk=None,debug=None):
        self.pieces = []
        self.num_pieces = 0
        self.round = 1
        self.turn = Piece.WHITE
        self.state = ChessBoard.NOTHING
        self.debug = debug
        self.valid = True

        if(wk is None or wr is None or bk is None):
            return

        print(type(wk))
        all_added = []
        all_added.append(self.add_piece(wk))
        all_added.append(self.add_piece(wr))
        all_added.append(self.add_piece(bk))
        
        if all(all_added):
            self.update_state()
        else:
            self.valid = False

    def board_id():
        b_king = self.get_b_king()
        w_king = self.get_w_king()
        w_rook = self.get_w_rook()

        return (b_king.row, b_king.col, w_king.row, w_king.col, w_rook.row, w_rook.col)
        

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

    def play_move(self,row,col,piece):
        w_king = self.get_w_king()
        w_rook = self.get_w_rook()
        b_king = self.get_b_king()
        
        if not piece.check_borders(row, col) or not piece.check_pos(row, col):
            return False

        if w_king is piece:
            
            res = b_king.restricted_positions()
            res.append((w_rook.row, w_rook.col))
            if self.turn is Piece.BLACK or (row,col) in res:
                return False
        
        elif w_rook is piece:
            if self.turn is Piece.BLACK or not piece.checkMoveValidity(w_king, row, col):
                return False

        elif b_king is piece:
            res_wrook = set(w_rook.restricted_positions())
            res_wking = set(w_king.restricted_positions())
            res = res_wrook | res_wking
            res.add((w_king.row, w_king.col))
            
            if w_rook.row is row and w_rook.col is col:
                self.pieces.remove(w_rook)

            if self.turn is Piece.WHITE or (row,col) in res:
                return False
        

        if piece.move(row,col):
            self.change_turn()
            self.update_state()

            return True

        return False

    def get_possible_moves(self):
        pieces_to_play = []
        if self.turn == Piece.WHITE:
            pieces_to_play = [self.get_w_king(), self.get_w_rook()]
        else:
            pieces_to_play = [self.get_b_king()]

        boards = []
        for piece in pieces_to_play:
            moves = piece.possible_moves()
            for row,col in moves:
                    new_board = copy.deepcopy(self)
                    if new_board.play_move(row, col, piece):
                        boards.append(new_board)

        return boards

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
                if (rboard.state is not ChessBoard.BLACK_KING_CHECKMATE) and (rboard.state is not ChessBoard.BLACK_KING_CHECKED):
                    break
        return rboard

    def draw(self):
        print('State: ', self.state)
        print('Round:', self.round)
        print('Player:', "BLACK" if self.turn is Piece.BLACK else "WHITE")
        sys.stdout.write('  ')
        for k in range(0,8):
            sys.stdout.write('  '+str(k)+' ')
        sys.stdout.write('\n')

        for row in range(0,8):

            sys.stdout.write('  +')
            for k in range(0,8):
                sys.stdout.write('---+')
            sys.stdout.write('\n')

            if self.debug:
                sys.stdout.write(str(row)+' ')
            else:
                sys.stdout.write(str(8-row)+' ')
            for col in range(0,8):

                check = 0
                for p in self.pieces:
                    if p.row == row and p.col == col:
                        check = 1
                        if type(p) is King:
                            if p.color == Piece.BLACK: 
                                sys.stdout.write('| K*')
                            else:
                                sys.stdout.write('| K ')

                        if type(p) is Rook:
                            if p.color == Piece.BLACK: 
                                sys.stdout.write('| R*')
                            else:
                                sys.stdout.write('| R ')
                if check is 0:
                    sys.stdout.write('|   ')
            
            sys.stdout.write('|\n')
    
        sys.stdout.write('  +')
        for k in range(0,8):
            sys.stdout.write('---+')
        sys.stdout.write('\n')

        sys.stdout.write('  ')
        for k in range(0,8):
            if self.debug:
                sys.stdout.write('  '+str(k)+' ')
            else:
                sys.stdout.write('  '+ chr(ord('a')+k)+' ')
        sys.stdout.write('\n')
# End of class ------

if __name__ == '__main__':
    
    # White plays first
    rw = Rook(7,0,Piece.WHITE)
    kb = King(0,2,Piece.BLACK)
    kw = King(2,2,Piece.WHITE)
    board = ChessBoard(Piece.WHITE, kw, rw, kb)
    board.draw()

    # #board = ChessBoard.get_random_chessboard()
    
    # board.add_piece(rw)
    # board.add_piece(kb)
    # board.add_piece(kw)
    # board.update_state()
    # board.draw()
    
    # board.play_move(0,0,rw)
    # board.draw()
