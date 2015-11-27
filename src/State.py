from Cheesboard import ChessBoard
from Pieces import King, Rook, Piece


class State:

    def __init__(self, board, points, prev_state=None):
        self.board = board
        self.points = points
        self.next_state = []
        self.prev_state = prev_state

    def __str__(self):
        return "[Round - %d, Points - %d]" %(self.get_round(), self.points)

    def __unicode__(self):
        return "[Round - %d, Points - %d]" %(self.get_round(), self.points)

    def get_next_states(self):
        boards = self.board.get_possible_moves()
        new_states = []
        for board in boards:
             new_states.append(State(board, self.points + 1, self))

        print len(boards)
        return new_states

    def get_round(self):
        return self.board.round

if __name__ == '__main__':
    board = ChessBoard.get_random_chessboard() 
    board.draw()
    state = State(board, 0)
    state.get_next_states()
