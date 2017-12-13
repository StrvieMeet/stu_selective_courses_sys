class Course:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.teacher = []



class School:
    def __init__(self,campus,price):
        self.campus = campus



class Classes:
    def __init__(self, name,price):
        self.name = name
        self.teacher = []
        self.student = []




class Student:
    def __init__(self, name,price):
        self.name = name
        self.classes = []
        self.student = []


class Teacher:
    def __init__(self, name,price):
        self.name = name
        self.classes = []
        self.student = []


if __name__ == '__main__':
    pass