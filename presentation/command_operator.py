from numpy import array

from presentation.command_center import CommandCenter, get_student_from_input
from presentation.help import Help


class CommandOperator:
    def __init__(self, command_center: CommandCenter):
        self.command_center = command_center
        Help.show_welcome()
        self.show_database_status()
        self.listen_for_command()

    def listen_for_command(self):
        command = str(input('NC> ')).lower().strip()
        if command == 'exit' or command == 'q':
            self.command_center.exit()
            return
        elif command == 'help' or command == 'h':
            self.show_help()
        elif command == 'reset database':
            self.__reset_database()
        elif command == 'reset network':
            self.__reset_network()
        elif command == 'create new student':
            self.__create_new_student()

        elif command == 'show current student':
            self.__show_current_student()

        elif command == 'remove current student':
            self.__remove_current_student()

        elif command == 'save current student':
            self.__save_current_student()
        elif command == 'find student':
            self.__find_student()

        elif command == 'predict':
            self.__predict()
        elif command == 'train':
            self.__train()
        elif command == 'auto train':
            self.__auto_train()
        elif command == 'show relationships':
            self.__show_relationships()
        else:
            print("No such command found.")
            print('Type "help" or "h" to see instructions for using the program.')

        self.listen_for_command()

    @staticmethod
    def show_help():
        Help().show_help()

    def __reset_database(self):
        reassurance = str(input(
            'all training data and students information will be lost. to Continue type "Yes": ')).lower()
        if reassurance == 'yes':
            self.command_center.reset_database()
            print('Database reset done.')
            exit()

    def __reset_network(self):
        reassurance = str(input(
            'all training data will be lost. to Continue type "Yes": ')).lower()
        if reassurance == 'yes':
            self.command_center.reset_network()
            print('Network reset done.')
            exit()

    def show_database_status(self):
        self.command_center.show_database_status()

    def __create_new_student(self):
        self.command_center.create_new_student()

    def __show_current_student(self):
        self.command_center.show_current_student()

    def __remove_current_student(self):
        self.command_center.remove_current_student()

    def __save_current_student(self):
        self.command_center.save_current_student()

    def __find_student(self):
        self.command_center.find_student(int(input('Enter student ID: ')))

    def __predict(self):
        self.command_center.predict_current_student_success()

    def __train(self):
        number_of_students = int(input('Enter the number of students to train: '))
        students = []
        success_rates = []
        for _ in range(number_of_students):
            students.append(get_student_from_input().to_list())
            success_rates.append(int(input('Enter the success status between 0 and 1: ')))
        number_of_epochs = int(input('Enter the number of epochs (training sessions): '))
        students = array(students)
        success_rates = array(success_rates)
        self.command_center.train(students, success_rates, number_of_epochs)
        self.__save_network_results(number_of_epochs)

    def __auto_train(self):
        number_of_students = int(input('Number of students to generate: '))
        number_of_epochs = int(input('Number of epochs (training sessions): '))
        self.command_center.auto_train(number_of_students, number_of_epochs)
        self.__save_network_results(number_of_epochs * number_of_students)

    def __save_network_results(self, number_of_epochs):
        save_results = str(
            input(
                'Training done. Do you want to save the current network status? Type Y for yes and N for no: ')) \
            .lower().strip()
        if save_results == 'y':
            self.command_center.save_current_network_status(number_of_epochs)
            print('New network status saved!')

    def __show_relationships(self):
        self.command_center.show_relationships()
