from infrastructure import Column, SQLDataType, DataColumn, SQLDataType
import numpy as np


class StudentModel():
    def __init__(self,
                 id: int,
                 name,
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
                 ) -> None:
        self.id = id
        self.name = name
        self.primary_school_grade = primary_school_grade
        self.elementary_school_grade = elementary_school_grade
        self.high_school_grade = high_school_grade
        self.present_economic_status = present_economic_status
        self.present_political_stress = present_political_stress
        self.student_confidence = student_confidence
        self.parents_education = parents_education
        self.number_of_family_members = number_of_family_members
        self.respect_for_teacher = respect_for_teacher
        self.access_to_modern_technology = access_to_modern_technology

    def to_data_columns(self) -> list[DataColumn]:
        return [
            DataColumn('name', self.name, SQLDataType.real),
            DataColumn('primary_school_grade',
                       self.primary_school_grade, SQLDataType.real),
            DataColumn('elementary_school_grade',
                       self.elementary_school_grade, SQLDataType.real),
            DataColumn('high_school_grade',
                       self.high_school_grade, SQLDataType.real),
            DataColumn('present_economic_status',
                       self.present_economic_status, SQLDataType.real),
            DataColumn('present_political_stress',
                       self.present_political_stress, SQLDataType.real),
            DataColumn('student_confidence',
                       self.student_confidence, SQLDataType.real),
            DataColumn('parents_education',
                       self.parents_education, SQLDataType.real),
            DataColumn('number_of_family_members',
                       self.number_of_family_members, SQLDataType.real),
            DataColumn('respect_for_teacher',
                       self.respect_for_teacher, SQLDataType.real),
            DataColumn('access_to_modern_technology',
                       self.access_to_modern_technology, SQLDataType.real),
        ]

    def to_array(self):
        return np.array([
            self.primary_school_grade,
            self.elementary_school_grade,
            self.high_school_grade,
            self.present_economic_status,
            self.present_political_stress,
            self.student_confidence,
            self.parents_education,
            self.number_of_family_members,
            self.respect_for_teacher,
            self.access_to_modern_technology,
        ])
    table_name = 'students'
    def __str__(self) -> str:
        return """
            student id: {}                  student name: {}
                    primary_school_grade: {}
                    elementary_school_grade: {}
                    high_school_grade: {}
                    present_economic_status: {}
                    present_political_stress: {}
                    student_confidence: {}
                    parents_education: {}
                    number_of_family_members: {}
                    respect_for_teacher: {}
                    access_to_modern_technology: {}
    """.format(
        self.id, self.name, 
            self.primary_school_grade,
            self.elementary_school_grade,
            self.high_school_grade,
            self.present_economic_status,
            self.present_political_stress,
            self.student_confidence,
            self.parents_education,
            self.number_of_family_members,
            self.respect_for_teacher,
            self.access_to_modern_technology,
    )
    @staticmethod
    def to_table() -> tuple[str, list[Column]]:

        return (StudentModel.table_name, [
            Column('name', SQLDataType.real),
            Column('primary_school_grade', SQLDataType.real),
            Column('elementary_school_grade', SQLDataType.real),
            Column('high_school_grade', SQLDataType.real),
            Column('present_economic_status', SQLDataType.real),
            Column('present_political_stress', SQLDataType.real),
            Column('student_confidence', SQLDataType.real),
            Column('parents_education', SQLDataType.real),
            Column('number_of_family_members', SQLDataType.real),
            Column('respect_for_teacher', SQLDataType.real),
            Column('access_to_modern_technology', SQLDataType.real),
        ])
