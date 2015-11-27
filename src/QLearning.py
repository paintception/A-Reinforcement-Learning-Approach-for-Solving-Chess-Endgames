from State import ParameterDC
from Cheesboard import ChessBoard


class QLearning:
	
	def __init__(self):
		self.states = {}
		self.current_state = ParameterDC(ChessBoard.get_random_chessboard(),points=0)
		self.add_state(self.current_state)

	def add_state(self, pt):
		if pt.__str__() not in self.states.keys():
			self.states[pt.__str__()] = pt.get_next_states()
			return True
		return False

	def learning_step(self):
		print(self.current_state)
		print(self.states)



if __name__ == '__main__':

	q = QLearning()

	q.learning_step()