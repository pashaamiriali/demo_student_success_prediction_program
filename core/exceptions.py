class NetworkNotTrainedException(Exception):
    def __init__(self,message: str):
        self.message=message


class NoStudentFoundException(Exception):
    def __init__(self,message: str):
        self.message=message