#-*- coding:utf-8 -*-#
student = {'WXZ':95,'Bob':80,'Jeff':85}
print('字典student的值为:{}'.format(student))

#增加元素
student['steff'] = 11
print('增加元素后的student:{}'.format(student))

#查询元素是否存在
print('Th'in student)

print(student.get('WXZ'))

#删除
student.pop('Jeff')
print('删除元素后的student:{}'.format(student))

############################################################
#set使用
#自动过滤重复元素
s = set([1,1,2,2,3,3])
print('set的值为:{}'.format(s))

#增加元素
s.add(4)
print('增加元素后的set为:{}'.format(s))
#删除元素
s.remove(1)
print('删除1后的set为:{}'.format(s))