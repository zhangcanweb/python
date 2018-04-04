a=100
if a<100:
	print('good')
else:
    print('bad');
a=2
b=3
print(a)
print(b)
print(10//3)
print(10/3)
if 1==2:print('one equals two')
if 1==1:print('one equale one')
# 乘方运算函数pow()
print(pow(2,3))
#int()函数将字符串转化成数字  input()函数运行时还要手动赋值一次
# a=input()
# b=input()
# print(int(a)*int(b))
# print(a)
#字符串和数字只能相乘不能加减除
x='10'
y=2
print(x*y)#1010
#abs()计算绝对值 round()四舍五入
print(abs(-10))#10
print(round(3.64))#4
#math.floor()去除小数点(外部引入math模块)
import math
print(math.floor(32.1))
#math.ceil()只要有小数点就进一位
print(math.ceil(32.1))
print(math.ceil(32.6))
#math.sqrt()可以（import math）也可以（from math import sqrt）
from math import sqrt
print(sqrt(3))
#海龟绘图
from turtle import *
forward(100)
left(120)
forward(100)
left(120)
forward(100)
