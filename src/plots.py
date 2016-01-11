import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rc('text',  usetex=True)
    data1 = [
     [0.1, 1000000, 0.0639, 6.81377151799687],
     [0.1, 1500000, 0.0636, 5.251572327044025],
     [0.1, 2000000, 0.0898, 9.21380846325167],
     [0.1, 2500000, 0.1192, 8.87248322147651],
     [0.1, 3000000, 0.1447, 7.246026261230131],
     [0.1, 3500000, 0.191, 8.206806282722512],
     [0.1, 4000000, 0.191, 7.850261780104712],
     [0.1, 4500000, 0.2495, 8.333466933867735],
     [0.1, 5000000, 0.2671, 8.171471359041558],
    ]

    data2 = [
     [0.2, 1000000, 0.0692, 6.01878612716763],
     [0.2, 1500000, 0.0764, 5.891361256544503],
     [0.2, 2000000, 0.1355, 8.385239852398524],
     [0.2, 2500000, 0.176, 8.510227272727272],
     [0.2, 3000000, 0.2003, 7.789815277084373],
     [0.2, 3500000, 0.2777, 8.645660785019805],
     [0.2, 4000000, 0.3497, 8.810694881326851],
     [0.2, 4500000, 0.4081, 8.888997794658172],
     [0.2, 5000000, 0.5008, 9.678314696485623],
        ]

    data3 = [
     [0.3, 1000000, 0.088, 6.81377151799687],
     [0.3, 1500000, 0.11, 5.251572327044025],
     [0.3, 2000000, 0.18, 9.21380846325167],
     [0.3, 2500000, 0.26, 8.87248322147651],
     [0.3, 3000000, 0.36, 7.246026261230131],
     [0.3, 3500000, 0.48, 8.206806282722512],
     [0.3, 4000000, 0.56, 7.850261780104712],
     [0.3, 4500000, 0.65, 8.333466933867735],
     [0.3, 5000000, 0.74, 8.333466933867735],

    ]


    data4 = [
     [0.4, 1000000, 0.10, 6.01878612716763],
     [0.4, 1500000, 0.18, 5.891361256544503],
     [0.4, 2000000, 0.29, 8.385239852398524],
     [0.4, 2500000, 0.43, 8.510227272727272],
     [0.4, 3000000, 0.58, 7.789815277084373],
     [0.4, 3500000, 0.69, 8.645660785019805],
     [0.4, 4000000, 0.79, 8.810694881326851],
     [0.4, 4500000, 0.87, 8.888997794658172],
     [0.4, 5000000, 0.91, 8.888997794658172],
    ]


    data8 = [
     [0.8, 1000000, 0.5067, 6.81377151799687],
     [0.8, 1500000, 0.8053, 5.251572327044025],
     [0.8, 2000000, 0.9169, 9.21380846325167],
     [0.8, 2500000, 0.9358, 8.87248322147651],
     [0.8, 3000000, 0.9369, 8.87248322147651],
    ]


    data9 = [
     [0.9, 1000000, 0.7112, 6.01878612716763],
     [0.9, 1500000, 0.8748, 5.891361256544503],
     [0.9, 2000000, 0.9313, 8.385239852398524],
     [0.9, 2500000, 0.9353, 8.510227272727272],
    ]
    data1 = np.array(data1)
    data2 = np.array(data2)
    data3 = np.array(data3)
    data4 = np.array(data4)
    data8 = np.array(data8)
    data9 = np.array(data9)

    x = data1[:,  1]
    x8 = data8[:, 1]
    x9 = data9[:, 1]

    y1 = data1[:,  2]
    y2 = data2[:,  2]
    y3 = data3[:,  2]
    y4 = data4[:,  2]
    y8 = data8[:,  2]
    y9 = data9[:,  2]


    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5,  10.5)
    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x, y1, 'r-',  linewidth=2,label='$\gamma=0.1$')
    plt.plot(x, y2, 'b-',  linewidth=2,label='$\gamma=0.2$')
    plt.plot(x, y3, 'g-',  linewidth=2,label='$\gamma=0.3$')
    plt.plot(x, y4, 'y-',  linewidth=2,label='$\gamma=0.4$')
    plt.plot(x8, y8, 'm-',  linewidth=2,label='$\gamma=0.8$')
    plt.plot(x9, y9, 'c-',  linewidth=2,label='$\gamma=0.9$')

    legend = plt.legend(loc='lower right',  shadow=True,  fontsize='large')
    plt.locator_params(nbins=10)

    plt.savefig('plots/win_percentage_g01_g02_g03_g04_g08_g09.png')


    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.1$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x,  y1,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g01.png')

    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.2$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x,  y2,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g02.png')


    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.3$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x,  y3,  'r-',  linewidth=2)

    ## Change this
    plt.savefig('plots/win_percentage_g03.png')

    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.4$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x, y4, 'r-',  linewidth=2)

    #legend = plt.legend(loc='lower right',  shadow=True,  fontsize='large')
    #plt.locator_params(nbins=10)

    plt.savefig('plots/win_percentage_g04.png')

    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.8$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x8,  y8,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g08.png')

    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.9$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x9,  y9,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g09.png')
