#-*- coding:utf-8 -*-#

#list使用
classmates = ['wxz','bob','Tracy']

print("classmates的第一个元素为:{},长度为:{}".format(classmates[0],len(classmates)))

#装逼专用
print("classmates的第一个元素为:{},长度为:{}".format(classmates[-3],len(classmates)) )

#插入
classmates.insert(1,"hello")
print("插入后的classmates:{}".format(classmates))

#追加
classmates.append("林枫")
print("追加后的classmates:{}".format(classmates))

#删除
classmates.pop(1)
print('删除索引为1的元素后的classmates:{}'.format(classmates))

#替换元素
classmates[1] = 'new hello'
print('替换元素后的classmates:{}'.format(classmates))

#################################################################

#tuple的使用
#一旦初始化就不能修改，比list更加安全
t =  (1,2,3,4,5)

#可变tuple（其中加入list）
changedT = ('a','b',['A','B'])
print('未修改changedT:{}'.format(changedT))
changedT[2][0] = 'X'
changedT[2][1] = 'Y'
print('修改后的changedT:{}'.format(changedT))