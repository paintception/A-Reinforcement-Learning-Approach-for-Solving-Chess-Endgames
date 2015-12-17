from State import State
from Cheesboard import ChessBoard
from random import randint
from Pieces import King, Rook, Piece
import random
from BaseParams import BoardPossitionParams
import time


class QLearning:

    def __init__(self,params,gamma,epochs,name):
        self.params = params
        self.epochs = epochs
        self.file_name = name
        self.gamma = gamma
        self.R = self.params.load(name)
        self.all_params = list(self.R.keys())

    def learning(self, epochs=None):
        last = time.time()
        wins = 0

        if not epochs:
            epochs = self.epochs
        total = epochs
        current_state_id = random.choice(self.all_params)

        visited_pos = []

        while epochs > 0:

            possible_states = self.R[current_state_id]

            if not possible_states or current_state_id in visited_pos:

                epochs -= 1

                current_state_id = random.choice(self.all_params)
                visited_pos = []
                continue

            rnd_action_id = random.choice(list(possible_states.keys()))

            visited_pos.append(current_state_id)
            current_state_id = self.cal_learning_step(current_state_id, rnd_action_id)


        now = time.time()
        return (now-last), (wins/total)

    def cal_learning_step(self, state, action):
        mx = 0
        poss_actions = self.R[action]

        white_plays = state[6]
        if white_plays == 1:
            mx = -10000000000000
        else:
            mx = 1000000000000000

        non_zero = False
        for a in poss_actions:
            if white_plays == 1 and poss_actions[a] != 0 and poss_actions[a] >= mx:
                non_zero = True
                mx = poss_actions[a]
            if white_plays == 0 and poss_actions[a] != 0 and poss_actions[a] <= mx:
                non_zero = True
                mx = poss_actions[a]

        if non_zero is False:
            mx = 0

        r_curr = self.R[state][action]
        self.R[state][action] = r_curr + 0.8*(mx * self.gamma - r_curr)

        return action

    def get_board(self,state_id):
         wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = state_id

         return ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                            wr=Rook(wr_r, wr_c, Piece.WHITE),
                            bk=King(bk_r, bk_c, Piece.BLACK),
                            white_plays=white_plays,
                            debug=True
                            );
    
    def save(self):

        file = self.file_name.split('.')[0] + '_trained_' + str(self.epochs) + '_' + str(int(self.gamma*10)) +'.bson'

        print ('Memory Saved:', file)
        self.params.save(self.R, file)


if __name__ == '__main__':

    bp = BoardPossitionParams()
    q = QLearning(bp,0.5,500000,'res/memory100-100.bson')

    last = time.time()
    ttime , wins = q.learning()
    print ('Time:', ttime, 'Wins Perc:',wins)
    q.save()


    """
    current_state_id = (4, 0, 6, 1, 7, 0, 0)
    board = q.get_board(current_state_id)
    print(board.board_id())
    board.draw()
    poss = ( q.R[current_state_id])
    for x in poss:
        board = q.get_board(x)
        print(board.board_id())
        board.draw()
    """
