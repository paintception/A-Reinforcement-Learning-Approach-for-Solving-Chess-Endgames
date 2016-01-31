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
         [0.3, 1000000 ,0.0882],
         [0.3, 1500000 ,0.1127],
         [0.3, 2000000 ,0.1887],
         [0.3, 2500000 ,0.2692],
         [0.3, 3000000 ,0.3656],
         [0.3, 3500000 ,0.4885],
         [0.3, 4000000 ,0.5655],
         [0.3, 4500000 ,0.6592],
         [0.3, 5000000 ,0.7458],
         [0.3, 5500000 ,0.8271],
         [0.3, 6000000 ,0.8736],
         [0.3, 6500000 ,0.9057],
         [0.3, 7000000 ,0.9258],
         [0.3, 7500000 ,0.9273],


    ]


    data4 = [
         [0.4, 1000000 ,0.1039],
         [0.4, 1500000 ,0.1823],
         [0.4, 2000000 ,0.2962],
         [0.4, 2500000 ,0.4316],
         [0.4, 3000000 ,0.5895],
         [0.4, 3500000 ,0.6913],
         [0.4, 4000000 ,0.7963],
         [0.4, 4500000 ,0.8714],
         [0.4, 5000000 ,0.9119],
         [0.4, 5500000 ,0.9264],
         [0.4, 6000000 ,0.9342],
         [0.4, 6500000 ,0.9359],
         [0.4, 7000000 ,0.9389],
         [0.4, 7500000 ,0.9356],

    ]


    data5 = [
         [0.5, 1000000 ,0.1481],
         [0.5, 1500000 ,0.2605],
         [0.5, 2000000 ,0.4538],
         [0.5, 2500000 ,0.6731],
         [0.5, 3000000 ,0.792],
         [0.5, 3500000 ,0.8806],
         [0.5, 4000000 ,0.9227],
         [0.5, 4500000 ,0.9326],
         [0.5, 5000000 ,0.9393],
         [0.5, 5500000 ,0.9341],
         [0.5, 6000000 ,0.9332],
         [0.5, 6500000 ,0.9379],

    ]
    data6 = [
         [0.6, 1000000 ,0.2016],
         [0.6, 1500000 ,0.4637],
         [0.6, 2000000 ,0.6858],
         [0.6, 2500000 ,0.8068],
         [0.6, 3000000 ,0.9078],
         [0.6, 3500000 ,0.9328],
         [0.6, 4000000 ,0.9332],
         [0.6, 4500000 ,0.9373],
         [0.6, 5000000 ,0.9337],
         [0.6, 5500000 ,0.9328],
         [0.6, 6000000 ,0.9338],
    ]


    data8 = [
         [0.8, 1000000 ,0.5067],
         [0.8, 1500000 ,0.8053],
         [0.8, 2000000 ,0.9169],
         [0.8, 2500000 ,0.9358],
         [0.8, 3000000 ,0.9369],
         [0.8, 3500000 ,0.9316],
         [0.8, 4000000 ,0.9328],
         [0.8, 4500000 ,0.9308],
         [0.8, 5000000 ,0.9319],
         [0.8, 5500000 ,0.9358],
         [0.8, 6000000 ,0.9367],

    ]


    data9 = [
         [0.9, 1000000 ,0.7112],
         [0.9, 1500000 ,0.8748],
         [0.9, 2000000 ,0.9313],
         [0.9, 2500000 ,0.9353],
         [0.9, 3000000 ,0.9308],
         [0.9, 3500000 ,0.9334],
         [0.9, 4000000 ,0.9359],
         [0.9, 4500000 ,0.9358],
         [0.9, 5000000 ,0.938],
         [0.9, 5500000 ,0.9362],
         [0.9, 6000000 ,0.9331],

    ]
    data1 = np.array(data1)
    data2 = np.array(data2)
    data3 = np.array(data3)
    data4 = np.array(data4)
    data5 = np.array(data5)
    data6 = np.array(data6)
    data8 = np.array(data8)
    data9 = np.array(data9)

    x1 = data1[:, 1]
    x2 = data2[:, 1]
    x3 = data3[:, 1]
    x4 = data4[:, 1]
    x5 = data5[:, 1]
    x6 = data6[:, 1]
    x8 = data8[:, 1]
    x9 = data9[:, 1]

    y1 = data1[:, 2]
    y2 = data2[:, 2]
    y3 = data3[:, 2]
    y4 = data4[:, 2]
    y5 = data5[:, 2]
    y6 = data6[:, 2]
    y8 = data8[:, 2]
    y9 = data9[:, 2]



    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5,  10.5)
    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x1, y1, 'r-',  linewidth=2,label='$\gamma=0.1$')
    plt.plot(x2, y2, 'b-',  linewidth=2,label='$\gamma=0.2$')
    plt.plot(x3, y3, 'g-',  linewidth=2,label='$\gamma=0.3$')
    plt.plot(x4, y4, 'y-',  linewidth=2,label='$\gamma=0.4$')
    plt.plot(x5, y5, 'g-',  linewidth=2,label='$\gamma=0.5$')
    plt.plot(x6, y6, 'y-',  linewidth=2,label='$\gamma=0.6$')
    plt.plot(x8, y8, 'm-',  linewidth=2,label='$\gamma=0.8$')
    plt.plot(x9, y9, 'c-',  linewidth=2,label='$\gamma=0.9$')

    legend = plt.legend(loc='lower right',  shadow=True,  fontsize='large')
    plt.locator_params(nbins=10)

    plt.savefig('plots/win_percentage_g01_g02_g03_g04_g05_g06_g08_g09.png')


    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.1$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x1,  y1,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g01.png')

    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.2$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x2,  y2,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g02.png')


    plt.clf()
    ## Change this
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.3$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x3,  y3,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g03.png')

    plt.clf()
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.4$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x4, y4, 'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g04.png')

    plt.clf()
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.5$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x5,  y5,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g05.png')

    plt.clf()
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.6$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x6,  y6,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g06.png')

    plt.clf()
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.8$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x8,  y8,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g08.png')

    plt.clf()
    plt.title(r'Win Percentage over 10000 games with \textbf{$ \gamma = 0.9$}')
    plt.xlabel('Training Epochs')
    plt.ylabel('Win Percentage')
    plt.plot(x9,  y9,  'r-',  linewidth=2)
    plt.savefig('plots/win_percentage_g09.png')

