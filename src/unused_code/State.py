from Cheesboard import ChessBoard
from Pieces import King, Rook, Piece
import json

class State:

    def __init__(self, board, points=0, prev_state=None):
        self.board = board
        self.points = points
        self.next_state = []
        self.prev_state = prev_state


    def __repr__(self):
        w_king = self.board.get_w_king()
        w_rook = self.board.get_w_rook()
        b_king = self.board.get_b_king()
        return "wk:(%d,%d),wr:(%d,%d),bk:(%d,%d)" % (w_king.row,w_king.col,w_rook.row,w_rook.col,b_king.row,b_king.col) 

    def get_id(self):
        w_king = self.board.get_w_king()
        w_rook = self.board.get_w_rook()
        b_king = self.board.get_b_king()
        return "%d,%d,%d,%d,%d,%d" % (w_king.row,w_king.col,w_rook.row,w_rook.col,b_king.row,b_king.col) 

    def get_json(self,next_states):
        w_king = self.board.get_w_king()
        w_rook = self.board.get_w_rook()
        b_king = self.board.get_b_king()

        y = []
        for state in next_states:
            w_king = state.board.get_w_king()
            w_rook = state.board.get_w_rook()
            b_king = state.board.get_b_king()

            y.append( {'w_king' :  w_king.to_json() , 'w_rook' : w_rook.to_json() , 'b_king' : b_king.to_json()}) 
       
        x =  {'w_king' :  w_king.to_json() , 'w_rook' : w_rook.to_json() , 'b_king' : b_king.to_json(), 'next_states' : y} 
        return json.dumps(x,indent=4)

    def get_next_states(self):
        boards = self.board.get_possible_moves()
        new_states = []
        for b in boards:
            new_states.append(State(b, 0, self))
    
        
        return new_states

    def get_round(self):
        return self.board.round


class ParameterDC(State):

    def __init__(self, board, points, prev_state=None):
        super(ParameterDC, self).__init__(board, points, prev_state)
        self.p_set = self.get_parameters()

    def __str__(self):
        return "(" + str(self.p_set[0]) + "," + str(self.p_set[1]) + ")"

    def __repr__(self):
        return "(" + str(self.p_set[0]) + "," + str(self.p_set[1]) + ")"



    def get_next_states(self):
        states = super(ParameterDC, self).get_next_states()
        pdcs = []
        l = []
        for state in states:
            pd = ParameterDC(state.board, state.points, self)
            if pd.__str__() not in l:
                pdcs.append(pd)
                l.append(pd.__str__())

        return pdcs

    def get_parameters(self):
        bk = self.board.get_b_king()
        wk = self.board.get_w_king()
        wr = self.board.get_w_rook()
        return (ParameterDC._get_limit(bk, wk, wr), ParameterDC._get_dist(bk, wk))

    @staticmethod
    def _get_limit(bk, wk, wr):
        bk_moves = set(bk.possible_moves())
        wk_moves = set(wk.possible_moves())
        wr_moves = set(wr.possible_moves())

        bk_moves -= (wk_moves | wr_moves)
        return len(bk_moves)

    @staticmethod
    def _get_dist(bk, wk):
        return abs(bk.row - wk.row) + abs(bk.col - wk.col)

def save_to_file(filename,data):
    with open(filename,'w') as outfile:
        outfile.write(data)

if __name__ == '__main__':
    board = ChessBoard.get_random_chessboard()
    s = State(board) 
    s.board.draw()
    print (s.get_id()) 
