from abc import ABC, abstractmethod
from repositories.network_repository import NetworkRepository
from repositories.student_repository import StudentRepository
from core.student_model import StudentModel
from core.exceptions import NoStudentFoundException, NetworkNotTrainedException


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
    def find_student(self, id: int):
        pass

    @abstractmethod
    def predict_current_student_success(self):
        pass


class CommandCenterIMPL(CommandCenter):
    def __init__(self, network_repo: NetworkRepository, students_repo: StudentRepository, ):
        self.current_student = None
        self.network_repo = network_repo
        self.students_repo = students_repo

    def exit(self):
        exit()

    def show_database_status(self):
        try:
            self.network_repo.show_training_status()
        except NetworkNotTrainedException:
            print('Network is not trained. Start training now!')


    def reset_database(self):
        self.network_repo.drop_network_table()
        self.students_repo.dropStudentsTable()

    def create_new_student(self):
        if(self.current_student != None):
            confirm = str(input(
                "There is an existing student, replace? Type Y for yes or N for no")).lower()
            if(confirm != 'y'):
                return

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

        self.current_student = StudentModel(0, name,
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
        print('Current student is: {}'.format(self.current_student.name))

    def show_current_student(self):
        if(type(self.current_student) is StudentModel):
            self.__print_student(self.current_student)
        else:
            print('Currently no student is stored in memory. ')

    def remove_current_student(self):
        if(self.current_student != None):
            confirm = str(input(
                "Remove the current student? Type Y for yes or N for no: ")).lower()
            if(confirm != 'y'):
                return
            self.current_student = None
        else:
            print('Currently no student is stored in memory.')

    def save_current_student(self):
        if(self.current_student != None):
            lastrowid = self.students_repo.saveStudentToDb(
                self.current_student)
            print(
                "The student status is saved with the following id: \n {}".format(lastrowid))
        else:
            print('Currently no student is stored in memory.')

    def find_student(self, id: int):
        try:
            student = self.students_repo.findSingleStudent(id)
            self.__print_student(student)
            to_store = str(input(
                'Store to memory? (existing student will be replaced) Type Y for yes and N for no: ')).lower()
            if(to_store == "y"):
                self.current_student = student
                print('Current student is: {}'.format(
                    self.current_student.name))
        except NoStudentFoundException:
            print("No student with this ID is found.")

    def predict_current_student_success(self):
        pass

    def __print_student(self, student: StudentModel):
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
