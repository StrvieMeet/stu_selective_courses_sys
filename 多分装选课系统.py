#!/usr/bin/env python
# encoding: utf-8

"""
@author: Meet
@file: 多分装选课系统.py
@time: 2017/12/4 8:29
"""
#!/usr/bin/env python
# encoding: utf-8

"""
@author: Meet
@file: 选课系统.py
@time: 2017/11/30 20:17
"""
import hashlib
import os
import pickle

class My_pickle:
    '''
    序列化
    '''
    def __init__(self,file_dir,object = None):
        self.file_dir = file_dir
        self.object = object

    def dump(self):
        # 文件写入
        with open(self.file_dir, 'wb+') as f:
            # 按照文件的路径打开文件写数据
            ret = pickle.dumps(self.object)
            # 写入数据
            f.write(ret)

    def load(self):
        '''
        :param path:
        :return:
        '''
        if os.path.getsize(self.file_dir):
            # 判断文件的大小
            with open(self.file_dir, 'rb') as f:
                # 按照文件的路径打开文件读取数据
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
    user_info_dir = os.path.join(BASE_DIR, 'user_info')

    def __init__(self):
        pass

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

    def auth(self,user,pwd):
        '''
        登陆验证
        :param user:
        :param pwd:
        :return:
        '''
        new_user,new_pwd = self.verification(user,pwd)
        with open(self.user_info_dir, encoding='utf-8')as f:
        # 打开用户的路径文件
            for line in f:
                # 遍历文件中的内容
                name, pwds, role = line.strip().split('|')
                # 把遍历的内容通过空格来分割，分别得到名称，密码的密文，身份
                if name == new_user and new_pwd == pwds:
                    # 判断用户输入的用户名和密码密文是不是和文件中的用户名密码密文相等
                    return role,pwd
                    # 如果相等就返回这个用户对应的角色
            return None

    def file_operation(self,file_user,file_password,role):
        '''
        文件操作
        :param file_user:
        :param file_password:
        :param role:
        :return:
        '''
        with open(self.user_info_dir, 'a+')as f:
            f.write("\n{}|{}|{}".format(file_user, file_password, role))

    def login(self):
        '''
        登陆系统
        :return:
        '''
        print('-'*20+"欢迎登陆选课系统"+'-'*20)
        user = input('请输入要登录的用户名：')
        pwd = input('请输入要登录的密码：')
        role = self.auth(user,pwd)
        if role:
            print('-'*20+"当前用户是{}".format(role[0])+'-'*20)
            if role[0] == 'Manager':
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
                while True:
                    try:
                        for k in dic.keys():
                            print(k,dic[k][0])
                        choice = input("请输入您要选择的序号：")
                        dic.get(int(choice))[1]()
                    except:
                        # print("请输入您要选择的序号：")
                        continue
        else:
            print('-'*10+"您输入的用户名或密码错误！"+'-'*10)
    def create_school(self):
        '''
        创建学校
        :return:
        '''
        schools = input("请输入要创建的学校：")
        school_info_dir = os.path.join(self.BASE_DIR, 'school_info')
        my_load = My_pickle(school_info_dir)
        file_object_dic = my_load.load()
        if schools in file_object_dic:
            print('-'*20+'您要创建的学校已存在！'+'-'*20)
        file_object_dic[schools] = schools
        my_dumps = My_pickle(school_info_dir, file_object_dic)
        my_dumps.dump()
        print('-'*20+'创建学校成功！'+'-'*20)

    def create_course(self):
        '''
        创建课程
        :return:
        '''
        course = input("请输入要创建的课程：")
        price = input("请输入课程的价格：")
        course_info_dir = os.path.join(self.BASE_DIR, 'course_info')
        my_load = My_pickle(course_info_dir)
        file_object_dic = my_load.load()
        if course in file_object_dic:
            print('-' * 20 + '您要创建的课程已存在！' + '-' * 20)
        file_object_dic[course] = [course,price]
        file_object_dic[course].append({'classes':[]})
        file_object_dic[course].append({'teacher':[]})
        my_dumps = My_pickle(course_info_dir, file_object_dic)
        my_dumps.dump()
        print('-' * 20 + '创建课程成功！' + '-' * 20)

    def create_teacher(self):
        '''
        创建讲师
        :return:
        '''
        teacher = input("请输入要创建的讲师：")
        teacher_pwd = input("请输入讲师的密码：")
        role = self.auth(teacher,teacher_pwd)
        if not role:
            teacher_info_dir = os.path.join(self.BASE_DIR, 'teacher_info')
            my_load = My_pickle(teacher_info_dir)
            file_object_dic = my_load.load()
            if teacher in file_object_dic:
                print('-' * 20 + '您要创建的讲师已存在！' + '-' * 20)
            file_object_dic[teacher] = [teacher]
            file_object_dic[teacher].append({'course':[]})
            my_dumps = My_pickle(teacher_info_dir, file_object_dic)
            my_dumps.dump()
            new_teacher,new_teacher_pwd = self.verification(teacher,teacher_pwd)
            self.file_operation(new_teacher,new_teacher_pwd,'Teacher')
            print('-' * 20 + '创建讲师成功！' + '-' * 20)
        else:
            print('-' * 20 + '您要创建的讲师已存在！' + '-' * 20)

    def create_student(self):
        '''
        创建学员
        :return:
        '''

        student = input("请输入要创建的学员：")
        student_pwd = input("请输入学员的密码：")
        role = self.auth(student, student_pwd)
        if not role:
            student_info_dir = os.path.join(self.BASE_DIR, 'student_info')
            my_load = My_pickle(student_info_dir)
            file_object_dic = my_load.load()
            if student in file_object_dic:
                print('-' * 20 + '您要创建的学员已存在！' + '-' * 20)
            file_object_dic[student] = [student]
            file_object_dic[student].append({'couser':[]})
            my_dumps = My_pickle(student_info_dir, file_object_dic)
            my_dumps.dump()
            new_student, new_student_pwd = self.verification(student, student_pwd)
            self.file_operation(new_student, new_student_pwd,'Student')
            print('-' * 20 + '创建学员成功！' + '-' * 20)
        else:
            print('-' * 20 + '您要创建的讲师已存在！' + '-' * 20)

    def create_classes(self):
        '''
        创建班级
        :return:
        '''
        classes = input("请输入要创建的班级：")
        classes_info_dir = os.path.join(self.BASE_DIR, 'classes_info')
        my_load = My_pickle(classes_info_dir)
        file_object_dic = my_load.load()
        if classes in file_object_dic:
            print('-' * 20 + '您要创建的班级已存在！' + '-' * 20)
        file_object_dic[classes] = [classes]
        file_object_dic[classes].append({'couser':[]})
        file_object_dic[classes].append({'student':[]})
        my_dumps = My_pickle(classes_info_dir, file_object_dic)
        my_dumps.dump()
        print('-' * 20 + '创建班级成功！' + '-' * 20)


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
    while True:
        ele.login()
