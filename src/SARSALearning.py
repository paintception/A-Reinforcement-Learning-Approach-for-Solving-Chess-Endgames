import random
from BaseParams import BoardPossitionParams
import time


class SARSALearning:
    """
    The SARSALearning class
    """

    def __init__(self, params, gamma, learning_rate, epochs, eps, name):
        self.params = params
        self.epochs = epochs
        self.file_name = name
        self.gamma = gamma
        self.R = self.params.load(name)
        self.all_params = list(self.R.keys())
        self.learning_rate = learning_rate
        self.eps = eps

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
        possible_states = self.R[current_state_id]
        if random.random() <= self.eps:
            # Select random action for for current state
            action_id = random.choice(list(possible_states.keys()))
        else:
            action_id, mx = self._get_max(current_state_id)
            if action_id is None:
                action_id = random.choice(list(possible_states.keys()))

        # List of all positions visited in current episode
        visited_pos = []

        while epochs > 0:

            # If is checkmate, draw or loos state it doesn`t have any next possible states so end episode.
            # Also ends episode if it visits previously visited position
            if action_id is None:
                epochs -= 1

                # Select new initial state for episode
                current_state_id = random.choice(self.all_params)
                visited_pos = []

                # All possible actions for current state. Basically next possible states of chessboard
                possible_states = self.R[current_state_id]

                if random.random() <= self.eps and possible_states:
                    # Select random action for for current state
                    action_id = random.choice(list(possible_states.keys()))
                elif possible_states:
                    action_id, mx = self._get_max(current_state_id)
                    if action_id is None:
                        action_id = random.choice(list(possible_states.keys()))
                continue

            visited_pos.append(current_state_id)
            # Do learning step
            current_state_id, action_id = self._cal_learning_step(current_state_id, action_id)

        now = time.time()
        return now - last

    def _cal_learning_step(self, state, next_state):
        # mx = 0
        poss_actions = self.R[next_state]
        if not poss_actions:
            return next_state, None

        if random.random() <= self.eps:
            rnd_action_id = random.choice(list(poss_actions.keys()))
            mx = poss_actions[rnd_action_id]
        else:
            rnd_action_id, mx = self._get_max_reverse(next_state)
            if rnd_action_id is None:
                rnd_action_id = random.choice(list(poss_actions.keys()))
                mx = poss_actions[rnd_action_id]

        if not mx == -1:
            r_curr = self.R[state][next_state]
            self.R[state][next_state] = r_curr + self.learning_rate * (mx * self.gamma - r_curr)

        return next_state, rnd_action_id

    def _get_max(self, state):
        poss_actions = self.R[state]

        white_plays = state[6]
        if white_plays == 1:
            mx = 1
        else:
            mx = 0

        max_action = None

        for a in poss_actions:
            if white_plays == 1 and poss_actions[a] != -1 and poss_actions[a] <= mx:
                max_action = a
                mx = poss_actions[a]
            if white_plays == 0 and poss_actions[a] != -1 and poss_actions[a] >= mx:
                max_action = a
                mx = poss_actions[a]

        return max_action, mx

    def _get_max_reverse(self, state):
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

        return max_action, mx

    def save(self):

        file = self.file_name.split('.')[0] + '_SARSA_trained_ep' + str(self.epochs) + '_g' + str(int(self.gamma * 10)) + \
               '_l' + str(int(self.learning_rate * 10)) + '_e' + str(int(self.eps * 100)) + '.bson'

        print('Memory Saved:', file)
        self.params.save(self.R, file)


if __name__ == '__main__':
    bp = BoardPossitionParams()
    q = SARSALearning(bp, gamma=0.99, learning_rate=0.8, epochs=2000000, eps=0.05, name='res/memory1-0.bson')

    last = time.time()
    ttime = q.learning()
    print('Time:', ttime)
    q.save()