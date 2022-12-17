
from presentation.command_center import CommandCenter
from presentation.help import Help


class CommandOperator():
    def __init__(self, command_center: CommandCenter):
        self.command_center = command_center
        Help.show_welcome()
        self.listen_for_command()

    def listen_for_command(self):
        command = str(input('NC> ')).lower()
        if(command == 'exit' or command == 'q'):
            self.command_center.exit()
            return
        elif(command == 'help' or command == 'h'):
            self.show_help()
        elif(command == 'reset database'):
            self.__reset_database()
        elif (command == 'create new student'):
            self.__create_new_student()

        elif (command == 'show current student'):
            self.__show_current_student()

        elif (command == 'remove current student'):
            self.__remove_current_student()

        elif (command == 'save current student'):
            self.__save_current_student()
        elif (command == 'find student'):
            self.__find_student()

        else:
            print("No such command found.")
            print('Type "help" or "h" to see instructions for using the program.')

        self.listen_for_command()

    def show_help(self):
        Help().show_help()

    def __reset_database(self):
        reassurance = str(input(
            'all training data and students information will be lost. to Continue type "Yes": ')).lower()
        if (reassurance == 'yes'):
            self.command_center.reset_database()
            print('Database reset done.')
            exit()

    def __create_new_student(self):
        self.command_center.create_new_student()

    def __show_current_student(self):
        self.command_center.show_current_student()

    def __remove_current_student(self):
        self.command_center.remove_current_student()

    def __save_current_student(self):
        self.command_center.save_current_student()

    def __find_student(self):
        self.command_center.find_student(int(str(input('Enter student ID: '))))
