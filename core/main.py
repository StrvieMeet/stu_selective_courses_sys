import sys
import hashlib
from core.manager import *
from core.student import *
from core.teacher import *
from core.course import *
from conf import settings


def auth(user,passwd):
    '''
    授权函数
    :param user:
    :param passwd:
    :return:
    '''
    md5obj = hashlib.md5((user).encode('utf-8'))
    # 使用md5方式加密，设置加盐，盐是每次传入的用户名
    md5obj.update(passwd.encode('utf-8'))
    # 对传入的密码进行加密
    passwd = md5obj.hexdigest()
    # 通过盐和要进行加密的密码合成一个密文
    f = open(settings.user_info_file,encoding='utf-8')
    # 打开settings中的用户的路径文件
    for line in f:
        # 遍历文件中的内容
        name,pwd,identity = line.strip().split(' ')
        # 把遍历的内容通过空格来分割，分别得到名称，密码的密文，身份
        if name == user and passwd == pwd:
            # 判断用户输入的用户名和密码密文是不是和文件中的用户名密码密文相等
            return identity
            # 如果相等就返回这个用户对应的角色

def login():
    '''
    登录函数
    :return:
    '''
    print('请您先登陆')
    # 打印登陆提示
    while True:
        name = input('请输入您的用户名 ： ').strip()
        # 循环让用户输入用户名
        pwd = input('请输入您的密码 ： ').strip()
        # 循环让用户输入密码
        ret = auth(name,pwd)
        # 调用auth函数，定义这个函数的时需要参数，所以要有参数的传递，并且接收用户的角色
        if ret:
            # 判断获取到参数是不是空
            return name,pwd,ret
            # 如果不为空就返回用户输入的用户名，密码，和身份
        else:
            print('您输入的用户名和密码有误')
            # 否则就提示您输入的用户名和密码有误

def start():
    '''
    项目启动函数
    :return:
    '''
    print(format('欢迎登陆选课系统','^50',))
    # 打印欢迎界面
    name,pwd,ret = login()
    # 调用login函数，然后接收返回的用户名，密码，和身份
    module_obj = sys.modules[__name__]
    # 获取到当前文件对象赋值给module_obj
    if hasattr(module_obj,ret):
        # 通过反射的hasattr判断一下这个文件中有没有角色这个方法
        role_class = getattr(module_obj,ret)
        # 如果有的话就使用反射的getattr获取这个角色的方法
        role_obj = role_class(name,pwd)
        # 找到对应的类，进行实例化对象
        price = None
        #  定义一个空变量
        while True:
            ret = role_obj.choose()
            # 循环调用实例化对象下的choose方法,返回的是一个列表
            if ret and len(ret)>2:
                # 判断获取的列表长度是否是2
                settings_info = getattr(settings, ret[2])
                # 通过反射的方式从settings配置文件中获取有序字典的内容
                if hasattr(role_obj,ret[1]) and ret[1] == 'create':
                    func = getattr(role_obj,ret[1])
                    student_name = input('请输入您{} ： '.format(ret[0]))
                    if ret[0] == '创建课程':
                        price=input('请输入课程的价格：')
                    func(settings_info,student_name,ret[4],price)
                elif hasattr(role_obj,ret[1]) and ret[1] == 'check':
                    func = getattr(role_obj, ret[1])
                    func(settings_info,ret[3])
            else:
                func = getattr(role_obj, ret[1])
                func()