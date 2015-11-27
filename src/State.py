from Cheesboard import ChessBoard
from Pieces import King, Rook, Piece


class State:

	def __init__(self, board, points, prev_state=None):
		self.board = board
		self.point = points
		self.next_state = []
                self.prev_state = prev_state

	def get_next_states(self):
            print self.board.get_possible_moves()
if __name__ == '__main__':
    board = ChessBoard.get_random_chessboard() 
    state = State(board,0)
    print state.get_next_states()
