from State import State
from Cheesboard import ChessBoard
from random import randint
import random
from BaseParams import BoardPossitionParams


class QLearning:

    def __init__(self,params):
        self.params = params
        self.gamma = 0.5
        self.R = self.params.load("burger.bson")
        self.all_params = list(self.R.keys())

    def learning(self, epochs):
        while epochs > 0:
            current_state_id = random.choice(self.all_params)
            current_state = self.R[current_state_id]
            rnd_action_id = random.choice(list(current_state.keys()))
            self.cal_learning_step(current_state_id, rnd_action_id)
            epochs -= 1

    def cal_learning_step(self, state, action):
        mx = 0
        for action in self.R[state]:
            if action[0] > mx:
                mx = action[0]

        r = self.R[state][action][0]
        self.R[state][action] = (r, mx*self.gamma)
        
if __name__ == '__main__':

    bp = BoardPossitionParams()
    q = QLearning(bp)
    print("start")
    q.learning(10)
    print("save")
    q.params.save(q.all_params, "burger10.bson")

