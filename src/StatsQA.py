
from Play import Play


if __name__ == '__main__':

    epoch = 2000000
    gamma = 0.99
    learning_rate = 0.8
    eps = 1.0
    eps_d = 0.05

    games_to_play = 10000

    base_memory = 'res/memory1-0.bson'
    fp = base_memory.split('.')[0] + '_Q_trained_ep' + str(epoch) + '_g' + str(int(gamma * 100)) + \
               '_l' + str(int(learning_rate * 10)) + '_e' + str(int(eps * 100)) + \
               '_ed' + str(int(eps_d * 100)) +'.bson'

    play = Play(fp, False)
    wins, rounds = play.play_stats(games_to_play)

    print('Win perc:', wins,'Average Rounds:', rounds)
