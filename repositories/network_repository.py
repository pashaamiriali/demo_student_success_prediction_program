from infrastructure.infrastructure import Database, Column, SQLDataType
import numpy as np
from core.exceptions import NetworkNotTrainedException


class NetworkRepository:
    def __init__(self, database: Database):
        self.database = database
        self.synaptic_weights = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        self.__primary_school_grade_to_success = 0
        self.__elementary_school_grade_to_success = 0
        self.__high_school_grade_to_success = 0
        self.__present_economic_status_to_success = 0
        self.__present_political_stress_to_success = 0
        self.__student_confidence_to_success = 0
        self.__parents_education_to_success = 0
        self.__number_of_family_members_to_success = 0
        self.__respect_for_teacher_to_success = 0
        self.__access_to_modern_technology_to_success = 0
        self.__total_number_of_training_sessions = 0
    table_name = 'network_weights'

    def load_from_database(self):
        data = self.database.read(NetworkRepository.table_name).fetchall()
        if len(data) == 0:
            raise NetworkNotTrainedException("Program is not trained.")
        else:
            last_instance = data[len(data)-1]
            self.__primary_school_grade_to_success = last_instance[0]
            self.__elementary_school_grade_to_success = last_instance[1]
            self.__high_school_grade_to_success = last_instance[2]
            self.__present_economic_status_to_success = last_instance[3]
            self.__present_political_stress_to_success = last_instance[4]
            self.__student_confidence_to_success = last_instance[5]
            self.__parents_education_to_success = last_instance[6]
            self.__number_of_family_members_to_success = last_instance[7]
            self.__respect_for_teacher_to_success = last_instance[8]
            self.__access_to_modern_technology_to_success = last_instance[9]
            self.__create_array()

    def __create_array(self):
        self.synaptic_weights = np.array([[
            self.__primary_school_grade_to_success,
            self.__elementary_school_grade_to_success,
            self.__high_school_grade_to_success,
            self.__present_economic_status_to_success,
            self.__present_political_stress_to_success,
            self.__student_confidence_to_success,
            self.__parents_education_to_success,
            self.__number_of_family_members_to_success,
            self.__respect_for_teacher_to_success,
            self.__access_to_modern_technology_to_success,

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

    def show_training_status(self) -> int:
        data = self.database.read(NetworkRepository.table_name).fetchall()
        if len(data) < 1:
            raise NetworkNotTrainedException('')
        number_of_training_sessions = 0
        for item in data:
            number_of_training_sessions += item[10]
        return number_of_training_sessions
