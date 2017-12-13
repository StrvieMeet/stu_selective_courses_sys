# li=[11,17,1,2,3,4,5,6,7,8,9]   #去除掉列表中的奇数
#
#
#
#
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)


li = [{'cname': 's8', 'name': 'alex13', 'id': 1},
 {'cname': 's6', 'name': 'alex13', 'id': 1},
 {'cname': 's4', 'name': 'alex13', 'id': 1},
 {'cname': 's4', 'name': 'egon2', 'id': 2},
 {'cname': 's6', 'name': 'egon2', 'id': 2},
 {'cname': 's6', 'name': 'jing', 'id': 33}]

ret = {}
for teacher in li:
    name = teacher["name"]
    if name not in ret:
        ret[name] = teacher  # alex：{'id': 1, 'name': 'alex13', 'cname': 's8'}
        ret[name]["class_list"] = [
            teacher["cname"]]  # alex：{'id': 1, 'name': 'alex13', 'cname': 's8','class_list':['s8']}
    else:
        ret[name]["class_list"].append(teacher["cname"])

print(ret)

        # def check_login(func):
#
#     def inner(*args,**kwargs):
#
#         ret = func(*args,**kwargs)
#
#         return ret
#
#     return inner
# @check_login     #f = check_login(f)
# def f():
#     return 123
#
# f()