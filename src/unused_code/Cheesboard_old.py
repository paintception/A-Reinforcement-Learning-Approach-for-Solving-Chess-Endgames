
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
def draw(self):

        print 'State: ', self.state
        print 'Round:', self.round

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
   
    def play_move(self,row,col,typ=None,realPiece=None):
        """
        Returns 0 when the move is invalid.
        """
        typp = None
        piece = None
        if realPiece is None:
            if typ in 'kK':
                typp = King
            elif typ in 'rR':
                typp = Rook

            for p in self.pieces:
                if  type(p) is typp and p.color == self.turn:
                    piece = p
                    break
            if piece is None:
                print "PIECE IS NONE"
                return False 
        else:
            piece = realPiece
        try:

            if type(piece) is King:
                for p in self.pieces:
                    # We don't care here about the same color pieces
                    if p.color != piece.color:
                        if (row,col) in p.restricted_positions():
                            raise Exception('Not allowed')
                        elif type(p) is Rook and (row,col) == (p.row,p.col):
                            self.pieces.remove(p)
                    else:
                        if (row,col) == (p.row,p.col):
                            raise Exception("Not allowed")        
            elif type(piece) is Rook:
                print "IN ROOK"
                p = self.get_wking()
                if (row,col) == (p.row,p.col):
                            raise Exception("Not allowed")
                if not piece.checkMoveValidity(p, row, col):
                    print "in check move val"
                    raise Exception("fucked up")



            o_row,o_col = piece.row, piece.col
            piece.move(row,col)
            
       #     print '(%d,%d) -> (%d,%d) OK' % (o_row,o_col,row,col)
        except:
            print '(%d,%d) -> (%d,%d) INVALID' % (piece.row,piece.col,row,col) 
            return False

        return True 

    def get_wking(self):
        for p in self.pieces:
            if type(p) is King and p.color is Piece.WHITE:
                return p
        return None

    def get_bking(self):
        for p in self.pieces:
            if type(p) is King and p.color is Piece.BLACK:
                return p
        return None

    def get_wrook(self):
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

    def manual_play(self):
        while True:
            self.draw()
            p =  "WHITE" if self.turn==Piece.WHITE else "BLACK"
            piece,row,col = receiveCommand('[' + p + ']Next move:')
            while self.play_move(row,col,piece) is False:
                piece,row,col = receiveCommand('[' + p +'] Play again:')
            
            self.update_state()

            if self.is_finished(): 
                self.draw()
                return self.state

            self.change_turn()
            if( self.turn == Piece.WHITE):
                self.round += 1

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
                if rboard.state is not ChessBoard.BLACK_KING_CHECKMATE:
                    break
        if rboard.state == ChessBoard.BLACK_KING_CHECKED:
            rboard.change_turn()
        return rboard



# End of class ------

def receiveCommand(msg):
    line  = raw_input(msg)
    while ( len(line) is not 3) or (line[0]  not in 'KkrR') or is_number(line[1]) is 0 or is_number(line[2]) is 0:
        line = raw_input(msg)
    row,col = int(line[1]), int(line[2])
    return line[0],row,col

def is_number(n):
    try:
        n = int(n)
    except ValueError:
        return 0
    return 1

if __name__ == '__main__':
    
    # White plays first
    board = ChessBoard(Piece.WHITE, debug= True)

    board = ChessBoard.get_random_chessboard()
    rw = Rook(1,2,Piece.WHITE)
    kb = King(2,5,Piece.BLACK)
    kw = King(4,6,Piece.WHITE)

#    board.add_piece(rw)
#    board.add_piece(kb)
#    board.add_piece(kw)
     
    board.manual_play()


