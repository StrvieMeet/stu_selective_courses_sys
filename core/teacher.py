import hashlib
from core.public_class import Person

class Teacher(Person):
    role = '讲师'

    def check_course(self):
        '''查看目前所教授的课程'''
        for course in self.courses:
            pass

    def check_classes(self):
        '''查看目前所教授的班级'''
        pass

    def check_studens(self,course):
        '''查看自己所带班级的学生'''
        pass

if __name__ == '__main__':
    # ret = Teacher.register()
    # print(ret)
    print(Teacher.__name__)