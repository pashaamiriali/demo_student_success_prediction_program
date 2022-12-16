from abc import ABC, abstractclassmethod
import sqlite3 as sql
from sqlite3 import Cursor
import enum


class SQLDataType(enum.Enum):
    text = "TEXT NOT NULL "
    int = "INT NOT NULL "
    real = "REAL NOT NULL "
    n_text = "TEXT "
    n_int = "INT"
    n_real = "REAL"


class Column():
    def __init__(self, name: str, type: SQLDataType):
        self.name = name
        self.type = type


class DataColumn():
    def __init__(self, name: str, data, type: SQLDataType):
        self.name = name
        self.data = data
        self.type = type


class SQLTableData():
    def __init__(self, data: list[DataColumn]) -> None:
        self.data = data


class Database(ABC):
    @abstractclassmethod
    def create_table(self, name: str, columns: list):
        pass

    @abstractclassmethod
    def drop_table(self, name: str):
        pass

    @abstractclassmethod
    def insert(self, table_name: str, data):
        pass

    @abstractclassmethod
    def read(self, table_name: str,) -> Cursor:  # type: ignore
        pass

    @abstractclassmethod
    def update(self, table_name: str, data: list[DataColumn], key: int):
        pass

    @abstractclassmethod
    def delete(self, table_name: str, key: int):
        pass

    @abstractclassmethod
    def find(self, table_name: str, key: int) -> Cursor:  # type: ignore
        pass


class DatabaseIMPL(Database):
    def __init__(self, database_name: str) -> None:
        super().__init__()
        self.__db = sql.connect(database_name).cursor()

    def create_table(self, name: str, columns: list[Column]):
        number_of_tables = len(self.__db.execute(
            '''
            SELECT name FROM sqlite_master WHERE type='table' AND name='{}';
            '''.format(name)
        ).fetchall())
        if number_of_tables > 0:
            return
        columns_in_text = ''
        for column in columns:
            comma = ','
            if columns.index(column) == (len(columns)-1):
                comma = ''
            columns_in_text += '{} {}{}'.format(column.name,
                                                column.type.value, comma)
        query = '''
                          CREATE TABLE {}
                          (
                              ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                              {}
                          );
                          '''.format(name, columns_in_text)
        self.__db.execute(query)
        self.__commit()

    def drop_table(self, name: str):
        query = '''
        DROP TABLE {};
        '''.format(name)
        self.__db.execute(query)

        self.__commit()

    def insert(self, table_name: str, data: SQLTableData):
        column_names = ''
        column_values = ''
        for tData in data.data:
            comma = ','
            if data.data.index(tData) == (len(data.data)-1):
                comma = ''
            column_names += ' {} {}'.format(tData.name, comma)
            val = None
            if(tData.type == SQLDataType.text):
                val = '"{}"'.format(tData.data)
            else:
                val = tData.data
            column_values += ' {} {}'.format(val, comma)

        query = '''
        INSERT INTO {} ({}) VALUES ({});
        '''.format(table_name, column_names, column_values)
        self.__db.execute(query)
        self.__commit()

    def read(self, table_name: str) -> Cursor:
        query = '''
        SELECT * FROM {};
        '''.format(table_name)
        return self.__db.execute(query)

    def update(self, table_name: str, data: SQLTableData, key: int):
        columns_and_values = ''
        for t_data in data.data:
            comma = ','
            if data.data.index(t_data) == (len(data.data)-1):
                comma = ''

            val = None
            if(t_data.type == SQLDataType.text):
                val = '"{}"'.format(t_data.data)
            else:
                val = t_data.data
            columns_and_values += ' {} = {}{}'.format(t_data.name, val, comma)

        query = '''
        UPDATE {} SET {} WHERE ID = {};
        '''.format(table_name, columns_and_values, key)
        self.__db.execute(query)
        self.__commit()

    def delete(self, table_name: str, key: int):
        query = '''
        DELETE FROM {} WHERE ID={}
        '''.format(table_name, key)
        print(query)
        self.__db.execute(query)
        self.__db.connection.commit()

    def find(self, table_name: str, key: int) -> Cursor:
        query = '''
        SELECT * FROM {} WHERE ID={}
        '''.format(table_name, key)
        print(query)
        return self.__db.execute(query)

    def __commit(self):
        self.__db.connection.commit()

    def close(self):
        self.__db.close()
