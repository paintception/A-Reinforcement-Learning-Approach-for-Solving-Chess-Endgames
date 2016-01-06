from Chessboard import Chessboard
from Parameters import Parameters
import random


class QLearning:
    """
    The QLearning class
    """
    def __init__(self, gamma, epochs, name,dim=None):
        self.params = Parameters()
        self.gamma = gamma
        self.epochs = epochs
        self.file_name = name
        self.R = self.params.load(name)
        self.all_states = list(self.R.keys())
        if not dim:
            self.N = 8
        else:
            self.N = dim

    def learning(self):
        """
        :return: The states with values
        """
        epochs = self.epochs
        s0 = random.choice(self.all_states)
        #s0 = (0,7,6,5,7,0,1)  # White is playing
        #s0 = (5,2,0,0,7,3,0) # Black is playing
        while epochs:
            # Choose a random action from current state
            possible_actions = list(self.R[s0].keys())
            #Chessboard.get_board(s0).draw()
            # No possible moves, draw or win
            if not possible_actions:
                #Chessboard.get_board(s0).draw()
                epochs -= 1
                s0 = random.choice(self.all_states)
                continue

            s1 = random.choice(possible_actions)

            if s1[2] is s1[4] and s1[3] is s1[5]:
                #Chessboard.get_board(s0).draw()
                epochs -= 1
                s0 = random.choice(self.all_states)
                continue
            """ DEBUG """
            #s1 = (5,2,7,0,7,2,0) # White
            #s1 = (0,7,6,1,7,0,0)
            #s1 = (5,2,0,0,7,2,1) # Black
            #Chessboard.get_board(s0).draw()
            #Chessboard.get_board(s1).draw()

            q_value = self.gamma * self.find_min_max(s0, s1)
            if s0[6] is 1:
                self.R[s0][s1] += q_value
            else:
                self.R[s0][s1] -= q_value

            s0 = s1

    def find_min_max(self, s0, s1):
        """
        :param s0: Current state
        :param s1: Next state
        :return:
        """
        # Check who is playing
        white_plays = s0[6]

        # Find the next possible moves from s1(action)
        possible_states = self.R[s1]

        if not possible_states and white_plays:
            return 100
        if not possible_states and not white_plays:
            return -100


        # Set max value to a very small number
        if white_plays is 0:
            mxn = -10000000
        else:
            mxn = 10000000

        for a in possible_states:
            x = possible_states[a]

            if white_plays is 0 and x > mxn:
                mxn = x
            if not (white_plays is 0) and x < mxn:
                mxn = x

        return mxn

    def save(self):

        file = self.file_name.split('.')[0] + '_trained_' + str(self.epochs) + '_' + str(int(self.gamma * 10)) + '.bson'

        print('Memory Saved:', file)
        self.params.save(file, self.R)

if __name__ == '__main__':
    q = QLearning(0.5, 100000, 'res/states.bson')
    q.learning()
    q.save()
