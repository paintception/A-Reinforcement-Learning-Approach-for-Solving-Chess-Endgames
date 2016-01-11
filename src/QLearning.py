import random
from BaseParams import BoardPossitionParams
import time


class QLearning:
    """
    The QLearning class
    """

    def __init__(self, params, gamma, learning_rate, epochs, name):
        self.params = params
        self.epochs = epochs
        self.file_name = name
        self.gamma = gamma
        self.R = self.params.load(name)
        self.all_params = list(self.R.keys())
        self.learning_rate = learning_rate

    def learning(self, epochs=None):
        """
        Actual learning function. All learning take place here.
        :param epochs: Number of episodes to run algorithm for
        :return: Algorithm runtime
        """
        last = time.time()

        if not epochs:
            epochs = self.epochs

        # Choose random initial state
        current_state_id = random.choice(self.all_params)

        # List of all positions visited in current episode
        visited_pos = []

        while epochs > 0:

            # All possible actions for current state. Basically next possible states of chessboard
            possible_states = self.R[current_state_id]

            # If is checkmate, draw or loos state it doesn`t have any next possible states so end episode.
            # Also ends episode if it visits previously visited position
            if not possible_states or current_state_id in visited_pos:
                epochs -= 1

                # Select new initial state for episode
                current_state_id = random.choice(self.all_params)
                visited_pos = []
                # Start new episode
                continue

            # Select random action for for current state
            rnd_action_id = random.choice(list(possible_states.keys()))

            visited_pos.append(current_state_id)
            # Do learning step
            current_state_id = self._cal_learning_step(current_state_id, rnd_action_id)

        now = time.time()
        return now - last

    def _cal_learning_step(self, state, action):
        mx = 0
        poss_actions = self.R[action]

        white_plays = state[6]
        if white_plays == 1:
            mx = 1
        else:
            mx = 0

        non_zero = False
        # Looking for min action for White and max for Black
        for a in poss_actions:
            if white_plays == 1 and poss_actions[a] != -1 and poss_actions[a] <= mx:
                non_zero = True
                mx = poss_actions[a]
            if white_plays == 0 and poss_actions[a] != -1 and poss_actions[a] >= mx:
                non_zero = True
                mx = poss_actions[a]

        # If min/max not initial was found update Q value
        if non_zero is True:
            r_curr = self.R[state][action]
            self.R[state][action] = r_curr + self.learning_rate * (mx * self.gamma - r_curr)

        return action

    def save(self):

        file = self.file_name.split('.')[0] + '_trained_' + str(self.epochs) + '_' + str(int(self.gamma * 10)) + '.bson'

        print('Memory Saved:', file)
        self.params.save(self.R, file)


if __name__ == '__main__':
    bp = BoardPossitionParams()
    q = QLearning(bp, 0.5, 0.8, 1000000, 'res/memory1-0.bson')

    last = time.time()
    ttime = q.learning()
    print('Time:', ttime)
    q.save()