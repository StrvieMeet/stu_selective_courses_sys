#!/usr/bin/env python
# encoding: utf-8

"""
@author: Meet
@file: 选课系统.py
@time: 2017/12/4 02:17
"""
import hashlib
import os
import pickle

class My_pickle:
    '''
    序列化
    '''
    def __init__(self,file_dir,object = None):
        # 初始化
        self.file_dir = file_dir
        # 使用这个类就要将文件的路径进行初始化
        self.object = object
        # 使用这个类就要将要进行dump时的对象

    def dump(self):
        # 序列化文件写入
        with open(self.file_dir, 'wb+') as f:
            # 按照文件的路径打开文件然后写入数据并获取文件句柄
            ret = pickle.dumps(self.object)
            # 将对象进行序列化
            f.write(ret)
            # 获取序列化的内容经行写入

    def load(self):
        '''
        :param path:
        :return:
        '''
        # 序列化文件读出
        if os.path.getsize(self.file_dir):
            # 如果文件的打小不为空
            with open(self.file_dir, 'rb') as f:
                # 按照文件的路径打开文件然后写入数据并获取文件句柄
                    ret = pickle.load(f)
                    # 统一对文件进行转换
        else:
            # 否则就返回一个空字典
            ret = {}
        return ret

class ElectiveSystem():
    '''
    选课系统
    '''

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 通过当前的文件获取到当前文件的父目录的父目录
    user_info_dir = os.path.join(BASE_DIR, 'user_info')
    # 使用总目录和user_info表进行文件路径拼接然后赋值给user_info_dir


    def verification(self,user,pwd):
        '''
        加密函数
        :param user:
        :param pwd:
        :return:
        '''
        md5obj = hashlib.md5((user).encode('utf-8'))
        # 使用md5方式加密，设置加盐，盐是每次传入的用户名
        md5obj.update(pwd.encode('utf-8'))
        # 对传入的密码进行加密
        passwd = md5obj.hexdigest()
        # 通过盐和要进行加密的密码合成一个密文
        return user,passwd
        # 返回用户的用户名以及进行md5的密码

    def auth(self,user,pwd):
        '''
        登陆验证
        :param user:
        :param pwd:
        :return:
        '''
        new_user,new_pwd = self.verification(user,pwd)
        # 调用加密方法，获取加密后的用户名和密码
        with open(self.user_info_dir, encoding='utf-8')as f:
        # 按照文件的路径打开文件然后写入数据并获取文件句柄
            for line in f:
                # 遍历文件中的内容
                name, pwds, role = line.strip().split('|')
                # 把遍历的内容通过空格来分割，分别得到名称，密码的密文，身份
                if name == new_user and new_pwd == pwds:
                    # 判断用户输入的用户名和密码密文是不是和文件中的用户名密码密文相等
                    return role
                    # 如果相等就返回这个用户对应的角色
            return None
            # 没有匹配成功后就返回None

    def file_operation(self,file_user,file_password,role):
        '''
        文件操作
        :param file_user:
        :param file_password:
        :param role:
        :return:
        '''
        with open(self.user_info_dir, 'a+',encoding='utf8')as f:
            # 按照文件的路径打开文件然后写入数据并获取文件句柄
            f.write("\n{}|{}|{}".format(file_user, file_password, role))
            # 将用户名，加密后的密码以及角色写入到文件中

    def login(self):
        '''
        登陆系统
        :return:
        '''
        print('-'*20+"欢迎登陆选课系统"+'-'*20)
        # 打印欢迎的语句
        user = input('请输入要登录的用户名：')
        # 让用户输入用户名然后获取到变量中
        pwd = input('请输入要登录的密码：')
        # 让用户输入密码然后获取到变量中
        role = self.auth(user,pwd)
        # 调用登陆验证，然后接受返回值
        if role:
            # 判断如果返回的值不为空
            print('-'*20+"当前用户是{}".format(role)+'-'*20)
            # 打印当前登陆的用户
            if role == 'Manager':
                # 因为返回的是一个元祖，判断元祖中第一个元素是不是等于Manager
                dic ={
                    1:['创建学校',self.create_school],
                    2:['创建课程',self.create_course],
                    3:['创建讲师',self.create_teacher],
                    4:['创建学员',self.create_student],
                    5:['创建班级',self.create_classes],
                    6:['查看学校',self.check_school],
                    7:['查看课程',self.check_course],
                    8:['查看讲师',self.check_teacher],
                    9:['查看学员',self.check_student],
                    10:['查看班级',self.check_classes],
                    11:['课程关联班级',self.course_Relate_classes],
                    12:['课程关联讲师',self.course_Relate_teacher],
                    13:['班级关联学生',self.classes_Relate_student]
                }
                # 如果等于的话就定一个字典，字典中存放着操作显示以及操作对应的函数
                while True:
                    # 循环
                    try:
                        # 异常捕获
                        for k in dic.keys():
                            # 循环字典的key
                            print(k,dic[k][0])
                            # 打印定义的序号和序号对应的内容
                        choice = input("请输入您要选择的序号：")
                        # 让用户输入要选择操作的序号，赋值给一个变量
                        dic.get(int(choice))[1]()
                        # 通过用户输入的内容获取字典中定义相对应的函数加括号执行
                    except:
                        print('-'*20+'请正确输入！'+'-'*20)
                        continue
                        # 否则跳过本次循环
            elif  role == 'Teahcer':
                pass
            elif role == 'Studnet':
                pass
        else:
            print('-'*10+"您输入的用户名或密码错误！"+'-'*10)
            # 如果获取的内容不是以上可以匹配的就表示用户名和密码不存在！

    def create_school(self):
        '''
        创建学校
        :return:
        '''
        schools = input("请输入要创建的学校：")
        # 让用户输入要创建的学校
        school_info_dir = os.path.join(self.BASE_DIR, 'school_info')
        # 使用总目录和school_info表进行文件路径拼接并赋值给school_info_dir变量
        my_load = My_pickle(school_info_dir)
        # 对My_pickle类进行实例化
        file_object_dic = my_load.load()
        # 通过实例化的对象调用类方法，并接收序列化回来的字典
        if schools in file_object_dic:
            # 判断用户输入在不在序列化出来的字典中
            print('-'*20+'您要创建的学校已存在！'+'-'*20)
            # 打印您要创建的学校已存在！
        file_object_dic[schools] = schools
        # 如果返回的字典是一个空，就对字典进行设置键值对
        my_dumps = My_pickle(school_info_dir, file_object_dic)
        # 对My_pickle类进行实例化
        my_dumps.dump()
        # 通过实例化的对象调用类方法
        print('-'*20+'创建学校成功！'+'-'*20)
        # 打印创建学校成功！

    def create_course(self):
        '''
        创建课程
        :return:
        '''
        course = input("请输入要创建的课程：")
        # 让用户输入要创建的课程，并赋值到变量中
        price = input("请输入课程的价格：")
        # 让用户输入要创建的课程价格，并赋值到变量中
        course_info_dir = os.path.join(self.BASE_DIR, 'course_info')
        # 使用总目录和school_info表进行文件路径拼接并赋值给course_info_dir变量
        my_load = My_pickle(course_info_dir)
        # 对My_pickle类进行实例化
        file_object_dic = my_load.load()
        # 通过实例化的对象调用类方法
        if course in file_object_dic:
            # 判断用户输入在不在序列化出来的字典中
            print('-' * 20 + '您要创建的课程已存在！' + '-' * 20)
            # 打印您要创建的课程已存在！
        file_object_dic[course] = [course,price]
        # 如果返回的字典是一个空，就对字典进行设置键值对
        file_object_dic[course].append({'classes':[]})
        # 对新创建的字典进行添加值
        file_object_dic[course].append({'teacher':[]})
        # 对新创建的字典进行添加值
        my_dumps = My_pickle(course_info_dir, file_object_dic)
        # 对My_pickle类进行实例化
        my_dumps.dump()
        # 通过实例化的对象调用类方法
        print('-' * 20 + '创建课程成功！' + '-' * 20)
        # 打印创建课程成功

    def create_teacher(self):
        '''
        创建讲师
        :return:
        '''
        teacher = input("请输入要创建的讲师：")
        # 让用户输入要创建的讲师，并赋值到变量中
        teacher_pwd = input("请输入讲师的密码：")
        # 让用户输入要创建的讲师密码，并赋值到变量中
        role = self.auth(teacher,teacher_pwd)
        # 调用登陆验证，然后接受返回值
        if not role:
            # 判断如果role没有值
            teacher_info_dir = os.path.join(self.BASE_DIR, 'teacher_info')
            # 使用总目录和teacher_info表进行文件路径拼接并赋值给teacher_info_dir变量
            my_load = My_pickle(teacher_info_dir)
            # 对My_pickle类进行实例化
            file_object_dic = my_load.load()
            # 通过实例化的对象调用类方法
            if teacher in file_object_dic:
                # 判断用户输入在不在序列化出来的字典中
                print('-' * 20 + '您要创建的讲师已存在！' + '-' * 20)
                # 打印您要创建的讲师已存在
            file_object_dic[teacher] = [teacher]
            # 如果不在的话就为这个字典设置键值对
            file_object_dic[teacher].append({'course':[]})
            # 对新创建的字典的值添加一个新的键值对
            my_dumps = My_pickle(teacher_info_dir, file_object_dic)
            # 对My_pickle类进行实例化
            my_dumps.dump()
            # 通过实例化的对象调用类方法
            new_teacher,new_teacher_pwd = self.verification(teacher,teacher_pwd)
            # 对输入的老师帐号和密码进行加密，然后返回最新的用户名，密码
            self.file_operation(new_teacher,new_teacher_pwd,'Teacher')
            # 将要创建的用户名和密码以及角色写入到文件中
            print('-' * 20 + '创建讲师成功！' + '-' * 20)
            # 打印创建讲师成功！
        else:
            print('-' * 20 + '您要创建的讲师已存在！' + '-' * 20)
            # 否则就打印您要创建的讲师已存在

    def create_student(self):
        '''
        创建学员
        :return:
        '''

        student = input("请输入要创建的学员：")
        # 用户输入要创建的学生用户，并赋值到变量中
        student_pwd = input("请输入学员的密码：")
        # 用户输入要创建的学生密码，并赋值到变量中
        role = self.auth(student, student_pwd)
        # 调用登陆验证，然后接受返回值
        if not role:
            # 判断如果role没有值
            student_info_dir = os.path.join(self.BASE_DIR, 'student_info')
            # 使用总目录和teacher_info表进行文件路径拼接并赋值给teacher_info_dir变量
            my_load = My_pickle(student_info_dir)
            # 对My_pickle类进行实例化
            file_object_dic = my_load.load()
            # 通过实例化的对象调用类方法
            if student in file_object_dic:
                # 判断用户输入在不在序列化出来的字典中
                print('-' * 20 + '您要创建的学员已存在！' + '-' * 20)
                # 打印您要创建的学员已存在
            file_object_dic[student] = [student]
            # 如果不在的话就为这个字典设置键值对
            file_object_dic[student].append({'couser':[]})
            # 对新创建的字典的值添加一个新的键值对
            my_dumps = My_pickle(student_info_dir, file_object_dic)
            # 对My_pickle类进行实例化
            my_dumps.dump()
            # 通过实例化的对象调用类方法
            new_student, new_student_pwd = self.verification(student, student_pwd)
            # 对输入的老师帐号和密码进行加密，然后返回最新的用户名，密码
            self.file_operation(new_student, new_student_pwd,'Student')
            # 将要创建的用户名和密码以及角色写入到文件中
            print('-' * 20 + '创建学员成功！' + '-' * 20)
            # 打印创建讲师成功！
        else:
            print('-' * 20 + '您要创建的讲师已存在！' + '-' * 20)
            # 否则就打印您要创建的讲师已存在

    def create_classes(self):
        '''
        创建班级
        :return:
        '''
        classes = input("请输入要创建的班级：")
        # 让用户输入要创建的班级
        classes_info_dir = os.path.join(self.BASE_DIR, 'classes_info')
        # 使用总目录和classes_info表进行文件路径拼接并赋值给classes_info_dir变量
        my_load = My_pickle(classes_info_dir)
        # 对My_pickle类进行实例化
        file_object_dic = my_load.load()
        # 通过实例化的对象调用类方法
        if classes in file_object_dic:
            # 判断用户输入的内容在不在序列化出来的字典中
            print('-' * 20 + '您要创建的班级已存在！' + '-' * 20)
            # 打印您要创建的班级已存在
        file_object_dic[classes] = [classes]
        # 如果字典为空，就为字典设置键值对
        file_object_dic[classes].append({'couser':[]})
        # 对设置的值进行添加键值对
        file_object_dic[classes].append({'student':[]})
        # 对设置的值进行添加键值对
        my_dumps = My_pickle(classes_info_dir, file_object_dic)
        # 对My_pickle类进行实例化
        my_dumps.dump()
        # 通过实例化的对象调用类方法
        print('-' * 20 + '创建班级成功！' + '-' * 20)
        # 打印创建班级成功

    # 查看相关函数
    def check_school(self):
        '''
        查看学校
        :return:
        '''
        file_dir = os.path.join(self.BASE_DIR,'school_info')
        my_pickle = My_pickle(file_dir)
        school_info_dic = my_pickle.load()
        if school_info_dic:
            for school_name in list(school_info_dic.keys()):
                print('-'*20+'学校名称：'+school_name+'-'*20)
        else:
            print("{}还没有创建！".format('学校'))

    def check_course(self):
        '''
        查看课程
        :return:
        '''
        file_dir = os.path.join(self.BASE_DIR, 'course_info')
        my_pickle = My_pickle(file_dir)
        course_info_dic = my_pickle.load()
        if course_info_dic:
            for school_name in list(course_info_dic.keys()):
                print('-' * 5 + '课程名称：{} ;课程价格：{};班级：{}; 讲师：{}'.format(course_info_dic[school_name][0],
                                                                       course_info_dic[school_name][1],
                                                                       course_info_dic[school_name][2]['classes'],
                                                                       course_info_dic[school_name][3]['teacher'])
                      +'-'*5)

        else:
            print("{}还没有创建！".format('讲师'))

    def check_teacher(self):
        '''
        查看讲师
        :return:
        '''
        file_dir = os.path.join(self.BASE_DIR, 'teacher_info')
        my_pickle = My_pickle(file_dir)
        teacher_info_dic = my_pickle.load()
        if teacher_info_dic:
            for teacher_name in list(teacher_info_dic.keys()):
                print('-' * 20 +'讲师：{};课程：{}'.format(teacher_info_dic[teacher_name][0],
                                                     teacher_info_dic[teacher_name][1]['course'])
                      +'-' * 20)
        else:
            print("{}还没有创建！".format('讲师'))

    def check_student(self):
        '''
        查看学员
        :return:
        '''
        file_dir = os.path.join(self.BASE_DIR, 'student_info')
        my_pickle = My_pickle(file_dir)
        student_info_dic = my_pickle.load()
        if student_info_dic:
            for student_name in list(student_info_dic.keys()):
                print('-' * 20 +'学生：{};课程：{}'.format(student_info_dic[student_name][0],
                                                     student_info_dic[student_name][1]['couser'])
                      + '-' * 20)
        else:
            print("{}还没有创建！".format('学生'))

    def check_classes(self):
        '''
        查看班级
        :return:
        '''
        file_dir = os.path.join(self.BASE_DIR, 'classes_info')
        my_pickle = My_pickle(file_dir)
        classes_info_dic = my_pickle.load()
        if classes_info_dic:
            for classes_name in list(classes_info_dic.keys()):
                print('-' * 20 +'班级：{} ;课程：{}; 学生：{}'.format(classes_info_dic[classes_name][0],
                                                             classes_info_dic[classes_name][1]['couser'],
                                                             classes_info_dic[classes_name][2]['student'])
                      + '-' * 20)
        else:
            print("{}还没有创建！".format('课程'))

    def course_Relate_classes(self):
        '''
        课程关联班级
        :return:
        '''
        course_dir = os.path.join(self.BASE_DIR, 'course_info')
        classes_dir = os.path.join(self.BASE_DIR, 'classes_info')
        course_pickle = My_pickle(course_dir)
        classes_pickle = My_pickle(classes_dir)
        courses_info_dict = course_pickle.load()
        classes_info_dict = classes_pickle.load()
        if courses_info_dict and classes_info_dict:
            print('courses : ', end='')
            for courses in courses_info_dict:
                print(courses, end='|')
            print()
            print('classes : ', end='')
            for classes in classes_info_dict:
                print(classes, end='|')
            print()
            while True:
                try:
                    courses, classes = input('请输入要关联的课程和班级，用&链接 : ').split('&')
                    if courses in courses_info_dict and classes in classes_info_dict:
                        courses_info_dict[courses][2]['classes'].append(classes_info_dict[classes][0])
                        classes_info_dict[classes][1]['couser'].append(courses_info_dict[courses][0])
                        My_pickle(course_dir,courses_info_dict).dump()
                        My_pickle(classes_dir,classes_info_dict).dump()
                        print('关联成功！')
                        break
                except:
                    print('您输入的内容有误，请重新输入！')

        else:
            print('请先创建课程或者班级！')

    def course_Relate_teacher(self):
        '''
        课程关联讲师
        :return:
        '''
        course_dir = os.path.join(self.BASE_DIR, 'course_info')
        teacher_dir = os.path.join(self.BASE_DIR, 'teacher_info')
        course_pickle = My_pickle(course_dir)
        teacher_pickle = My_pickle(teacher_dir)
        courses_info_dict = course_pickle.load()
        teacher_info_dict = teacher_pickle.load()
        if courses_info_dict and teacher_info_dict:
            print('courses : ', end='')
            for courses in courses_info_dict:
                print(courses, end='|')
            print()
            print('teacher : ', end='')
            for teacher in teacher_info_dict:
                print(teacher, end='|')
            print()
            print(courses_info_dict,teacher_info_dict)
            while True:
                try:
                    courses, teacher = input('请输入要关联的课程和讲师，用&链接 : ').split('&')
                    if courses in courses_info_dict and teacher in teacher_info_dict:
                        courses_info_dict[courses][3]['teacher'].append(teacher_info_dict[teacher][0])
                        teacher_info_dict[teacher][1]['course'].append(courses_info_dict[courses][0])
                        My_pickle(course_dir, courses_info_dict).dump()
                        My_pickle(teacher_dir, teacher_info_dict).dump()
                        print('关联成功！')
                        break
                except:
                    print('您输入的内容有误，请重新输入！')

        else:
            print('请先创建课程或者讲师！')

    def classes_Relate_student(self):
        '''
        班级关联学生
        :return:
        '''
        classes_dir = os.path.join(self.BASE_DIR, 'classes_info')
        student_dir = os.path.join(self.BASE_DIR, 'student_info')
        classes_pickle = My_pickle(classes_dir)
        student_pickle = My_pickle(student_dir)
        classes_info_dict = classes_pickle.load()
        student_info_dict = student_pickle.load()
        if classes_info_dict and student_info_dict:
            print('classes : ', end='')
            for classes in classes_info_dict:
                print(classes, end='|')
            print()
            print('teacher : ', end='')
            for student in student_info_dict:
                print(student, end='|')
            print()
            print(classes_info_dict, student_info_dict)
            while True:
                try:
                    classes, student = input('请输入要关联的班级和学生，用&链接 : ').split('&')
                    if classes in classes_info_dict and student in student_info_dict:
                        student_info_dict[student][1]['couser'].append(classes_info_dict[classes][0])
                        classes_info_dict[classes][2]['student'].append(student_info_dict[student][0])
                        My_pickle(classes_dir, classes_info_dict).dump()
                        My_pickle(student_dir, student_info_dict).dump()
                        print('关联成功！')
                        break
                except:
                    print('您输入的内容有误，请重新输入！')

        else:
            print('请先创建课程或者讲师！')


if __name__ == '__main__':
    ele = ElectiveSystem()
    # 实例化对象
    while True:
        ele.login()
        # 通过对象来调用登陆方法