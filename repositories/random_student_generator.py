from abc import ABC, abstractmethod
from core.student_model import StudentModel
import random


# ! Important values in hypothetical premise (for success)
# High primary schools grade (0.8-1.0)
# Low parents education (0.0-0.4)
# High access to modern technology (0.8-1.0)
# High confidence (0.8-1.0)
# ! reverse for failure


class RandomStudentGenerator(ABC):
    @abstractmethod
    def generate_successful_students(self, count: int) -> list[StudentModel]:
        pass

    @abstractmethod
    def generate_failure_students(self, count: int) -> list[StudentModel]:
        pass

    @abstractmethod
    def generate_random_students(self, count: int) -> list[StudentModel]:
        pass


class RandomStudentGeneratorIMPL(RandomStudentGenerator):
    def __init__(self) -> None:
        super().__init__()

    def generate_successful_students(self, count: int) -> list[StudentModel]:
        students = []
        for _ in range(count):
            student = StudentModel(0,  # id
                                   str(random.uniform(0.0, 1.0)),  # name
                                   # primary_school_grade
                                   1.0,
                                   # elementary_school_grade
                                   random.uniform(0.0, 0.9),
                                   # high_school_grade
                                   random.uniform(0.0, 0.9),
                                   # present_economic_status
                                   1.0,
                                   # present_political_stress
                                   0.0,
                                   # student_confidence
                                   1.0,
                                   # parents_education
                                   0.0,
                                   # number_of_family_members
                                   random.uniform(0.0, 0.9),
                                   # respect_for_teacher
                                   1.0,
                                   # access_to_modern_technology
                                   1.0,
                                   )
            students.append(student)
        return students

    def generate_failure_students(self, count: int) -> list[StudentModel]:
        students = []
        for _ in range(count):
            student = StudentModel(0,  # id
                                   str(random.uniform(0.0, 1.0)),  # name
                                   # primary_school_grade
                                   random.uniform(0.0, 0.4),
                                   # elementary_school_grade
                                   random.uniform(0.0, 1.0),
                                   # high_school_grade
                                   random.uniform(0.0, 1.0),
                                   # present_economic_status
                                   random.uniform(0.0, 1.0),
                                   # present_political_stress
                                   random.uniform(0.0, 1.0),
                                   # student_confidence
                                   random.uniform(0.0, 0.4),
                                   # parents_education
                                   random.uniform(0.8, 1.0),
                                   # number_of_family_members
                                   random.uniform(0.0, 1.0),
                                   # respect_for_teacher
                                   random.uniform(0.0, 1.0),
                                   # access_to_modern_technology
                                   random.uniform(0.0, 0.4),
                                   )
            students.append(student)
        return students

    def generate_random_students(self, count: int) -> list[StudentModel]:
        students = []
        for _ in range(count):
            student = StudentModel(0,  # id
                                   str(random.uniform(0.0, 1.0)),  # name
                                   # primary_school_grade
                                   random.uniform(0.0, 1.0),
                                   # elementary_school_grade
                                   random.uniform(0.0, 1.0),
                                   # high_school_grade
                                   random.uniform(0.0, 1.0),
                                   # present_economic_status
                                   random.uniform(0.0, 1.0),
                                   # present_political_stress
                                   random.uniform(0.0, 1.0),
                                   # student_confidence
                                   random.uniform(0.0, 1.0),
                                   # parents_education
                                   random.uniform(0.0, 1.0),
                                   # number_of_family_members
                                   random.uniform(0.0, 1.0),
                                   # respect_for_teacher
                                   random.uniform(0.0, 1.0),
                                   # access_to_modern_technology
                                   random.uniform(0.0, 1.0),
                                   )
            students.append(student)
        return students
