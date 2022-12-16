from infrastructure import DatabaseIMPL
from repositories import StudentRepositoryIMPL
from network import Network
from random_student_generator import RandomStudentGeneratorIMPL
from command_center import CommandOperator, CommandCenterIMPL
import numpy as np


def initialize_database():
    database = DatabaseIMPL('students_db.db')
    repo = StudentRepositoryIMPL(database)
    repo.createStudentsTable()


def initialize_command_line():
    cc = CommandCenterIMPL()
    CommandOperator(cc)


def initialize():
    initialize_database()
    initialize_command_line()


def run_neural_network():
    # TODO: create a new network scheme
    neural_network = Network()
    print('Random synaptic weights:')
    print(neural_network.synaptic_weights)

    training_input = np.array([[0.1, 0.2, 0.9, 0.1, 0.2, 0.9, 0.1, 0.2, 0.9, 0.1, ],
                               [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9,
                                   0.9, 0.9, 0.9, ],
                               [0.9, 0.3, 0.9, 0.9, 0.3, 0.9, 0.9,
                                   0.3, 0.9, 0.9, ],
                               [0.2, 0.9, 0.9, 0.2, 0.9, 0.9, 0.2, 0.9, 0.9, 0.2, ], ])

    training_outputs = np.array([[0, 1, 1, 0]]).T

    print('Training started...')
    neural_network.train(training_input, training_outputs, 10000)
    print('Training done.')

    print('Synaptic weights after training: ')
    print(neural_network.synaptic_weights)

    i1 = str(input("Input 1: "))
    i2 = str(input("Input 2: "))
    i3 = str(input("Input 3: "))
    i4 = str(input("Input 4: "))
    i5 = str(input("Input 5: "))
    i6 = str(input("Input 6: "))
    i7 = str(input("Input 7: "))
    i8 = str(input("Input 8: "))
    i9 = str(input("Input 9: "))
    i10 = str(input("Input 10: "))

    print('New input data: ', i1, i2, i3, i4,
          i5, i6, i7, i8, i9, i10,)
    print('Output data: ')
    print(neural_network.think(
        np.array([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, ])))


if __name__ == "__main__":
    initialize()
    rs = RandomStudentGeneratorIMPL()
    fs = rs.generateRandomStudents(2)

    # for s in fs:
    #     print(s)
    # run_neural_network()
