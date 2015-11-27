from Cheesboard import ChessBoard
from Pieces import King, Rook, Piece


class State:

    def __init__(self, board, points=0, prev_state=None):
        self.board = board
        self.points = points
        self.next_state = []
        self.prev_state = prev_state

    def __str__(self):
        return "[Round - %d, Points - %d]" %(self.get_round())

    def __unicode__(self):
        return "[Round - %d, Points - %d]" %(self.get_round())

    def get_next_states(self):
        boards = self.board.get_possible_moves()
        new_states = []
        for board in boards:
            board.draw()
            new_states.append(State(board, 0, self))

        return new_states

    def get_round(self):
        return self.board.round


class ParameterDC(State):

    def __init__(self, board, points, prev_state=None):
        super(ParameterDC, self).__init__(board, points, prev_state)
        self.p_set = self.get_parameters()

    def __str__(self):
        return "(" + self.p_set(0) + "," + self.p_set(1) + ")"

    def get_next_states(self):
        states = super(ParameterDC, self).get_next_states()
        pdcs = []
        for state in states:
            pdcs.append(ParameterDC(state.board, state.points, self))

        return pdcs

    def get_parameters(self):
        bk = self.board.get_b_king()
        wk = self.board.get_w_king()
        wr = self.board.get_w_rook()
        return (ParameterDC._get_limit(bk, wk, wr), ParameterDC._get_dist(bk, wk))

    @staticmethod
    def _get_limit(bk, wk, wr):
        bk_moves = set(bk.possible_moves())
        wk_moves = set(wk.possible_moves())
        wr_moves = set(wr.possible_moves())

        bk_moves -= (wk_moves | wr_moves)
        return len(bk_moves)

    @staticmethod
    def _get_dist(bk, wk):
        return abs(bk.row - wk.row) + abs(bk.col - wk.col)


if __name__ == '__main__':
    board = ChessBoard.get_random_chessboard()
    board.draw()
    state = ParameterDC(board, 0)
    print(state.p_set)