from Cheesboard import ChessBoard
from Pieces import King, Rook, Piece
import sys, traceback

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
		for bk_r in range(0,7):
			for bk_c in range(0,7):
				for wk_r in range(0,7):
					for wk_c in range(0,7):
						for wr_r in range(0,7):
							for wr_c in range(0,7):
								params.append((bk_r, bk_c, wk_r, wk_c, wr_r, wr_c))
		return params

	def get_possible_nxt_prms(self, params=None):
		if params is None:
			params = self.get_all_params()

		nxt_prms = {}
		for bk_r, bk_c, wk_r, wk_c, wr_r, wr_c in params:
			
			board = ChessBoard(King(wk_r, wk_c, Piece.WHITE), Rook(wr_r, wr_c, Piece.WHITE), King(bk_r, bk_c, Piece.BLACK))
			if not board.valid:
				continue

			nxt_pos = {}
			for nxt_moves in board.get_possible_moves():
				r = 0
				if nxt_moves.state == ChessBoard.BLACK_KING_CHECKMATE:
					r = 100
				elif nxt_moves.state == ChessBoard.DRAW:
					r = -100
				nxt_pos[nxt_moves.board_id()] = (r, 0)

			nxt_prms[board.board_id()] = nxt_pos
		
if __name__ == '__main__':
	bp = BoardPossitionParams()
	p = bp.get_possible_nxt_prms()
	print(p)
