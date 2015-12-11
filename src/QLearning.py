from State import State
from Cheesboard import ChessBoard
from random import randint
from Pieces import King, Rook, Piece
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
        #current_state_id = self.all_params[0]

        while epochs > 0:

            print(current_state_id)

            possible_states = self.R[current_state_id]

            if not possible_states :
                wk_r, wk_c, wr_r, wr_c, bk_r, bk_c = current_state_id
                board = ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                               wr=Rook(wr_r, wr_c, Piece.WHITE),
                               bk=King(bk_r, bk_c, Piece.BLACK))
                print('State: ', board.state)
                epochs -= 1
                current_state_id = random.choice(self.all_params)
                continue

            rnd_action_id = random.choice(list(possible_states.keys()))
            #rnd_action_id = list(possible_states.keys())[0]



            res = self.cal_learning_step(current_state_id, rnd_action_id)
            if res is None:

                wk_r, wk_c, wr_r, wr_c, bk_r, bk_c = current_state_id
                board = ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                               wr=Rook(wr_r, wr_c, Piece.WHITE),
                               bk=King(bk_r, bk_c, Piece.BLACK))
                print('State: ', board.state)
                epochs -= 1
                current_state_id = random.choice(self.all_params)
            else:
                current_state_id = res

    def cal_learning_step(self, state, action):
        mx = 0
        non_zero = False

        poss_actions = self.R[action]

        for a in poss_actions:
            if poss_actions[a][1] != 0:
                non_zero = True
            if poss_actions[a][0] >= mx:
                mx = poss_actions[a][0]

        if non_zero:
            r = self.R[state][action][0]
            self.R[state][action] = (r, mx*self.gamma)
            return None
        else:
            return action
        
if __name__ == '__main__':

    bp = BoardPossitionParams()
    q = QLearning(bp,'res/final.bson')

    #for x in q.R.keys():
    #    print (len(q.R[x]))
    print("start")

    q.learning(100)
    print("save")
    q.params.save(q.all_params, "res/final100.bson")

