from Pieces import King, Rook, Piece
import copy
import sys


class Chessboard:
    """
    This is the main class of the game
    """

    # Constant Definitions
    NOTHING = 'PLAYING'
    BLACK_KING_CHECKED = 'BLACK_KING_CHECKED'
    BLACK_KING_CHECKMATE = 'BLACK_KING_CHECKMATE'
    DRAW = 'DRAW'

    def __init__(self, wk=None, wr=None, bk=None, white_plays=None,dim=None):
        """
        The constructor of Chessboard
        :param wk: White King Piece
        :param wr: White Rook Piece
        :param bk: Black King Piece
        :param white_plays: True if white begins
        :return: None
        """
        self.pieces = []
        self.round = 1
        self.turn = white_plays

        self.state = Chessboard.NOTHING
        self.valid = True
        if not dim:
            self.N = 8
        else:
            self.N = dim

        if wk is None or wr is None or bk is None:
            return

        # Add the pieces
        all_added = []
        all_added.append(self.add_piece(wk))
        all_added.append(self.add_piece(bk))
        if (wr.row, wr.col) != (-1, -1):
            all_added.append(self.add_piece(wr))

        if all(all_added):
            self.update_state()
        else:
            self.valid = False

        if white_plays and self.state == Chessboard.BLACK_KING_CHECKED:
            self.valid = False

    def board_id(self):
        """
        :return: The board id
        """
        b_king = self.get_b_king()
        w_king = self.get_w_king()
        w_rook = self.get_w_rook()
        x, y = 0, 0
        if w_rook is None:
            x, y = -1, -1
        else:
            x, y = w_rook.row, w_rook.col

        return w_king.row, w_king.col, x, y, b_king.row, b_king.col, self.turn

    def is_valid_to_add(self, piece):
        """
        In case that the piece cannot be placed on the board
        this function returns false
        :param piece: The piece to add
        :return True on success
        """
        for p in self.pieces:
            if piece.row == p.row and piece.col == p.col:
                return False
            if type(piece) is King and type(p) is King and (piece.row, piece.col) in p.restricted_positions(self.N):
                return False
        return True

    def add_piece(self, piece):
        """
        Add pieces to the list of pieces.
        :param piece: The piece to add
        """
        if self.is_valid_to_add(piece):
            self.pieces.append(piece)
            return True

        return False

    def get_w_king(self):
        """
        :return: White King
        """
        for p in self.pieces:
            if type(p) is King and p.color == Piece.WHITE:
                return p
        return None

    def get_b_king(self):
        """
        :return: Black King
        """
        for p in self.pieces:
            if type(p) is King and p.color == Piece.BLACK:
                return p
        return None

    def get_w_rook(self):
        """
        :return: White Rook
        """
        for p in self.pieces:
            if type(p) is Rook and p.color == Piece.WHITE:
                return p
        return None

    def play_move(self, row, col, piece):
        """
        Play next move
        :param row: Desired row to play
        :param col: Desired column to play
        :param piece: Desired piece to play
        :return: True on success
        """
        if self.state == Chessboard.DRAW:
            return True

        w_king = self.get_w_king()
        w_rook = self.get_w_rook()
        b_king = self.get_b_king()

        # Check borders
        if not piece.check_borders(row, col, self.N) or not piece.check_pos(row, col):
            return False

        # If white king plays
        if w_king is piece:
            res = b_king.restricted_positions(self.N)
            res.append((w_rook.row, w_rook.col))
            if self.turn is Piece.BLACK or (row, col) in res:
                return False

        elif w_rook is piece:
            if self.turn is Piece.BLACK or not piece.check_move_validity(w_king, row, col):
                return False

        elif b_king is piece:
            res_wrook = set(w_rook.restricted_positions(w_king, self.N))
            res_wrook.remove((w_rook.row, w_rook.col))
            res_wking = set(w_king.restricted_positions(self.N))
            res = res_wrook | res_wking
            res.add((w_king.row, w_king.col))

            if w_rook.row is row and w_rook.col is col:
                self.pieces.remove(w_rook)

            if self.turn is Piece.WHITE or (row, col) in res:
                return False

        if piece.move(row, col, self.N):
            self.change_turn()
            self.update_state()
            return True

        return False

    def get_possible_moves(self):
        """
        :return: Possible boards
        """
        pieces_to_play = []
        if self.state is Chessboard.DRAW:
            return []
        if self.turn == Piece.WHITE:
            pieces_to_play = [self.get_w_king(), self.get_w_rook()]
        else:
            pieces_to_play = [self.get_b_king()]

        boards = []
        piece_num = 0
        for piece in pieces_to_play:

            moves = []
            if type(piece) is Rook:
                piece_num = 1
                moves = piece.possible_moves(self.get_w_king(), self.N)
            else:
                if Piece.BLACK == piece.color:
                    piece_num = 2
                else:
                    piece_num = 0
                moves = piece.possible_moves(self.N)

            for row, col in moves:
                new_board = copy.deepcopy(self)
                clone_piece = None
                if piece_num is 0:
                    clone_piece = new_board.get_w_king()
                elif piece_num is 1:
                    clone_piece = new_board.get_w_rook()
                else:
                    clone_piece = new_board.get_b_king()

                if new_board.play_move(row, col, clone_piece):
                    boards.append(new_board)

        return boards

    def update_state(self):
        """
        Update the current state
        :return:None
        """
        kw = None
        kb = None
        rw = None
        for p in self.pieces:
            if type(p) is King and p.color is Piece.WHITE:
                kw = p
            if type(p) is King and p.color is Piece.BLACK:
                kb = p
            if type(p) is Rook and p.color is Piece.WHITE:
                rw = p

        if rw is None:
            self.state = Chessboard.DRAW
            return

        restr = (set(kw.possible_moves(self.N)) | set(rw.possible_moves(kw,self.N)))

        res = rw.restricted_positions(kw,self.N)
        checked = (kb.row, kb.col) in res

        if checked and set(kb.possible_moves(self.N)).issubset(restr):
            self.state = Chessboard.BLACK_KING_CHECKMATE
        elif checked:
            self.state = Chessboard.BLACK_KING_CHECKED
            self.turn = Piece.BLACK
        elif not checked and (set(kb.possible_moves(self.N))).issubset(restr):
            self.state = Chessboard.DRAW
        else:
            self.state = Chessboard.NOTHING

    def change_turn(self):
        """
        Change the turn
        :return: None
        """
        if self.turn == Piece.WHITE:
            self.turn = Piece.BLACK
        else:
            self.turn = Piece.WHITE

    def is_finished(self):
        """
        :return: True if black king is checkmate or a draw
        """
        if self.state is Chessboard.BLACK_KING_CHECKMATE or self.state is Chessboard.DRAW:
            return True
        return False

    def draw(self):
        """
        Draw the Chessboard
        :return:None
        """
        print('State: ', self.state)
        print('Round:', self.round)
        print('Player:', "BLACK" if self.turn is Piece.BLACK else "WHITE")
        sys.stdout.write('  ')
        for k in range(0,self.N):
            sys.stdout.write('  ' + str(k) + ' ')
        sys.stdout.write('\n')
        for row in range(0,self.N):
            sys.stdout.write('  +')
            for k in range(0,self.N):
                sys.stdout.write('---+')
            sys.stdout.write('\n')
            sys.stdout.write(str(row) + ' ')
            for col in range(0,self.N):
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
        for k in range(0, self.N):
            sys.stdout.write('---+')
        sys.stdout.write('\n')
        sys.stdout.write('  ')
        for k in range(0, self.N):
            sys.stdout.write('  ' + str(k) + ' ')
        sys.stdout.write('\n')

    @staticmethod
    def get_board(state_id,dim=None):
        wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = state_id
        return Chessboard(wk=King(wk_r, wk_c, Piece.WHITE),
                          wr=Rook(wr_r, wr_c, Piece.WHITE),
                          bk=King(bk_r, bk_c, Piece.BLACK),
                          white_plays=white_plays,
                          dim=dim
                          )

if __name__ == '__main__':
    board = Chessboard.get_board((2,3,1,5,2,5,0),6)
    board.draw()

