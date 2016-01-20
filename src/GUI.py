import cocos
import pyglet
import random
import pickle
from cocos.director import director
from Cheesboard import ChessBoard,King,Rook,Piece


class Game(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self, file_name):
        super(Game, self).__init__()
        self.init_board()
        self.file_name = file_name
        self.R = self.load(file_name)
        self.butt = 1
        self.finish = 0
        label = cocos.text.Label('Round:',
                                  font_name='Times New Roman',
                                  font_size=26,
                                  anchor_x='left', anchor_y='bottom')
        label.position = 0, 0
        self.add(label,z=4)

        label = cocos.text.Label('Player:',
                                  font_name='Times New Roman',
                                  font_size=26,
                                  anchor_x='left', anchor_y='bottom')
        label.position = 64*4, 0
        self.add(label,z=4)


        self.wking = cocos.sprite.Sprite('GUI/wking.gif')
        self.wking.position = self.convert_pos(0,0)
        self.wking.scale = 0.1
        self.add(self.wking, z=1)

        self.wrook = cocos.sprite.Sprite('GUI/wrook.gif')
        self.wrook.position = self.convert_pos(0,2)
        self.wrook.scale = 0.1
        self.add(self.wrook, z=2)

        self.bking = cocos.sprite.Sprite('GUI/bking.gif')
        self.bking.position = self.convert_pos(5,4)
        self.bking.scale = 0.1
        self.add(self.bking, z=3)


        # Start with a random state
        self.next_state_id = None
        self.current_state_id = random.choice(list(self.R))
        self.set_position(self.current_state_id)
        self.board = self.get_board(self.current_state_id)

        if self.white_plays:
            txt = 'WHITE'
        else:
            txt = 'BLACK'
        self.who_plays = cocos.text.Label(txt,
                                  font_name='Times New Roman',
                                  font_size=32,
                                  anchor_x='right', anchor_y='bottom')
        self.who_plays.position = 64*8, 0
        self.add(self.who_plays,z=4)

        self.round = cocos.text.Label(str(self.board.turn),
                                  font_name='Times New Roman',
                                  font_size=32,
                                  anchor_x='left', anchor_y='bottom')
        self.round.position = 64*2, 0
        self.add(self.round, z=4)

        self.play()

    def on_key_press(self, key, modifiers):
        if self.finish is 1:
            return
        print('Continue:', key)
        self.butt += 1
        if self.butt is 1:
            self.current_state_id = self.next_state_id
            self.set_position(self.current_state_id)
        else:
            self.current_state_id = self.next_state_id
            self.set_position(self.current_state_id)
            self.play()

    def play(self):
        if self.current_state_id[6] is 1:
            self.board.turn += 1
            self.round.element.text = str(self.board.turn)
            self.who_plays.element.text = 'WHITE'
        else:
            self.who_plays.element.text = 'BLACK'

        next_states = self.R[self.current_state_id]

        if self.current_state_id[6] is 0:
            self.next_state_id = self.get_min_state(next_states)
        else:
            self.next_state_id  = self.get_max_state(next_states)

        board = self.get_board(self.current_state_id)

        if board.state is ChessBoard.BLACK_KING_CHECKMATE or self.board.turn>40:
            self.set_position(self.current_state_id)
            self.bking.z = 0
            self.finish = 1
            box = cocos.layer.ColorLayer(255, 255, 255, 200, width=64*8, height=72)
            box.position = 0, 64*8
            self.add(box,z = 3)

            print("Self State:", board.state)
            if board.state is self.board.BLACK_KING_CHECKMATE:
                label = cocos.text.Label('CHECKMATE',
                              font_name='Comic Sans MS',
                              font_size=52,
                              color=(90,135,161, 255),
                              anchor_x='center', anchor_y='top')
            else:
                label = cocos.text.Label('DRAW',
                          font_name='Comic Sans MS',
                          font_size=52,
                          color=(90,135,161, 255),
                          anchor_x='center', anchor_y='top')

            label.position = 64*4, 64*9
            self.add(label,z=4)

            return
        for i in next_states:
            print (i,'->', next_states[i])
        print('MaxMin:',  self.next_state_id ,'->',next_states[self.next_state_id ])

    def init_board(self):
        y = 64
        for i in range(8):
            x = 0
            for j in range(8):
                if j % 2 == 0:
                    if i % 2 == 0:
                        box = cocos.layer.ColorLayer(255, 215, 97, 255, width=64, height=64)
                    else:
                        box = cocos.layer.ColorLayer(128, 64, 0, 255, width=64, height=64)
                else:
                    if i % 2 == 0:
                       box = cocos.layer.ColorLayer(128, 64, 0, 255, width=64, height=64)
                    else:
                        box = cocos.layer.ColorLayer(255, 215, 97, 255, width=64, height=64)

                box.position = x, y
                self.add(box)
                x += 64
            y += 64

    def set_position(self,state):
        self.wking.position = self.convert_pos(state[0],state[1])
        self.wrook.position = self.convert_pos(state[2],state[3])
        self.bking.position = self.convert_pos(state[4],state[5])
        self.white_plays = state[6]
        pass

    def convert_pos(self,row,col):
        return col * 64 + 32, 64*8 - row * 64 - 32 +64



    def get_board(self,state_id):
         wk_r, wk_c, wr_r, wr_c, bk_r, bk_c, white_plays = state_id
         return ChessBoard(wk=King(wk_r, wk_c, Piece.WHITE),
                            wr=Rook(wr_r, wr_c, Piece.WHITE),
                            bk=King(bk_r, bk_c, Piece.BLACK),
                            white_plays=white_plays,
                            debug=True
                            )
    @staticmethod
    def get_max_state(states):
        max_q = -1
        max_state = None

        # if random.random() < 0.1 :
        #    return random.choice(list(states.keys()))

        for state in states:

            if states[state] > max_q and states[state] != 0:
                max_q= states[state]
                max_state = state
            elif states[state] == 100:
                max_state = state
                break

        return max_state

    @staticmethod
    def get_min_state(states):
        min_q = 1
        min_state = None
        for state in states:

            if states[state] < min_q:
                min_q= states[state]
                min_state = state
            elif states[state] == -100:
                min_state = state
                break

        return min_state

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as infile:
            params = pickle.load(infile)
            return params

if __name__ == '__main__':
    base_memory = 'res/memory1-0.bson'
    epoch = 5000000
    gamma = 0.6
    fp = base_memory.split('.')[0] + '_trained_' + str(epoch) + '_' + str(int(gamma*10)) + '.bson'

    director.init(width=64*8, height=64*9, caption="Chess Game Engine",resizable=False)
    director.run(cocos.scene.Scene(Game(fp)))
