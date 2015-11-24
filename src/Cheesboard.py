__author__ = 'yaron'
import sys
from Pieces import King, Rook, Piece

class ChessBoard:
    NOTHING = 'PLAYING'
    BLACK_KING_CHECKED = 'BLACK_KING_CHECKED'
    DRAW = 'DRAW' 
    WIN = 'WIN' 

    def __init__(self,turn):
        self.pieces = []
        self.num_pieces = 0
        self.round = 1
        self.turn = turn
        self.state = ChessBoard.NOTHING

    def is_valid_to_add(self,piece):
        """
        In case that the piece cannot be placed on the board
        this function raises an exception

        """
        for p in self.pieces:
            if piece.row == p.row and piece.col == p.col:
                raise Exception('Can\'t place this piece here')
            # They have to be in different color
            if piece.color is not p.color:
                for invalidPos in  p.restricted_positions():
                    if(piece.row == invalidPos[0]) and (piece.col == invalidPos[1]):
                        raise Exception('Can\'t place this piece here')
        return 1

    def add_piece(self, piece):
        """
        Add pieces to the list of pieces.
        """
        if self.is_valid_to_add(piece):
            self.pieces.append(piece)
            self.num_pieces += 1
            return 1

        return 0


    def draw(self):
        """
        This will just draw the ChessBoard.
        """
        sys.stdout.write('  ')
        for k in range(0,8):
            sys.stdout.write('  '+str(k)+' ')
        sys.stdout.write('\n')

        for row in range(0,8):

            sys.stdout.write('  +')
            for k in range(0,8):
                sys.stdout.write('---+')
            sys.stdout.write('\n')

            sys.stdout.write(str(row)+' ')
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

   
    def play_move(self,row,col,typ):
        """
        Returns 0 when the move is invalid.
        """
        typp = None
        piece = None
        if typ in 'kK':
            typp = King
        elif typ in 'rR':
            typp = Rook

        for p in self.pieces:
            if  type(p) is typp and p.color == self.turn:
                piece = p
                break
        if piece is None:
            return 0
        try:

            if type(piece) is King:
                for p in self.pieces:
                    # We don't care here about the same color pieces
                    if p.color != piece.color:
                        if (row,col) in p.restricted_positions():
                            raise Exception('Not allowed')

            o_row,o_col = piece.row, piece.col
            piece.move(row,col)
            
            print '(%d,%d) -> (%d,%d) OK' % (o_row,o_col,row,col) 
        except:
            print '(%d,%d) -> (%d,%d) INVALID' % (piece.row,piece.col,row,col) 
            return 0

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
    
        if (kb.row,kb.col) in rw.restricted_positions():
            self.state = ChessBoard.BLACK_KING_CHECKED 
            return

        self.state = ChessBoard.NOTHING 

    def change_turn(self):
        if self.turn == Piece.WHITE:
            self.turn = Piece.BLACK
        else:
            self.turn = Piece.WHITE

    def manual_play(self):
        while True:
            print 'State: ', self.state
            self.draw()
            p =  "WHITE" if self.turn==Piece.WHITE else "BLACK"
            piece,row,col = receiveCommand('[' + p + ']Next move:')
            while self.play_move(row,col,piece) is 0:
                piece,row,col = receiveCommand('[' + p +'] Play again:')
            
            self.update_state()
            self.change_turn()

    def random_play(self):
        while True:
            pass


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
    board = ChessBoard(Piece.WHITE)

    wr = Rook(5,2,Piece.WHITE)
    bk = King(2,5,Piece.BLACK)
    wk = King(4,6,Piece.WHITE)

    board.add_piece(wr)
    board.add_piece(wk)
    board.add_piece(bk)
    
    board.manual_play()


