from Cheesboard import ChessBoard
from src.CheesboardKB import ChessBoardKB
from src.Pieces import *
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
    """
    The purpose of this class is to build and save all the possible states
    of the chessboard with two kings and a rook
    """
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
                r = -1
                if nxt_moves.state == ChessBoard.BLACK_KING_CHECKMATE:
                    r = 1
                elif nxt_moves.state == ChessBoard.DRAW:
                    r = 0
                nxt_pos[nxt_moves.board_id()] = r

            nxt_prms[(wk_r,wk_c,wr_r,wr_c,bk_r,bk_c,white_plays)] = nxt_pos

            count += 1
            if count % 1000 == 0:
                print (count)

        return nxt_prms

    def save(self, parms, filename):
        """
        :param params: The data to save
        :param filename: The name of the file
        :return: None
        """
        with open(filename, 'wb') as outfile:
            pickle.dump(parms, outfile, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        """
        Load parameters
        :param filename: The name of the file
        :return: Parameters
        """
        with open(filename, 'rb') as infile:
            params = pickle.load(infile)
            return params

class BoardPossitionParamsKB(BaseParams):
    """
    The purpose of this class is to build and save all the possible states
    of the chessboard with two kings and a rook
    """
    def get_all_params(self):
        params = []
        for wk_r in range(0,8):
            for wk_c in range(0,8):
                for wbw_r in range(-1,8):
                    for wbw_c in range(-1,8):
                        for wbb_r in range(-1,8):
                            for wbb_c in range(-1,8):
                                for bk_r in range(0,8):
                                    for bk_c in range(0,8):
                                        for white_plays in range(0,2):
                                            if(wbw_r == -1 and wbw_c != -1 or wbw_r!=-1 and wbw_c == -1) :
                                                continue
                                            if(wbb_r == -1 and wbb_c != -1 or wbb_r!=-1 and wbb_c == -1) :
                                                continue
                                            params.append((wk_r, wk_c, wbw_r, wbw_c, wbb_r, wbb_c, bk_r, bk_c,white_plays))
        return params

    def get_possible_nxt_prms(self, params=None):
        if params is None:
            params = self.get_all_params()

        count = 0
        nxt_prms = {}
        for wk_r, wk_c, wbw_r, wbw_c, wbb_r, wbb_c, bk_r, bk_c, white_plays in params:

            board = ChessBoardKB(wk=King(wk_r, wk_c, Piece.WHITE),
                                 wbw=WhiteBishop(wbw_r, wbw_c, Piece.WHITE),
                                 wbb=BlackBishop(wbb_r, wbb_c, Piece.WHITE),
                                 bk=King(bk_r, bk_c, Piece.BLACK),
                                 white_plays=white_plays)
            if not board.valid:
                continue

            nxt_pos = {}
            for nxt_moves in board.get_possible_moves():
                r = -1
                if nxt_moves.state == ChessBoard.BLACK_KING_CHECKMATE:
                    r = 1
                elif nxt_moves.state == ChessBoard.DRAW:
                    r = 0
                nxt_pos[nxt_moves.board_id()] = r

            nxt_prms[(wk_r, wk_c, wbw_r, wbw_c, wbb_r, wbb_c, bk_r, bk_c, white_plays)] = nxt_pos

            count += 1
            if count % 1000 == 0:
                print (count)

        return nxt_prms

    def save(self, parms, filename):
        """
        :param params: The data to save
        :param filename: The name of the file
        :return: None
        """
        with open(filename, 'wb') as outfile:
            pickle.dump(parms, outfile, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        """
        Load parameters
        :param filename: The name of the file
        :return: Parameters
        """
        with open(filename, 'rb') as infile:
            params = pickle.load(infile)
            return params

if __name__ == '__main__':

    # bp = BoardPossitionParams()
    # par = bp.get_possible_nxt_prms()
    # bp.save(par, 'res/memory1-0.bson')
    bpb = BoardPossitionParamsKB()
    par = bpb.get_possible_nxt_prms()
    bpb.save(par, 'resBK/memory1-0.bson')

