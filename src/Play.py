import os.path
from BaseParams import BoardPossitionParams
import pickle
import random
from Cheesboard import ChessBoard,King,Rook,Piece


class Play:

    def __init__(self,file_name,debug=None):
        self.file_name = file_name
        self.R = self.load(file_name)
        self.debug = debug

    def play_stats(self,games_to_play):
        wins = 0
        turns = 0
        for i in range(0,games_to_play):
            win, turn = self.play()
            if win:
                wins +=1
                turns += turn

        if wins is 0:
            return 0,0
        return (wins/games_to_play), (turns/wins)

    def play(self, state_id=None):

        current_state_id = None
        turn = 0
        win = False

        if not  state_id:
            current_state_id = random.choice(list(self.R))
        else:
            current_state_id = state_id

        while True:

            if not current_state_id or turn >= 40:
                break

            board = get_board(current_state_id)

            if current_state_id[6] is 1:
                turn += 1

            next_states = self.R[current_state_id]

            if not next_states:
                board = get_board(current_state_id)

                if self.debug:
                    board.draw()

                if board.state == ChessBoard.BLACK_KING_CHECKMATE:
                    win = True
                break

            max_state_id = None
            if current_state_id[6] is 0:
                max_state_id = self.get_min_state(next_states)
            else:
                max_state_id = self.get_max_state(next_states)

            if self.debug:
                print ('Turn: ',turn)
                board.draw()
                for i in next_states:
                    print (i,'->',next_states[i])
                print ('Max:', max_state_id)
                input()

            current_state_id = max_state_id

        return win, turn

    @staticmethod
    def get_max_state(states):
        max_q = -10000000000000
        max_state = None
        for state in states:

            if states[state] > max_q:
                max_q= states[state]
                max_state = state

        return max_state

    @staticmethod
    def get_min_state(states):
        min_q = 10000000000000000
        min_state = None
        for state in states:

            if states[state] < min_q:
                min_q= states[state]
                min_state = state

        return min_state

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as infile:
            params = pickle.load(infile)
            return params


def get_board(state_id):
         wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = state_id
         return ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                            wr=Rook(wr_r, wr_c, Piece.WHITE),
                            bk=King(bk_r, bk_c, Piece.BLACK),
                            white_plays=white_plays,
                            debug=True
                            )
if __name__ == '__main__':

    p = Play('res/memory_trained_100000_5.bson',True)
    wins, turns = p.play_stats(1)
    #wins, turns = p.play()
    print (wins, turns)


