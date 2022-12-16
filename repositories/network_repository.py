from infrastructure.infrastructure import Database, Column, SQLDataType
import numpy as np
from core.exceptions import NetworkNotTrainedException


class NetworkRepository():
    def __init__(self, database: Database):
        self.database = database
        self.synaptic_weights = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        self.primary_school_grade_to_success = 0
        self.elementary_school_grade_to_success = 0
        self.high_school_grade_to_success = 0
        self.present_economic_status_to_success = 0
        self.present_political_stress_to_success = 0
        self.student_confidence_to_success = 0
        self.parents_education_to_success = 0
        self.number_of_family_members_to_success = 0
        self.respect_for_teacher_to_success = 0
        self.access_to_modern_technology_to_success = 0
    table_name = 'network_weights'

    def load_from_database(self):
        data = self.database.read(NetworkRepository.table_name).fetchall()
        if len(data) == 0:
            raise NetworkNotTrainedException("Program is not trained.")
        else:
            last_instance = data[len(data)-1]
            self.primary_school_grade_to_success = last_instance[0]
            self.elementary_school_grade_to_success = last_instance[1]
            self.high_school_grade_to_success = last_instance[2]
            self.present_economic_status_to_success = last_instance[3]
            self.present_political_stress_to_success = last_instance[4]
            self.student_confidence_to_success = last_instance[5]
            self.parents_education_to_success = last_instance[6]
            self.number_of_family_members_to_success = last_instance[7]
            self.respect_for_teacher_to_success = last_instance[8]
            self.access_to_modern_technology_to_success = last_instance[9]
            self.__create_array()

    def __create_array(self):
        self.synaptic_weights = np.array([[
            self.primary_school_grade_to_success,
            self.elementary_school_grade_to_success,
            self.high_school_grade_to_success,
            self.present_economic_status_to_success,
            self.present_political_stress_to_success,
            self.student_confidence_to_success,
            self.parents_education_to_success,
            self.number_of_family_members_to_success,
            self.respect_for_teacher_to_success,
            self.access_to_modern_technology_to_success,

        ]])

    def create_network_table(self):
        self.database.create_table(NetworkRepository.table_name, [
            Column('primary_school_grade_to_success', SQLDataType.real),
            Column('elementary_school_grade_to_success', SQLDataType.real),
            Column('high_school_grade_to_success', SQLDataType.real),
            Column('present_economic_status_to_success', SQLDataType.real),
            Column('present_political_stress_to_success', SQLDataType.real),
            Column('student_confidence_to_success', SQLDataType.real),
            Column('parents_education_to_success', SQLDataType.real),
            Column('number_of_family_members_to_success', SQLDataType.real),
            Column('respect_for_teacher_to_success', SQLDataType.real),
            Column('access_to_modern_technology_to_success', SQLDataType.real),
        ])

    def drop_network_table(self):
        self.database.drop_table(NetworkRepository.table_name)
