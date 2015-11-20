__author__ = 'yaron'
import sys
from Pieces import King, Rook, Piece

class ChessBoard:

    def __init__(self):
        self.pieces = []
        self.num_pieces = 0

    def add_piece(self, piece):
        self.pieces.append(piece)
        self.num_pieces += 1

    def is_valid_to_add(self,piece):
        for p in self.pieces:
            print p



    def draw(self):

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
                            if p.color == Piece.WHITE: 
                                sys.stdout.write('| K*')
                            else:
                                sys.stdout.write('| K ')

                        if type(p) is Rook:
                            if p.color == Piece.WHITE: 
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

if __name__ == '__main__':
    board = ChessBoard()
    board.add_piece( Rook(1,2,Piece.WHITE))
    board.add_piece( King(6,3,Piece.BLACK))
    board.add_piece( Rook(6,2,Piece.BLACK))
    board.draw()



