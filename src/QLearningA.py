import random
from BaseParams import BoardPossitionParams
import time


class QLearningA:
    """
    The QLearning class
    """

    def __init__(self, params, gamma, learning_rate, epochs, eps, eps_d, name):
        self.params = params
        self.epochs = epochs
        self.file_name = name
        self.gamma = gamma
        self.R = self.params.load(name)
        self.all_params = list(self.R.keys())
        self.learning_rate = learning_rate
        self.eps = eps
        self.eps_d = eps_d

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

        eps = self.eps

        while epochs > 0:

            # All possible actions for current state. Basically next possible states of chessboard
            possible_states = self.R[current_state_id]

            # If is checkmate, draw or loos state it doesn`t have any next possible states so end episode.
            # Also ends episode if it visits previously visited position
            # if not possible_states or current_state_id in visited_pos:
            if not possible_states:
                epochs -= 1

                # Select new initial state for episode
                current_state_id = random.choice(self.all_params)
                visited_pos = []

                # Decrease eps
                if epochs % 100000 == 0:
                    eps -= self.eps_d

                # Start new episode
                continue

            if random.random() <= eps:
                # Select random action for for current state
                rnd_action_id = random.choice(list(possible_states.keys()))
            else:
                rnd_action_id = self._get_max(current_state_id)
                if rnd_action_id is None:
                    rnd_action_id = random.choice(list(possible_states.keys()))

            visited_pos.append(current_state_id)
            # Do learning step
            current_state_id = self._cal_learning_step(current_state_id, rnd_action_id)

        now = time.time()
        return now - last

    def _cal_learning_step(self, state, next_state):
        mx = 0
        poss_actions = self.R[next_state]

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
            r_curr = self.R[state][next_state]
            self.R[state][next_state] = r_curr + self.learning_rate * (mx * self.gamma - r_curr)

        return next_state

    def _get_max(self, state):
        poss_actions = self.R[state]

        white_plays = state[6]
        if white_plays == 1:
            mx = 0
        else:
            mx = 1

        max_action = None

        for a in poss_actions:
            if white_plays == 1 and poss_actions[a] != -1 and poss_actions[a] >= mx:
                max_action = a
                mx = poss_actions[a]
            if white_plays == 0 and poss_actions[a] != -1 and poss_actions[a] <= mx:
                max_action = a
                mx = poss_actions[a]

        return max_action

    def save(self):

        file = self.file_name.split('.')[0] + '_Q_trained_ep' + str(self.epochs) + '_g' + str(int(self.gamma * 100)) + \
               '_l' + str(int(self.learning_rate * 10)) + '_e' + str(int(self.eps * 100)) + \
               '_ed' + str(int(self.eps_d * 100)) + '.bson'

        print('Memory Saved:', file)
        self.params.save(self.R, file)


if __name__ == '__main__':
    bp = BoardPossitionParams()
    q = QLearningA(bp, gamma=0.99, learning_rate=0.8, epochs=2000000, eps=1.0, eps_d=0.05, name='res/memory1-0.bson')

    last = time.time()
    ttime = q.learning()
    print('Time:', ttime)
    q.save()