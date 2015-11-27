__author__ = 'yaron'

from Cheesboard import ChessBoard
import csv

# 0. White King column
# 1. White King row
# 2. White Rook column
# 3. White Rook row
# 4. Black King column
# 5. Black King row
# => rank


class DatabaseLearning:

    rank_to_points = {
        'draw': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16
    }

    pos_to_num = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    def __init__(self, parameter_set):
        self.dataset = self._get_dataset()
        self.parameter_set = parameter_set
        self.knowledge = {}

    def learn(self, iterations):
        for i in range(0, iterations):
            board = ChessBoard.get_random_chessboard()
            self.parameter_set.calculate_parameters(board)
            rank = self.parameter_set.learning_move()
            if self.parameter_set.rank_higher(self.knowledge, rank):
                self.knowledge = self.parameter_set.update_knowledge(self.knowledge)

    def _get_dataset(self):
        dataset = {}
        with open('dataset/krkopt.data') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                dataset[(self.pos_to_num[row[0]], int(row[1])-1, self.pos_to_num[row[2]], int(row[3])-1, self.pos_to_num[row[4]], int(row[5])-1)] \
                    = self.rank_to_points[row[6]]

        return dataset


class BaseParametersSet:

    knowledge_file = ''

    def __init__(self):
        self.parameter_set = ()
        self.new_parameter_set = ()

    def calculate_parameters(self, board):
        pass

    def learning_move(self):
        return 0

    def rank_higher(self, knowledge, rank):
        pass

    def update_knowledge(self, knowledge):
        pass

    def load_knowledge_file(self):
        pass

    def save_knowledge_file(self, knowledge):
        pass


class ParameterSet1(BaseParametersSet):

# (BK_to_WK_row, BK_to_WK_col, BK_to_WR_row, BK_to_WR_col, WK_to_WR_row, WK_to_WR_col)

    knowledge_file = 'knowledge/parameter_set_1.csv'

    def save_knowledge_file(self, knowledge):
        with open(self.knowledge_file) as file:
            writer = csv.writer(file, delimeter=",")
            for ps, nps in knowledge:
                writer.writerow([ps, nps])





if __name__ == '__main__':
    dl = DatabaseLearning()





