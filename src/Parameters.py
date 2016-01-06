import pickle
from Chessboard import Chessboard
from Pieces import Piece, King, Rook

class Parameters:
    """
    The purpose of this class is to build and save all the possible states
    of the chessboard with two kings and a rook
    """
    def __init__(self, N=None):
        """
        Constructor of parameters class
        :return:None
        """
        if not N:
            self.N = 8
        else:
            self.N = N
        self.params = []
        self.nxt_prms = {}

    def get_all_params(self):
        """
        :return:Parameters
        """
        self.params = []
        for wk_r in range(0, self.N):
            for wk_c in range(0, self.N):
                for wr_r in range(-1, self.N):
                    for wr_c in range(-1, self.N):
                        for bk_r in range(0, self.N):
                            for bk_c in range(0, self.N):
                                for white_plays in range(0, 2):
                                    if wr_r == -1 and wr_c != -1 or wr_r != -1 and wr_c == -1:
                                        continue
                                    self.params.append((wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays))
        return self.params

    def get_possible_nxt_prms(self, params=None):
        if params is None:
            if not self.params:
                self.get_all_params()
            params = self.params
        count = 0
        self.nxt_prms = {}
        for wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays in params:

            board = Chessboard(wk=King(wk_r, wk_c, Piece.WHITE),
                               wr=Rook(wr_r, wr_c, Piece.WHITE),
                               bk=King(bk_r, bk_c, Piece.BLACK),
                               white_plays=white_plays,
                               dim=self.N)
            if not board.valid:
                continue

            nxt_pos = {}
            for nxt_moves in board.get_possible_moves():
                r = 0
                if nxt_moves.state == Chessboard.BLACK_KING_CHECKMATE:
                    r = 100
                elif nxt_moves.state == Chessboard.DRAW:
                    r = -100
                nxt_pos[nxt_moves.board_id()] = r

            self.nxt_prms[(wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays)] = nxt_pos

            count += 1
            if count % 1000 == 0:
                print(count)

        return self.nxt_prms

    def save(self, filename, params=None):
        """
        :param params: The data to save
        :param filename: The name of the file
        :return: None
        """
        if not params:
            params = self.nxt_prms

        with open(filename, 'wb') as outfile:
            pickle.dump(params, outfile, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        """
        Load parameters
        :param filename: The name of the file
        :return: Parameters
        """
        with open(filename, 'rb') as infile:
            self.params = pickle.load(infile)
            return self.params

if __name__ == '__main__':
    p = Parameters(5)
    p.get_possible_nxt_prms()
    p.save('res/states.bson')
