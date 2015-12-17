from Cheesboard import ChessBoard
from Pieces import King, Rook, Piece
import pickle


class BaseParams:


    def __init__(self):
        pass

    def get_all_params(self):
        pass


    def get_possible_nxt_prms(self,par):
        pass

    def get_id(self):
        pass


class BoardPossitionParams(BaseParams):
    """docstring for BoardPossitionParams"""


    def get_all_params(self):
        params = []
        for wk_r in range(0,8):
            for wk_c in range(0,8):
                for wr_r in range(-1,8):
                    for wr_c in range(-1,8):
                        for bk_r in range(0,8):
                            for bk_c in range(0,8):
                                for white_plays in range(0,2):
                                    if(wr_r == -1 and wr_c != -1 or wr_r!=-1 and wr_c == -1) :
                                        continue
                                    params.append((wk_r, wk_c, wr_r, wr_c, bk_r, bk_c,white_plays))
        return params

    def get_possible_nxt_prms(self, params=None):
        if params is None:
            params = self.get_all_params()

        count = 0
        nxt_prms = {}
        for wk_r, wk_c, wr_r, wr_c, bk_r, bk_c,white_plays in params:

            board = ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                               wr=Rook(wr_r, wr_c, Piece.WHITE),
                               bk=King(bk_r, bk_c, Piece.BLACK),
                               white_plays=white_plays)
            if not board.valid:
                continue

            nxt_pos = {}
            for nxt_moves in board.get_possible_moves():
                r = 0
                if nxt_moves.state == ChessBoard.BLACK_KING_CHECKMATE:
                    r = 100
                elif nxt_moves.state == ChessBoard.DRAW:
                    r = -100
                nxt_pos[nxt_moves.board_id()] = r

            nxt_prms[(wk_r,wk_c,wr_r,wr_c,bk_r,bk_c,white_plays)] = nxt_pos

            count += 1
            if count % 1000 == 0:
                print (count)

        return nxt_prms

    def save(self, parms, filename):
        to_save_parms = {}
        with open(filename, 'wb') as outfile:
            pickle.dump(parms, outfile, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename, 'rb') as infile:
            params = pickle.load(infile)
            return params

if __name__ == '__main__':

    bp = BoardPossitionParams()
    par = bp.get_possible_nxt_prms()
    bp.save(par, 'res/memory100-100.bson')





    """
    wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = (2, 6, 0, 0, 0, 7, 1)
    board = ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                               wr=Rook(wr_r, wr_c, Piece.WHITE),
                               bk=King(bk_r, bk_c, Piece.BLACK),debug=True,white_plays=0)

    board.draw()
    print (board.valid)

    next_poss = board.get_possible_moves()

    print (len(next_poss))
    for ps in next_poss:
        wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = ps.board_id()

        board = ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                            wr=Rook(wr_r, wr_c, Piece.WHITE),
                            bk=King(bk_r, bk_c, Piece.BLACK),
                            white_plays=white_plays
                            );
        board.draw()
        print (ps.board_id())
    """