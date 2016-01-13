import sys
from src.Pieces import King, Bishop, Piece, BlackBishop, WhiteBishop
import random
import copy


class ChessBoardKB:
    NOTHING = 'PLAYING'
    BLACK_KING_CHECKED = 'BLACK_KING_CHECKED'
    BLACK_KING_CHECKMATE = 'BLACK_KING_CHECKMATE'
    DRAW = 'DRAW'

    def __init__(self, wk=None, wbw=None, wbb=None, bk=None, debug=None, white_plays=None):
        self.pieces = []
        self.round = 1
        self.turn = Piece.WHITE
        if white_plays is not None:
            self.turn = white_plays
        self.state = ChessBoardKB.NOTHING
        self.debug = debug
        self.valid = True

        if wk is None or wbb is None or wbw is None or bk is None:
            return

        all_added = []
        all_added.append(self.add_piece(wk))
        if (wbb.row, wbb.col) != (-1, -1):
            all_added.append(self.add_piece(wbb))
        if (wbw.row, wbw.col) != (-1, -1):
            all_added.append(self.add_piece(wbw))
        all_added.append(self.add_piece(bk))

        if all(all_added):
            self.update_state()
        else:
            self.valid = False

            # if self.state == ChessBoardKB.BLACK_KING_CHECKED:
            #    self.valid = False

    def board_id(self):
        b_king = self.get_b_king()
        w_king = self.get_w_king()
        w_bishop_white = self.get_w_bishop_white()
        w_bishop_black = self.get_w_bishop_black()
        w_bishop_white_row, w_bishop_white_col = 0, 0
        if w_bishop_white is None:
            w_bishop_white_row, w_bishop_white_col = -1, -1
        else:
            w_bishop_white_row, w_bishop_white_col = w_bishop_white.row, w_bishop_white.col
            
        w_bishop_black_row, w_bishop_black_col = 0, 0
        if w_bishop_black is None:
            w_bishop_black_row, w_bishop_black_col = -1, -1
        else:
            w_bishop_black_row, w_bishop_black_col = w_bishop_black.row, w_bishop_black.col

        return w_king.row, w_king.col, w_bishop_white_row, w_bishop_white_col, w_bishop_black_row, w_bishop_black_col, b_king.row, b_king.col, self.turn

    def is_valid_to_add(self, piece):
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
            return True

        return False

    def get_w_king(self):
        for p in self.pieces:
            if type(p) is King and p.color == Piece.WHITE:
                return p
        return None

    def get_b_king(self):
        for p in self.pieces:
            if type(p) is King and p.color == Piece.BLACK:
                return p
        return None
    
    def get_w_bishop_white(self):
        for p in self.pieces:
            if type(p) is WhiteBishop and p.color == Piece.WHITE:
                return p
        return None
    
    def get_w_bishop_black(self):
        for p in self.pieces:
            if type(p) is BlackBishop and p.color == Piece.WHITE:
                return p
        return None

    def play_move(self, row, col, piece):

        if self.state == ChessBoardKB.DRAW:
            return True
        w_king = self.get_w_king()
        w_bishop_white = self.get_w_bishop_white()
        w_bishop_black = self.get_w_bishop_black()
        b_king = self.get_b_king()

        if not piece.check_borders(row, col):
            return False

        if w_king is piece:

            res = b_king.restricted_positions()
            res.append((w_bishop_white.row, w_bishop_white.col))
            res.append((w_bishop_black.row, w_bishop_black.col))
            if self.turn is Piece.BLACK or (row, col) in res:
                return False

        elif w_bishop_white is piece or w_bishop_black is piece:
            if self.turn is Piece.BLACK or not (row, col) in piece.possible_moves(w_king):
                return False

        elif b_king is piece:
            res_w_bishop_white = set(w_bishop_white.restricted_positions(w_king))
            res_w_bishop_black = set(w_bishop_black.restricted_positions(w_king))
            res_w_king = set(w_king.restricted_positions())
            res = res_w_bishop_white | res_w_bishop_black | res_w_king
            res.add((w_king.row, w_king.col))

            if w_bishop_white.row is row and w_bishop_white.col is col:
                self.pieces.remove(w_bishop_white)
                
            if w_bishop_black.row is row and w_bishop_black.col is col:
                self.pieces.remove(w_bishop_black)

            if self.turn is Piece.WHITE or (row, col) in res:
                return False

        if piece.move(row, col):
            self.change_turn()
            self.update_state()

            return True

        return False

    def get_possible_moves(self):
        pieces_to_play = []
        if self.state is ChessBoardKB.DRAW or self.state is ChessBoardKB.BLACK_KING_CHECKMATE or not self.valid:
            return []

        if self.turn == Piece.WHITE:
            pieces_to_play = [self.get_w_king(), self.get_w_bishop_white(), self.get_w_bishop_black()]
        else:
            pieces_to_play = [self.get_b_king()]

        boards = []
        piece_num = 0
        for piece in pieces_to_play:

            moves = []
            if type(piece) is BlackBishop:
                piece_num = 1
                moves = piece.possible_moves(self.get_w_king())
            elif type(piece) is WhiteBishop:
                piece_num = 2
                moves = piece.possible_moves(self.get_w_king())
            else:
                if Piece.BLACK == piece.color:
                    piece_num = 3
                else:
                    piece_num = 0
                moves = piece.possible_moves()

            for row, col in moves:
                new_board = copy.deepcopy(self)
                clone_piece = None
                if piece_num is 0:
                    clone_piece = new_board.get_w_king()
                elif piece_num is 1:
                    clone_piece = new_board.get_w_bishop_black()
                elif piece_num is 2:
                    clone_piece = new_board.get_w_bishop_white()
                else:
                    clone_piece = new_board.get_b_king()

                if new_board.play_move(row, col, clone_piece):
                    boards.append(new_board)

        return boards

    def update_state(self):
        kw = None
        kb = None
        bww = None
        bwb = None
        for p in self.pieces:
            if type(p) is King and p.color is Piece.WHITE:
                kw = p
            if type(p) is King and p.color is Piece.BLACK:
                kb = p
            if type(p) is WhiteBishop and p.color is Piece.WHITE:
                bww = p
            if type(p) is BlackBishop and p.color is Piece.WHITE:
                bwb = p

        if bww is None or bwb is None:
            self.state = ChessBoardKB.DRAW
            return

        restr = (set(kw.possible_moves()) | set(bww.possible_moves(kw)) | set(bwb.possible_moves(kw)))

        res = (set(bww.possible_moves(kw)) | set(bwb.possible_moves(kw)))
        checked = (kb.row, kb.col) in res

        if checked and set(kb.possible_moves()).issubset(restr):
            self.state = ChessBoardKB.BLACK_KING_CHECKMATE
        elif checked:
            self.state = ChessBoardKB.BLACK_KING_CHECKED
            self.turn = Piece.BLACK
        elif not checked and (set(kb.possible_moves())).issubset(restr):
            self.state = ChessBoardKB.DRAW
        else:
            self.state = ChessBoardKB.NOTHING

    def change_turn(self):
        if self.turn == Piece.WHITE:
            self.turn = Piece.BLACK
        else:
            self.turn = Piece.WHITE

    def is_finished(self):
        if self.state is ChessBoardKB.BLACK_KING_CHECKMATE or self.state is ChessBoardKB.DRAW:
            return True
        return False

    @staticmethod
    def get_random_ChessBoardKB():
        rboard = None
        # while True:
        #     rboard = ChessBoardKB(debug=True)
        #     all_added = []
        #     all_added.append(rboard.add_piece(King(random.randint(0, 7), random.randint(0, 7), Piece.BLACK)))
        #     all_added.append(rboard.add_piece(King(random.randint(0, 7), random.randint(0, 7), Piece.WHITE)))
        #     all_added.append(rboard.add_piece(Rook(random.randint(0, 7), random.randint(0, 7), Piece.WHITE)))
        # 
        #     if all(all_added):
        #         rboard.update_state()
        #         if (rboard.state is not ChessBoardKB.BLACK_KING_CHECKMATE) and (
        #             rboard.state is not ChessBoardKB.BLACK_KING_CHECKED):
        #             break
        return rboard

    def draw(self):
        print('State: ', self.state)
        # print('Round:', self.round)
        print('Player:', "BLACK" if self.turn is Piece.BLACK else "WHITE")
        sys.stdout.write('  ')
        for k in range(0, 8):
            sys.stdout.write('  ' + str(k) + ' ')
        sys.stdout.write('\n')

        for row in range(0, 8):

            sys.stdout.write('  +')
            for k in range(0, 8):
                sys.stdout.write('---+')
            sys.stdout.write('\n')

            if self.debug:
                sys.stdout.write(str(row) + ' ')
            else:
                sys.stdout.write(str(8 - row) + ' ')
            for col in range(0, 8):

                check = 0
                for p in self.pieces:
                    if p.row == row and p.col == col:
                        check = 1
                        if type(p) is King:
                            if p.color == Piece.BLACK:
                                sys.stdout.write('| K*')
                            else:
                                sys.stdout.write('| K ')

                        if type(p) is BlackBishop or type(p) is WhiteBishop:
                            if p.color == Piece.BLACK:
                                sys.stdout.write('| B*')
                            else:
                                sys.stdout.write('| B ')
                if check is 0:
                    sys.stdout.write('|   ')

            sys.stdout.write('|\n')

        sys.stdout.write('  +')
        for k in range(0, 8):
            sys.stdout.write('---+')
        sys.stdout.write('\n')

        sys.stdout.write('  ')
        for k in range(0, 8):
            if self.debug:
                sys.stdout.write('  ' + str(k) + ' ')
            else:
                sys.stdout.write('  ' + chr(ord('a') + k) + ' ')
        sys.stdout.write('\n')


# End of class ------

if __name__ == '__main__':
    # White plays first
    bww = WhiteBishop(2, 7, Piece.WHITE)
    bwb = BlackBishop(3, 7, Piece.WHITE)
    kb = King(1, 1, Piece.BLACK)
    kw = King(0, 7, Piece.WHITE)
    board = ChessBoardKB(kw, bww, bwb, kb, white_plays=True, debug=True)
    print(board.board_id())
    board.draw()
    # exit(1)

    # print(board.play_move(2, 7, board.get_b_king()))
    # print(board.board_id())
    # board.draw()
    print(board.play_move(3, 6, board.get_w_bishop_white()))
    print(board.board_id())
    board.draw()

    board = ChessBoardKB.get_random_ChessBoardKB()

    # board.add_piece(rw)
    # board.add_piece(kb)
    # board.add_piece(kw)
    # board.update_state()
    # board.draw()

    # board.play_move(0,0,rw)
    # board.draw()
