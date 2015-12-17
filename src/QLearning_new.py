import random
from Cheesboard import ChessBoard
from Pieces import King, Rook, Piece
from BaseParams import BoardPossitionParams


class QLearning:
	def __init__(self,params,gamma,epochs,name):
		#possible_actions = 
		self.gamma = gamma
		self.epochs = epochs
		self.params = params
		self.file_name = name
		self.R = self.params.load(name)
		self.all_states = list(self.R.keys())
		self.hasMaxValue = False


	def learn_something_please(self):
		epochs = self.epochs
		s0 = random.choice(self.all_states)
		while epochs:
			# Choose a random action from the current state
			possible_actions = list(self.R[s0].keys())

			# No possible moves, draw or win
			if not possible_actions:
				#board = self.get_board(s0)
				#board.draw()
				#input()
				s0 = random.choice(self.all_states)
				epochs -= 1
				#print (self.count_non_zeros())
				continue
			s1 = random.choice(possible_actions)
			# We need to find the max/min from the next state
			q_value = self.gamma * self.find_max_min(s0,s1)

			self.R[s0][s1] += q_value 

			s0 = s1

	def find_max_min(self,s0,s1):
		#Check who is playing
		white_plays = s0[6]

		# Find the next possible moves from s1(action)
		possible_states = self.R[s1]

		if not possible_states:
			return 0

		# Set max value to a very small number
		if white_plays is 1:
			mxn = -100000000000000000000000000000000000
		else:
			mxn =  100000000000000000000000000000000000

		for a in possible_states:
			x = possible_states[a]
			#print (x)
			if abs(x - 0) < 0.0000000001:
				continue
			
			if white_plays is 1 and x > mxn:
				mxn = x
			if not (white_plays is 1) and x < mxn:
				mxn = x

		return mxn

	def count_non_zeros(self):
		count = 0
		for s0 in self.R.keys():
			for s1 in self.R[s0]:
				x = self.R[s0][s1]
				if abs(x - 0) > 0.000000001:
					count += 1
		return count  

	def get_board(self,state_id):
         wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = state_id

         return ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                            wr=Rook(wr_r, wr_c, Piece.WHITE),
                            bk=King(bk_r, bk_c, Piece.BLACK),
                            white_plays=white_plays,
                            debug=True
                            );
	def Learn(self):

		for e in range(self.epochs): 						# run for all episodes
			current_state = random.choice(self.all_params) 	# initialize s
			for step in current_state:						# repeat for all steps available from a specific state
				possible_states = self.R[current_state]		# retrieve all possible states
	def save(self):

		file = self.file_name.split('.')[0] + '_trained_' + str(self.epochs) + '_' + str(int(self.gamma*10)) +'.bson'

		print ('Memory Saved:', file)
		self.params.save(self.R, file)


if __name__ == '__main__':
	
    bp = BoardPossitionParams()
    q = QLearning(bp,0.8,1000000,'res/memory.bson')
    q.learn_something_please()
    q.save()
