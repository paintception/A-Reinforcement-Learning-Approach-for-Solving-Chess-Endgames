from Chessboard import Chessboard
from Parameters import Parameters
import random
import numpy as np

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
        s0 = (2,2,0,0,4,2,1)
        while epochs:
            # Choose a random action from current state
            possible_actions = list(self.R[s0].keys())

            x = self.get_possible_moves_2_layers(s0);

            if not x:

                epochs -= 1
                s0 = random.choice(self.all_states)
                print(epochs)
                continue

            dd = np.array(x)

            dd = dd[:,1]

            ind = np.argmax(dd)
            val = np.amax(dd)


            print (ind , '->',val)

            q_value = self.gamma * val;

            if s0[6] is 1:
                q_value = - q_value

            self.R[s0][x[ind][0]] += q_value

            #Chessboard.get_board(s0,5).draw()
            #Chessboard.get_board(x[ind][0],5).draw()

            s0 = x[ind][0]

    def get_possible_moves_2_layers(self, s0):
        # Choose a random action from current state
        possible_moves_1 = list(self.R[s0].keys())
        l = []
        for s1 in possible_moves_1:
            if s1[2] is s1[4] and s1[3] is s1[5]:
                continue
            possible_moves_2 = (self.R[s1].keys())
            if s1[2] is -1 and s1[3] is -1:
                l.append([s1, self.R[s0][s1] - 100 ])
            for s2 in possible_moves_2:
                l.append([s1, self.R[s0][s1] - self.R[s1][s2] ])

        return l

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
