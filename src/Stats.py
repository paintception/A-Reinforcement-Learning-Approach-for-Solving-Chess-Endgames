
from Play import Play


if __name__ == '__main__':

    epoch = 5000000
    gamma = 9.0
    #epochs = [ x for x in range(100,1000,100)]

    games_to_play = 100

    base_memory = 'res/memory1-0.bson'
    fp = base_memory.split('.')[0] + '_trained_' + str(epoch) + '_9.bson'

    play = Play(fp, False)
    wins, rounds = play.play_stats(games_to_play)

    print('Win perc:', wins,'Average Rounds:', rounds)
