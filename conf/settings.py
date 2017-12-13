import os
user_info_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db','user_info')
courses_info_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db','courses_info')
classes_info_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db','classes_info')
teachers_info_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db','teachers_info')
students_info_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db','students_info')
db_path =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db','classes')


# admin_user = 'eva'
# admin_pwd = '123456'

if __name__ == '__main__':
      print(user_info_file)
      print(db_path)
#     name_lst = ['宝宝','博博','王浩','赵龙飞','黄旭','海娇','海燕']
#     import hashlib
#     for name in name_lst:
#         md5_obj = hashlib.md5(name.encode('utf-8'))
#         md5_obj.update('123456'.encode('utf-8'))
#         print(name,md5_obj.hexdigest(),'student')