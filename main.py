from infrastructure.infrastructure import DatabaseIMPL
from repositories.student_repository import StudentRepositoryIMPL
from core.network import Network
from repositories.random_student_generator import RandomStudentGeneratorIMPL
from repositories.network_repository import NetworkRepository
from presentation.command_center import CommandCenterIMPL
from presentation.command_operator import CommandOperator
import numpy as np


def initialize_database() -> tuple:
    database = DatabaseIMPL('students_db.db')
    network_repo = NetworkRepository(database)
    network_repo.create_network_table()

    students_repo = StudentRepositoryIMPL(database)
    students_repo.createStudentsTable()

    return (network_repo, students_repo)


def initialize_command_line(network_repo, students_repo):
    cc = CommandCenterIMPL(network_repo, students_repo)
    CommandOperator(cc)


def initialize():
    result = initialize_database()
    network_repo = result[0]
    students_repo = result[1]
    initialize_command_line(network_repo, students_repo)


def run_neural_network():
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


def main():
    initialize()
    # rs = RandomStudentGeneratorIMPL()
    # fs = rs.generateRandomStudents(2)

    # for s in fs:
    #     print(s)
    # run_neural_network()


if __name__ == "__main__":
    main()
