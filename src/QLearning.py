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
        wins = 0

        current_state_id = random.choice(self.all_params)
        #current_state_id = (6, 2, 4, 6, 3, 6, 0)
        while epochs > 0:

            board = self.get_board(current_state_id)
            #board.draw()
            #print(current_state_id)


            possible_states = self.R[current_state_id]


            if not possible_states :

                board = self.get_board(current_state_id);
                #board.update_state()
                print (board.state)


                epochs -= 1
                if (board.state is ChessBoard.BLACK_KING_CHECKMATE):
                    wins += 1


                #board.draw()
                current_state_id = random.choice(self.all_params)
                continue

            rnd_action_id = random.choice(list(possible_states.keys()))

            res = self.cal_learning_step(current_state_id, rnd_action_id)
            if res is None:

                board = self.get_board(rnd_action_id)
                print('Why doesn\'t get in here?')
                print('State: ', board.state)
                epochs -= 1
                current_state_id = random.choice(self.all_params)
            else:
                current_state_id = res

        print ('Wins:',wins)

    def cal_learning_step(self, state, action):
        """

        :type action: object
        """
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

    def get_board(self,state_id):
         wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = state_id

         return  ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                            wr=Rook(wr_r, wr_c, Piece.WHITE),
                            bk=King(bk_r, bk_c, Piece.BLACK),
                            white_plays=white_plays,
                            debug=True
                            );
    
    
if __name__ == '__main__':

    bp = BoardPossitionParams()
    q = QLearning(bp,'res/final_final.bson')

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

    #for x in q.R.keys():
    #    print (len(q.R[x]))

    q.learning(100)
    #q.params.save(q.all_params, "res/final100.bson")

