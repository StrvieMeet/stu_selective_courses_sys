import os
import sys
'''
项目的启动接口
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取当前的文件然后找到当前文件的父目录的父目录
sys.path.append(BASE_DIR)
# 将找到的父目录文件添加到环境变中

from core import main
# 从主逻辑目中找到main文件然后导入

if __name__ == '__main__':
    main.start()
    # 找到文件导入的文件中的start函数加括号调用