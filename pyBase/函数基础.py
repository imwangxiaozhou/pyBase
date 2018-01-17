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