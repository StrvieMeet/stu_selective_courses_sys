import os
import pickle
class Mypickle:
    '''
    定义一个序列化的类
    '''
    @staticmethod
    def load(path):
        '''
        :param path:
        :return:
        '''

        if os.path.getsize(path):
            # 判断文件的大小
            with open(path, 'rb') as f:
                # 按照文件的路径打开文件读取数据
                for imter in f:
                    ret = pickle.load(imter)
                # 统一对文件进行转换
        else:
            # 否则就返回一个空字典
            ret = {}
        return ret

    @staticmethod
    def dump(obj,path):
        # 文件写入
        with open(path,'wb+') as f:
            # 按照文件的路径打开文件写数据
            ret = pickle.dumps(obj)
            # 写入数据
            f.write(ret)
