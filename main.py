import numpy as np

from core.network import Network
from core.exceptions import NetworkNotTrainedException
from infrastructure.infrastructure import DatabaseIMPL
from presentation.command_center import CommandCenterIMPL
from presentation.command_operator import CommandOperator
from repositories.network_repository import NetworkRepository
from repositories.random_student_generator import RandomStudentGeneratorIMPL
from repositories.student_repository import StudentRepositoryIMPL, StudentRepository


def initialize_database() -> tuple:
    database = DatabaseIMPL('students_db.db')
    network_repo = NetworkRepository(database)
    network_repo.create_network_table()

    students_repo = StudentRepositoryIMPL(database)
    students_repo.create_students_table()

    return network_repo, students_repo


def initialize_command_line(network_repo: NetworkRepository, students_repo: StudentRepository):
    synaptic_weights = None
    try:
        network_repo.load_from_database()
        synaptic_weights = network_repo.get_synaptic_weights()
    except NetworkNotTrainedException:
        synaptic_weights = None
    network = Network(synaptic_weights)
    rand_student_gen = RandomStudentGeneratorIMPL()
    cc = CommandCenterIMPL(network_repo, students_repo, network, rand_student_gen)
    CommandOperator(cc)


def initialize():
    result = initialize_database()
    network_repo = result[0]
    students_repo = result[1]
    initialize_command_line(network_repo, students_repo)


def main():
    initialize()


if __name__ == "__main__":
    main()
