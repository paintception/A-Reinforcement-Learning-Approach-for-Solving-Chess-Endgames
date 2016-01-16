__author__ = 'yaron'

import json

class Piece():

    WHITE = 1
    BLACK = 0

    def __init__(self, row,col, color):
        """
        :param row: Row index of the piece
        :param col: Col index of the piece
        :param color: Color of the piece
        :except Exception: Wrong color
        :return: None
        """
        if not (color is self.WHITE or color is self.BLACK):
            raise Exception("Wrong color")
        self.row = row
        self.col = col
        self.color = color

    def __str__(self):
        """
        :return: String representation
        """
        return "%s(row - %d, col - %d)" %("W" if self.color==self.WHITE else "B", self.row, self.col)

    def __unicode__(self):
        """
        :return: String representation
        """
        return "%s(row - %d, col - %d)" %("W" if self.color==self.WHITE else "B", self.row, self.col)

    def to_json(self):
        return { 'row' : self.row , 'col' : self.col }

    def move(self, d_row, d_col):
        """
        Move the piece to the desired coordinates
        :param d_row: The desired row to move
        :param d_col: The desired column to move
        :return: True on success
        """
        if self.check_borders(d_row, d_col) and self.check_pos(d_row, d_col):
            self.col = d_col
            self.row = d_row
            return True
        return False
    
    def check_borders(self, d_row, d_col):
        """
        Check if the coordinates are inside the board
        :param d_row: The desired row
        :param d_col: The desired column
        :param N: Dimension
        :return:
        """
        if d_row < 0 or d_row > 7:
            return False
        if d_col < 0 or d_col > 7:
            return False

        return True

    def check_pos(self, d_row, d_col):
        """
        Check if the new position is valid
        :param d_row: The desired row
        :param d_col: The desired column
        :return: True on success
        """
        return False

    def restricted_positions(self, king=None):
        """
        :return: The restricted positions
        """
        return []

    def possible_moves(self, king=None):
        """
        :return: The possible moves
        """
        return []


class King(Piece):
    """
    This is the King class which inherits from Piece
    """

    def check_pos(self, d_row, d_col):
        """
        Check if the new position is valid
        :param d_row: The desired row
        :param d_col: The desired column
        :return: True on success
        """
        dist = abs(d_row-self.row) + abs(d_col-self.col)

        if dist == 1 or (dist == 2 and self.row != d_row and self.col != d_col):
            return True
        else:
            return False

    def restricted_positions(self, king=None):
        lis = self.possible_moves()
        lis.append((self.row,self.col))
        return lis

    def possible_moves(self, king=None):
        rows = []
        cols = []
        if self.row + 1 <= 7:
            rows.append(self.row+1)
        if self.row - 1 >= 0:
            rows.append(self.row-1)
        if self.col + 1 <= 7:
            cols.append(self.col+1)
        if self.col - 1 >= 0:
            cols.append(self.col-1)
        rows.append(self.row)
        cols.append(self.col)

        moves = [(row, col) for row in rows for col in cols]
        moves.remove((self.row, self.col))

        return moves


class Rook(Piece):
    """
    This is the Rook class which inherits from Piece
    """

    def check_pos(self, d_row, d_col):
        if d_row == self.row and d_col != self.col:
            return True
        if d_row != self.row and d_col == self.col:
            return True

        return False

    def possible_moves(self, king=None):
        pos = []
        for x in range(0,8):
            if x != self.row:
                pos.append((x, self.col))
            if x != self.col:
                pos.append((self.row, x))

        for p in pos:

            if p == (king.row, king.col):
                pos.remove(p)

            if (self.row == king.row and king.col > self.col):
                if p[1]>king.col:
                    pos.remove(p)
            if (self.row == king.row and king.col < self.col):
                if p[1]<king.col:
                    pos.remove(p)
            if (self.col == king.col and king.row > self.row):
                if p[0]>king.row:
                    pos.remove(p)
            if (self.col == king.col and king.row < self.row):
                if p[0]<king.row:
                    pos.remove(p)

        return pos

    def restricted_positions(self, king=None):
        lis = self.possible_moves(king)
        lis.append((self.row, self.col))
        return lis

    def check_move_validity(self, piece, row, col):
        if row == piece.row and col == piece.col:
            return False
        if col < piece.col and col < self.col and  self.col > piece.col and piece.row == self.row:
            return False
        elif row < piece.row and row < self.row and self.row < piece.row and piece.col == self.col:
            return False
        elif col > piece.col and col > self.col and self.col < piece.col and piece.row == self.row:
            return False
        elif row > piece.row and row > self.row and self.row > piece.row and piece.col == self.col:
            return False
        return True


class Bishop(Piece):

    def move(self, d_row, d_col):
        """
        Move the piece to the desired coordinates
        :param d_row: The desired row to move
        :param d_col: The desired column to move
        :return: True on success
        """
        if self.check_borders(d_row, d_col):
            self.col = d_col
            self.row = d_row
            return True
        return False

    def check_pos(self, d_row, d_col):
        """
        Check if the next move is valid
        :param d_row: The desired row
        :param d_col: The desired column
        :return: True on success
        """
        return (d_row, d_col) in self.possible_moves()

    def restricted_positions(self, king=None):
        """
        :return: The restricted positions
        """
        return self.possible_moves(king)

    def possible_moves(self, king=None):
        """
        :return: The possible moves
        """
        line1 = []
        for k in range(1, 8):
            if king is not None and (self.row - k, self.col - k) == (king.row, king.col):
                line1.clear()
            else:
                line1.append((self.row - k, self.col - k))

        for k in range(1, 8):
            if king is not None and (self.row + k, self.col + k) == (king.row, king.col):
                break
            else:
                line1.append((self.row + k, self.col + k))

        line2 = []
        for k in range(1, 8):
            if king is not None and (self.row - k, self.col + k) == (king.row, king.col):
                line2.clear()
            else:
                line2.append((self.row - k, self.col + k))

        for k in range(1, 8):
            if king is not None and (self.row + k, self.col - k) == (king.row, king.col):
                break
            else:
                line2.append((self.row + k, self.col - k))

        return list(set(line1) | set(line2))


class BlackBishop(Bishop):
    pass


class WhiteBishop(Bishop):
    pass

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

