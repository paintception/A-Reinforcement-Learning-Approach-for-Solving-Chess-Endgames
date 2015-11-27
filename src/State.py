
class State:

	def __init__(self,board, round_num, points):
		self.board = board
		self.round = round_num
		self.point = points
		self.next_state = []

	def get_next_states(self):
