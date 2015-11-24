__author__ = 'yaron'


class Piece(object):

    WHITE = 1
    BLACK = 0

    def __init__(self, row, col, color):
        if not (color is self.WHITE or color is self.BLACK):
            raise Exception("Wrong color")
        self.row = row
        self.col = col
        self.color = color

    def __str__(self):
        return "%s(row - %d, col - %d)" %("W" if self.color==self.WHITE else "B", self.row, self.col)

    def __unicode__(self):
        return "%s(row - %d, col - %d)" %("W" if self.color==self.WHITE else "B", self.row, self.col)

    def move(self, d_row, d_col):
        if self.check_borders(d_row, d_col) and self.check_pos(d_row, d_col):
            self.col = d_col
            self.row = d_row
        else:
            raise Exception("Wrong move")

    def check_borders(self, d_row, d_col):
        if d_row < 0 or d_row > 7:
            return False
        if d_col < 0 or d_col > 7:
            return False

        return True

    def check_pos(self, d_row, d_col):
        return False

    def restricted_positions(self):
        return []

    def possible_moves(self):
        return []


class King(Piece):

    def check_pos(self, d_row, d_col):
        dist = abs(d_row-self.row) + abs(d_col-self.col)

        if dist == 1 or (dist == 2 and self.row !=  d_row and self.col != d_col):
            return True
        else:
            return False

    def restricted_positions(self):
        return self.possible_moves()

    def possible_moves(self):
        rows = []
        cols = []
        if self.row + 1 <= 7:
            rows.append(self.row+1)
        if self.row - 1 > 0:
            rows.append(self.row-1)
        if self.col + 1 <= 7:
            cols.append(self.col+1)
        if self.col - 1 > 0:
            cols.append(self.col-1)
        rows.append(self.row)
        cols.append(self.col)
        moves = [(row, col) for row in rows for col in cols]
        moves.remove((self.row, self.col))
        return moves


class Rook(Piece):

    def check_pos(self, d_row, d_col):
        if d_row == self.row and d_col != self.col:
            return True
        if d_row != self.row and d_col == self.col:
            return True

        return False

    def possible_moves(self):
        pos = []
        for x in range(0,8):
            if x != self.row:
                pos.append((x, self.col))
            if x != self.col:
                pos.append((self.row, x))
        return pos

    def restricted_positions(self):
        return self.possible_moves()

if __name__ == '__main__':
    print("King")
    k = King(3,3, Piece.WHITE)
    print(k.possible_moves())
    # k.move(3,2)
    # print(k)
    # print("Rook")
    # r = Rook(3,3)
    # print(r)
    # r.move(3,7)
    # print(r)
