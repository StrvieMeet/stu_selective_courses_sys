import pickle
import hashlib
from core.course import *
from conf import settings

class Person:
    '''
    创建一个父类，所有的方法都继承这个类
    '''
    def __init__(self,name,pwd):
        # 初始化
        self.name = name
        self.__pwd = pwd
        self.course = []
        self.classes = []

    @classmethod
    def pwd(cls,name,pwd):
        md5obj = hashlib.md5((name).encode('utf-8'))
        md5obj.update((pwd).encode('utf-8'))
        return md5obj.hexdigest()

    @classmethod
    def register(cls,username):
        '''
        注册用户
        :return:
        '''
        ret = cls.get_register_info(username)
        # 调用执行获取注册用户的这个方法，并接收返回的name，pwd参数
        if ret:
            # 判读是否有参数
            name,pwd = ret[0],ret[1]
            # 因为返回多个参数得到的是一个元祖，从元祖中获取用户名和密码
            teacher_obj = cls(name,pwd)
            # 实例化teacher这个类    <core.teacher.Teacher object at 0x036ED290>
            return teacher_obj
            # 返回实例化的对象
        else:
            # 否则就返回None
            return

    @classmethod
    def get_register_info(cls,username):
        '''
        获取注册用户
        :return:
        '''
        while True:
            pwd = input('请输入%s的密码 : '%cls.role).strip()
            # 循环获取用户输入的密码使用字符串拼接，那个类实例化调用就是那个类的类变量
            pwd2 = input('请确认%s的密码,输入q退出 ：'%cls.role).strip()
            # 循环获取用户输入的密码使用字符串拼接，那个类实例化调用就是那个类的类变量
            if pwd2.lower() == 'q':
                # 如果第二次输入的内容是q就退出
                return
                # 结束本次循环
            if pwd and pwd == pwd2:
                # 判断密码不为空且俩次密码是否一致
                with open(settings.user_info_file,'a+') as f:
                    # 打开配置文件中设置的文件
                    f.write('\n%s %s %s'%(username,cls.pwd(username,pwd2),cls.__name__))
                    # 将创建的用户进行保存
                return username, pwd
                # 然后返回用户名和密码
            else:
                continue
                # 否则就跳出当前循环

    @staticmethod
    def get_user_info():
        pass

    def load_teachers(self):
        pass

    def load_students(self):
        pass

    def load_coursers(self):
        pass

    def load_classes(self):
        pass