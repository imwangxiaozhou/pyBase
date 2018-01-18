#-*- coding:utf-8 -*-#

#返回多个值
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return  nx,ny

x,y =move(100,100,60,math.pi/6)
print(x)

#python 默认参数
def power(x,n=2):
    s = 1
    while n > 0:
        n = n -1
        s = s *x
    return s

print(power(5))#使用默认参数
print(power(5,2))
print(power(5,5))

#默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

################################################################
#可变参数
def calculate(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return  sum

print('传入参数1，2，3结果为:{}'.format(calculate(1,2,3)))

nums = [1,2,3]
print('传入一个tuple后的结果为:{}'.format(calculate(*nums)))

##################################################################
#关键字参数
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)

person('michael',30)

person('adam',45,gender='M',job='Engineer')

#检查关键字参数
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name',name,'age',age,'other',kw)

#限制关键字
#只允许city和job作为关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)