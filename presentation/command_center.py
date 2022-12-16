from abc import ABC, abstractmethod


class CommandCenter(ABC):

    @abstractmethod
    def exit(self):
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
    def predict_current_student_success(self):
        pass


class CommandCenterIMPL(CommandCenter):
    def __init__(self,):
        self.current_student = None

    def exit(self):
        exit()

    def reset_database(self):
        pass

    def create_new_student(self):
        pass

    def show_current_student(self):
        pass

    def remove_current_student(self):
        pass

    def edit_current_student(self):
        pass

    def predict_current_student_success(self):
        pass

