#-*- coding:utf-8 -*-#

#常见输入
str = input("请输入:")
print("你输入的内容是:%s"%str)

#常见格式化输出
#1(旧式操作)
print("his name is %s"%("Bob"))
#%s 字符串  %d 整数  %f  浮点数


#2
print('{} name is {}.'.format('his','Bob'))

#3数字格式化
num1 = 123.12
num2 = 123.123
num3 = 123
print('{:.3f},{:.3f},{:.3f}'.format(num1,num2,num3))