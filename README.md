# A Reinforcement Learning Approach for Solving Chess Endgames

In this project we show how a Reinforcement Learning approach can be successfully applied in chess. This is done by focusing on KRK endgames and by implementing the Q-Learning algorithm with different exploration policies. The main goal of this research was to train an artificial agent able to win the endgames as a White Player against an "experienced" Black Player.

In order to train an agent be sure to follow the following steps:

* Installed python3 and all required packages, in particular "cocos" if you want the fancy GUI
* Create a /res dir in src dir.
* Launch BaseParams.py in order to build the empty Q-Matrix
* To train the Agent using the Q-Learning algorithm set necessary parameters at the end of QLearning.py, and of course launch it.
* To see statistcs relative to how many wins and the average number of moves regarding the White Player launch StatsQ.py with relative parameters
* If you want to see a command line GUI change Play(fp,TRUE)
* If you want to see the fancy GUI launch GUI from res /GUI being sure to use the correct memory file in the __main__
 
* Have fun from Matthia Yaroslav Zacharias and Evangelos
