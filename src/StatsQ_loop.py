
from Play import Play
from QLearning import QLearning
from BaseParams import BoardPossitionParams


if __name__ == '__main__':
    
    games_to_play = 10000

    base_memory = 'res/memory1-0.bson'
    gamma = 0.99
    learning_rate = 0.8

    epoch_min = 3500000
    epoch_max = 5000000

    eps_min = 0.1
    eps_max = 0.1
    
    while eps_min <= eps_max:

        while epoch_min <= epoch_max:

            bp = BoardPossitionParams()
            q = QLearning(bp, gamma=gamma, learning_rate=learning_rate, epochs=epoch_min, eps=eps_min, name=base_memory)
            q.learning()
            q.save()

            fp = base_memory.split('.')[0] + '_Q_trained_ep' + str(epoch_min) + '_g' + str(int(gamma * 100)) + \
                   '_l' + str(int(learning_rate * 10)) + '_e' + str(int(eps_min * 100)) + '.bson'

            play = Play(fp, False)
            wins, rounds = play.play_stats(games_to_play)
            
            with open(("res/eps_"+str(int(eps_min * 100))), 'a') as outfile:
                outfile.write(str(epoch_min)+"-"+str(wins)+"-"+str(rounds)+"\n")
            
            print('Win perc:', wins,'Average Rounds:', rounds)
            
            epoch_min += 500000
         
        eps_min += 0.05

