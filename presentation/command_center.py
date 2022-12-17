from abc import ABC, abstractmethod

from numpy import array

from repositories.network_repository import NetworkRepository
from repositories.student_repository import StudentRepository
from repositories.random_student_generator import RandomStudentGenerator
from core.student_model import StudentModel
from core.exceptions import NoStudentFoundException, NetworkNotTrainedException
from core.network import Network


class CommandCenter(ABC):

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def show_database_status(self):
        pass

    @abstractmethod
    def reset_database(self):
        pass

    @abstractmethod
    def create_new_student(self):
        pass

    @abstractmethod
    def show_current_student(self):
        pass

    @abstractmethod
    def remove_current_student(self):
        pass

    @abstractmethod
    def save_current_student(self):
        pass

    @abstractmethod
    def find_student(self, key: int):
        pass

    @abstractmethod
    def predict_current_student_success(self):
        pass

    @abstractmethod
    def train(self, students: array, success_rates: array, number_of_epochs: int):
        pass

    @abstractmethod
    def auto_train(self, number_of_students: int, number_of_epochs: int):
        pass

    @abstractmethod
    def save_current_network_status(self, number_of_epochs: int):
        pass


def print_student(student: StudentModel):
    present_text = """
        Student ID: {} Student Name: {}
        Primary school grade: {}
        Elementary school grade: {}
        High school grade: {}
        Present economic status: {}
        Present political stress: {}
        Student confidence: {}
        Parents education: {}
        Number of family members: {}
        Respect for teacher: {}
        Access to modern technology: {}
        """.format(
        student.id,
        student.name,
        student.primary_school_grade,
        student.elementary_school_grade,
        student.high_school_grade,
        student.present_economic_status,
        student.present_political_stress,
        student.student_confidence,
        student.parents_education,
        student.number_of_family_members,
        student.respect_for_teacher,
        student.access_to_modern_technology,
    )
    print(present_text)


def get_student_from_input() -> StudentModel:
    name = str(input('Name: '))
    primary_school_grade = float(str(input('Primary school grade: ')))
    elementary_school_grade = float(
        str(input('Elementary school grade: ')))
    high_school_grade = float(str(input('High school grade: ')))
    present_economic_status = float(
        str(input('Present economic status: ')))
    present_political_stress = float(
        str(input('Present political stress: ')))
    student_confidence = float(str(input('Student confidence: ')))
    parents_education = float(str(input('Parents education: ')))
    number_of_family_members = float(
        str(input('Number of family members: ')))
    respect_for_teacher = float(str(input('Respect for teacher: ')))
    access_to_modern_technology = float(
        str(input('Access to modern technology: ')))
    return StudentModel(0, name,
                        primary_school_grade,
                        elementary_school_grade,
                        high_school_grade,
                        present_economic_status,
                        present_political_stress,
                        student_confidence,
                        parents_education,
                        number_of_family_members,
                        respect_for_teacher,
                        access_to_modern_technology,
                        )


class CommandCenterIMPL(CommandCenter):

    def __init__(self, network_repo: NetworkRepository, students_repo: StudentRepository, network: Network,
                 random_student_generator: RandomStudentGenerator):
        self.current_student = None
        self.network_repo = network_repo
        self.students_repo = students_repo
        self.network = network
        self.random_student_generator = random_student_generator

    def exit(self):
        exit()

    def show_database_status(self):
        try:
            total_epochs = self.network_repo.show_training_status()
            print(f'Total number of epochs (training sessions): {total_epochs}')
        except NetworkNotTrainedException:
            print('Network is not trained. Start training now!')

    def reset_database(self):
        self.network_repo.drop_network_table()
        self.students_repo.drop_students_table()

    def create_new_student(self):
        if self.current_student is not None:
            confirm = str(input(
                "There is an existing student, replace? Type Y for yes or N for no")).lower()
            if confirm != 'y':
                return

        self.current_student = get_student_from_input()
        print('Current student is: {}'.format(self.current_student.name))

    def show_current_student(self):
        if type(self.current_student) is StudentModel:
            print_student(self.current_student)
        else:
            print('Currently no student is stored in memory. ')

    def remove_current_student(self):
        if self.current_student is not None:
            confirm = str(input(
                "Remove the current student? Type Y for yes or N for no: ")).lower()
            if confirm != 'y':
                return
            self.current_student = None
        else:
            print('Currently no student is stored in memory.')

    def save_current_student(self):
        if self.current_student is not None:
            lastrowid = self.students_repo.save_student_to_db(
                self.current_student)
            print(
                "The student status is saved with the following id: \n {}".format(lastrowid))
        else:
            print('Currently no student is stored in memory.')

    def find_student(self, key: int):
        try:
            student = self.students_repo.find_single_student(key)
            print_student(student)
            to_store = str(input(
                'Store to memory? (existing student will be replaced) Type Y for yes and N for no: ')).lower()
            if to_store == "y":
                self.current_student = student
                print('Current student is: {}'.format(
                    self.current_student.name))
        except NoStudentFoundException:
            print("No student with this ID is found.")

    def predict_current_student_success(self):
        if type(self.current_student) is StudentModel:
            chance_of_success = self.network.think(
                self.current_student.to_array())[0]
            if chance_of_success > 0.5:
                print("This student will succeed with {}% chance.".format(
                    (chance_of_success * 100)))
            else:
                print("This student will fail because it has {}% chance in success".format(
                    (chance_of_success * 100)))
        else:
            print(
                'There is no student stored in memory.\n type "create new student" to store one; then run "predict" '
                'to predict the state of the student.')

    def train(self, students: array, success_rates: array, number_of_epochs: int):
        self.network.train(students, success_rates, number_of_epochs)

        self.__show_synaptic_weights()

    def auto_train(self, number_of_students: int, number_of_epochs: int):
        rand_students = self.random_student_generator.generate_successful_students(number_of_students)
        prev_checkpoint = 0.0
        step = 0.1
        for i in range(len(rand_students)):
            self.network.train(array([rand_students[i].to_list()]), array([0.9]), number_of_epochs)
            if i > (len(rand_students) * (prev_checkpoint + step)):
                prev_checkpoint += step
                print(f'{round(prev_checkpoint * 100)}% done.')

        self.__show_synaptic_weights()
        self.save_current_network_status(number_of_students * number_of_epochs)

    def save_current_network_status(self, number_of_epochs: int):
        self.network_repo.save_synaptic_weights(self.network.synaptic_weights, number_of_epochs)

    def __show_synaptic_weights(self):
        relations = self.network.get_synaptic_weights()
        print("""
        This is what the network thinks about the relationship between each input and the students' outcome:
        The effect of Primary school grade in success: {}
        The effect of Elementary school grade in success: {}
        The effect of High school grade in success: {}
        The effect of Present economic status in success: {}
        The effect of Present political stress in success: {}
        The effect of Student confidence in success: {}
        The effect of Parents education in success: {}
        The effect of Number of family members in success: {}
        The effect of Respect for teacher in success: {}
        The effect of Access to modern technology in success: {}
        """.format(
            relations[0][0],
            relations[1][0],
            relations[2][0],
            relations[3][0],
            relations[4][0],
            relations[5][0],
            relations[6][0],
            relations[7][0],
            relations[8][0],
            relations[9][0],
        ))
