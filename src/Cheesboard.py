__author__ = 'yaron'

from Pieces import King, Rook

class Cheesboard:

    def __init__(self):
        self.pieces = []
        self.num_pieces = 0

    def add_piece(self, piece):
        self.pieces.append(piece)
        self.num_pieces += 1




    def draw(self):
        pass
