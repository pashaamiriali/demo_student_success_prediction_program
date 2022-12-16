from abc import ABC, abstractclassmethod
from core.student_model import StudentModel
from infrastructure.infrastructure import Database


class StudentRepository(ABC):
    
    @abstractclassmethod
    def saveStudentToDb(self, student: StudentModel):
        pass

    @abstractclassmethod
    def findAllStudents(self) -> list[StudentModel]:  # type: ignore
        pass

    @abstractclassmethod
    def findSingleStudent(self, key: int) -> StudentModel:  # type: ignore
        pass

    @abstractclassmethod
    def deleteStudent(self, key: int):
        pass

    @abstractclassmethod
    def createStudentsTable(self):
        pass

    @abstractclassmethod
    def dropStudentsTable(self):
        pass


class StudentRepositoryIMPL(StudentRepository):
    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database

    def saveStudentToDb(self, student: StudentModel):
        number_of_rows_found = len(self.database.find(
            StudentModel.table_name, student.id).fetchall())
        if(number_of_rows_found > 0):
            self.database.update(StudentModel.table_name,
                                 student.to_data_columns, student.id)
        else:
            self.database.insert(StudentModel.table_name,
                                 student.to_data_columns,)

    def findAllStudents(self) -> list[StudentModel]:
        data = self.database.read(StudentModel.table_name).fetchall()
        return_items = []
        for item in data:
            return_items.append(StudentModel(
                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
                item[5],
                item[6],
                item[7],
                item[8],
                item[9],
                item[10],
                item[11],
            ))
        return return_items

    def findSingleStudent(self, key: int) -> StudentModel:
        data = self.database.read(StudentModel.table_name).fetchall()
        item = data[0]
        return StudentModel(
            item[0],
            item[1],
            item[2],
            item[3],
            item[4],
            item[5],
            item[6],
            item[7],
            item[8],
            item[9],
            item[10],
            item[11],
        )

    def deleteStudent(self, key: int):
        self.database.delete(StudentModel.table_name, key)

    def createStudentsTable(self):
        student_skeleton = StudentModel.to_table()
        self.database.create_table(student_skeleton[0], student_skeleton[1])

    def dropStudentsTable(self):
        self.database.drop_table(StudentModel.table_name)
