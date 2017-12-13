import os
from collections import OrderedDict
# 导入这个模块，这个是创建有序字典的模块
from conf import settings
from core.public_class import Person
from core import teacher
from core.pickle_handler import Mypickle
from core.course import *

class Manager(Person):
    # 创建一个类，继承了Person父类，在父类中进行初始化
    role = '管理员'

    operate = OrderedDict([('1',['创建课程', 'create','courses_info_file','课程',Course]),
                           ('2',['创建班级', 'create','classes_info_file','班级',Classes]),
                           ('3',['创建学员账号', 'create','students_info_file','学员',Student]),
                           ('4',['创建讲师账号', 'create','teachers_info_file','讲师',Teacher]),
                           ('5',['查看讲师', 'check','teachers_info_file','讲师']),
                           ('6',['查看班级', 'check','classes_info_file','班级']),
                           ('7',['查看课程', 'check','courses_info_file','课程']),
                           ('8',['给课程关联讲师', 'combine_teacher_course']),
                           ('9',['退出', 'quit']),
                           ])
    # 定义一个有序字典赋值给opeate

    def choose(self):
        '''
        选择操作
        :return:
        '''
        for item in Manager.operate:
            # 循环operate这个有序字典
            print(item,Manager.operate[item][0])
            # 循环打印有序字典中的内容
        num = input('请输入您要进行操作的序号 ： ')
        # 让用户输入要操作的序号
        try:
            operate = Manager.operate[num]
            return operate

        except:
            # 否则就捕获异常
            print('您输入的序号有误。')
            # 然后打印您输入的序号有误

    def check(self,check_file,check_theme):
        '''
        查看
        :param check_file:
        :param check_theme:
        :return:
        '''
        check_info_dic = Mypickle.load(check_file)
        # 通过传入的文件路径将数据序列化出来
        if check_info_dic:
            # 判断是否为空
            for info in check_info_dic:
                # 循环获取的内容
                print('\033[45;1m{}\033[0m'.format(info))
                # 进行打印
                for attr in check_info_dic[info].__dict__:
                    if not attr.startswith('_'):
                        print('\t\t%s %s' % (attr, check_info_dic[info].__dict__[attr]))
                        # print(check_info_dic[info].__dict__[attr])
        else:
            print('目前还没有可以查看的%s～'%check_theme)

    def create(self,create_file,create_name,func,price):

        if func == Teacher:
            func_obj = teacher.Teacher.register(create_name)
            if func_obj:
                # 判断这个实例化的类有没有
                teacher_info_dic = Mypickle.load(create_file)
                # 调用自己定义的一个文件读取的方法，参数是配置文件中写如的路径
                if func_obj.name in teacher_info_dic:
                    # 如果实例化这个对象的name在读取的文件中
                    print('您要创建的{}名已经存在！'.format(create_name))
                    # 打印已经存在一个同名的讲师
                else:

                    teacher_info_dic[func_obj.name] = func_obj
                    # 否则在返回的空字典中设置一对键值
                    Mypickle.dump(teacher_info_dic, settings.teachers_info_file)
                    # 然后将新创建的字典通过文件写入到配置文件中的路径文件中
                    print('{}创建成功！'.format(create_name))
                    # 打印讲师账号创建成功
        else:
            files_info_dic = Mypickle.load(create_file)
            files_dir = os.path.join(settings.db_path, create_name)
            if create_name in files_info_dic and os.path.exists(files_dir):
                print('您要创建的{}名已经存在！'.format(create_name))
            else:
                os.makedirs(files_dir, exist_ok=True)
                student_obj = func(create_name,price)
                files_info_dic[create_name] = student_obj
                Mypickle.dump(files_info_dic, create_file)
                print('{}创建成功！'.format(create_name))

    def combine_teacher_course(self):
        teachers_info_dict = Mypickle.load(settings.teachers_info_file)
        courses_info_dict = Mypickle.load(settings.courses_info_file)
        if teachers_info_dict and courses_info_dict:
            print('teachers : ', end='')
            for teacher in teachers_info_dict:
                print(teacher, end='|')
            print()
            print('courses : ', end='')
            for course in courses_info_dict:
                print(course, end='|')
            print()
            while True:
                try:
                    teacher, course = input('请输入要关联的讲师和课程，用&链接 : ').split('&')
                    if teacher in teachers_info_dict and course in courses_info_dict:
                        teachers_info_dict[teacher].course.append(courses_info_dict[course])
                        courses_info_dict[course].teacher.append(courses_info_dict[course])
                        Mypickle.dump(teachers_info_dict, settings.teachers_info_file)
                        Mypickle.dump(courses_info_dict, settings.courses_info_file)
                        print('关联成功！')
                        break
                except:
                    print('您输入的内容有误，请重新输入。')

        else:
            print('请先创建讲师或者课程')

    def quit(self):

        quit()


# if __name__ == '__main__':
        #     operate = OrderedDict([('创建课程', 'create_courses'),
        #                            ('创建班级', 'create_classes'),
        #                            ('创建学员账号', 'create_student'),
        #                            ('创建讲师账号', 'create_teacher'),
        #                            ('查看讲师', 'check_teacher_info'),
        #                            ('查看班级', 'check_class_info'),
        #                            ('查看课程', 'check_course_info'),
        #                            ])
        #     for n,o in enumerate(operate,1):
        #         print(n,o)

# def check_teacher_info(self):
#     self.check(settings.teachers_info_file, '讲师')
#
# def check_class_info(self):
#     self.check(settings.classes_info_file, '班级')
#
# def check_student_info(self):
#     self.check(settings.students_info_file, '学生')
#
# def check_course_info(self):
#     self.check(settings.courses_info_file, '课程')

# def create_courses(self):
#     '''
#     创建课程
#     :return:
#     '''
#     course_info_dic = Mypickle.load(settings.courses_info_file)
#     course_name = input('请输入您要创建的课程名 ： ')
#     course_dir = os.path.join(settings.db_path,course_name)
#     if course_name in course_info_dic and os.path.exists(course_dir):
#         print('您要创建的课程名已经存在！')
#     else:
#         os.makedirs(course_dir,exist_ok=True)
#         course_price = input('请输入您要创建课程的价格 ： ')
#         course_obj = Course(course_name,course_price)
#         course_info_dic[course_name] = course_obj
#         Mypickle.dump(course_info_dic,settings.courses_info_file)
#         print('课程创建成功！')
#
# def create_classes(self):
#     '''
#     创建班级
#     :return:
#     '''
#     classes_info_dic = Mypickle.load(settings.classes_info_file)
#     classes_name = input('请输入您要创建的班级名 ： ')
#     classes_dir = os.path.join(settings.db_path, classes_name)
#     if classes_name in classes_info_dic and os.path.exists(classes_dir):
#         print('您要创建的班级名已经存在！')
#     else:
#         os.makedirs(classes_dir, exist_ok=True)
#         classes_obj = Classes(classes_name)
#         classes_info_dic[classes_name] = classes_obj
#         Mypickle.dump(classes_info_dic, settings.classes_info_file)
#         print('课程创建成功！')
#
# def create_teacher(self):
#             '''
#             创建老师
#             :return:
#             '''
#             teacher_obj = Teacher.register()
#             # 调用用户注册方法，最后返回一个teacher实例化的对象
#             if teacher_obj:
#                 # 判断这个实例化的类有没有
#                 teacher_info_dic = Mypickle.load(settings.teachers_info_file)
#                 # 调用自己定义的一个文件读取的方法，参数是配置文件中写如的路径
#                 if teacher_obj.name in teacher_info_dic:
#                     # 如果实例化这个对象的name在读取的文件中
#                     print('已经存在一个同名的讲师')
#                     # 打印已经存在一个同名的讲师
#                 else:
#
#                     teacher_info_dic[teacher_obj.name] = teacher_obj
#                     # 否则在返回的空字典中设置一对键值
#                     Mypickle.dump(teacher_info_dic, settings.teachers_info_file)
#                     # 然后将新创建的字典通过文件写入到配置文件中的路径文件中
#                     print('讲师账号创建成功！')
#                     # 打印讲师账号创建成功
#
# def create_student(self):
#     '''
#     创建班级
#     :return:
#     '''
#     student_info_dic = Mypickle.load(settings.students_info_file)
#     student_name = input('请输入您要创建的学生名 ： ')
#     student_dir = os.path.join(settings.db_path, student_name)
#     if student_name in student_info_dic and os.path.exists(student_dir):
#         print('您要创建的学生名已经存在！')
#     else:
#         os.makedirs(student_dir, exist_ok=True)
#         student_obj = Student(student_name)
#         student_info_dic[student_name] = student_obj
#         Mypickle.dump(student_info_dic, settings.students_info_file)
#         print('学生创建成功！')

# 找到函数就返回函数
# operate1 = Manager.operate[num][0]
# # 从有序字典中查找用户输入的值对应的名称
# operate = Manager.operate[num][1]
# # 从有序字典中查找用户输入的值对应的函数
# operate2 = Manager.operate[num][2]
# # 从有序字典中查找用户输入的值对应的绝对路径
# operate3 = Manager.operate[num][3]
# # 从有序字典中查找用户输入的值对应的类型
# return operate1,operate,operate2,operate3
# 找到函数就返回函数