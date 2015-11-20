__author__ = 'yaron'


class Piece():

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


class King(Piece):

    def check_pos(self, d_row, d_col):
        dist = abs(d_row-self.row) + abs(d_col-self.col)
        if dist == 1:
            return True
        else:
            return False

    def restricted_positions(self):
        pos = []
        pos.append((self.row+1, self.col-1))
        pos.append((self.row+1, self.col))
        pos.append((self.row+1, self.col+1))

        pos.append((self.row-1, self.col-1))
        pos.append((self.row-1, self.col))
        pos.append((self.row-1, self.col+1))

        pos.append((self.row, self.col-1))
        pos.append((self.row, self.col+1))

        return pos


class Rook(Piece):

    def check_pos(self, d_row, d_col):
        if d_row == self.row and d_col != self.col:
            return True
        if d_row != self.row and d_col == self.col:
            return True

        return False

    def restricted_positions(self):
        pos = []
        for x in range(0,7):
            if x != self.row:
                pos.append((x, self.col))
            if x != self.col:
                pos.append((self.row, x))


if __name__ == '__main__':
    print("King")
    k = King(3,3)
    print(k)
    k.move(3,2)
    print(k)
    print("Rook")
    r = Rook(3,3)
    print(r)
    r.move(3,7)
    print(r)

