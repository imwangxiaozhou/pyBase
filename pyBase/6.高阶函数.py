#-*- coding:utf-8 -*-#

#1.变量可以指向函数
import math

#将函数赋值给f变量
f=abs

#调用f
print('调用f:{}'.format(f(-100)))


#函数名也是变量

def add(x,y,f):
    return f(x)+f(y)

#map

def f(x):
    return x*x

print('[1,2,3,4,5,6,7]使用map:{}'.format(list(map(f,[1,2,3,4,5,6,7]))))

#reduce

print('reduce实现效果:reuce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2,),x3),x4)')

#filter过滤器
def is_odd(n):
    return n%2 == 1

print('[1,2,3,5,6,9,10,26]过滤掉偶数之后:{}'.format(list(filter(is_odd,[1,2,3,5,6,9,10,26]))))

#sorted排序
sorted([36,4,-34,56,-23],key=abs)