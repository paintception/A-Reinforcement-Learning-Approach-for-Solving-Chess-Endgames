import os.path
from BaseParams import BoardPossitionParams
from QLearning import QLearning
from Play import Play
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

if __name__ == '__main__':


    epochs = [1000000] 
    #epochs = [ x for x in range(100,1000,100)]

    games_to_play = 10000

    base_memory = 'res/memory1-0.bson'

    stats_array = [
        [ ],
        [ ],
    ]


    for epoch in epochs:

        # CHANGE THIS WITH GAMMA FOR YARUSLAV IS 0.3 0.5,
        i= 0
        for gamma,i in enumerate(range(1,3,1)):
            fp = base_memory.split('.')[0] + '_trained_' + str(epoch) + '_' + str(int(gamma/10)) + '.bson'

            #Check if is trained
            if not os.path.isfile(fp):
                print ('[Info] The agent is training for',epoch,'epochs')
                bp = BoardPossitionParams()
                q = QLearning(bp, gamma,0.8, epoch, base_memory)
                q.learning()
                q.save()
                #exit(0)
            # Play
            print ('Memory exists..\nPlaying...')
            play = Play(fp, False)
            wins, rounds = play.play_stats(games_to_play)

            print('Win perc:', wins,'Average Rounds:', rounds)
            stats_array[i].append((wins, rounds))
            i+=1

    plt.rc('text', usetex=True)
    data = np.array(stats_array)

    x = np.array(epochs[0:5])
    y0 = data[0][:, 0]
    y1 = data[1][:, 0]

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.1$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x,y0,'r-', linewidth=2)

    #legend = plt.legend(loc='lower right', shadow=True, fontsize='large')
    #plt.locator_params(nbins=10)

    plt.savefig('plots/win_percentage_g01.png')
    f = open('plots/win_percentage_g01.txt','w')
    for i, y in enumerate(y0):
        s = str(x[i])+' '+ str(y) + '\n'
        f.write(s) # python will convert \n to os.linesep
    f.close()


    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.2$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x, y1, 'r-', linewidth=2)

    ## Change this
    plt.savefig('plots/win_percentage_g02.png')

    f = open('plots/win_percentage_g02.txt', 'w')
    for i, y in enumerate(y0):
        s = str(x[i])+' ' + str(y) + '\n'
        f.write(s)# python will convert \n to os.linesep
    f.close()
