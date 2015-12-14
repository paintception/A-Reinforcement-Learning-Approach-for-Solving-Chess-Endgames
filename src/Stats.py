import os.path
from BaseParams import BoardPossitionParams
from QLearning import QLearning
from Play import Play

if __name__ == '__main__':

    epochs = 100000
    games_to_play = 1000
    gamma = 0.8
    base_memory = 'res/memory.bson'
    file = base_memory.split('.')[0] + '_trained_' + str(epochs) + '_' + str(int(gamma*10)) + '.bson'

    #Check if is trained
    if not os.path.isfile(file):
        print ('[Info] The agent is training for',epochs,'epochs')
        bp = BoardPossitionParams()
        q = QLearning(bp, gamma, epochs, base_memory)
        q.save()
    # Play
    play = Play(file, False)
    wins, rounds = play.play_stats(games_to_play)

    print ('Win perc:', wins,'Average Rounds:', rounds)

