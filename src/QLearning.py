from State import State
from Cheesboard import ChessBoard
from random import randint
import random
from BaseParams import BoardPossitionParams


class QLearning:

    def __init__(self,params,name):
        self.params = params
        self.gamma = 0.5
        self.R = self.params.load(name)
        self.all_params = list(self.R.keys())

    def learning(self, epochs):
        current_state_id = random.choice(self.all_params)
        while epochs > 0:
            current_state = self.R[current_state_id]
            rnd_action_id = random.choice(list(current_state.keys()))

            res = self.cal_learning_step(current_state_id, rnd_action_id)
            if res is None:
                epochs -= 1

                current_state_id = random.choice(self.all_params)
            else:
                current_state_id = res

    def cal_learning_step(self, state, action):
        mx = 0
        non_zero = False
        print (action)
        print (self.R[action])
        for action in self.R[action]:
            if action[1] != 0:
                non_zero = True
            if action[0] > mx:
                mx = action[0]

        if non_zero:
            r = self.R[state][action][0]
            self.R[state][action] = (r, mx*self.gamma)
            return None
        else:
            return action
        
if __name__ == '__main__':

    bp = BoardPossitionParams()
    q = QLearning(bp,'res/final.bson')

    for x in q.R.keys():
        print (len(q.R[x]))
    print("start")


    #q.learning(1)
    print("save")
    q.params.save(q.all_params, "res/final1.bson")

