#集合
#定义集合用{}
#集合没有序列号
#集合中没有重复元素
#集合可以用len()函数
#集合可以用 in 和 not in 逻辑运算符
a={1,2,3}
b={2,3,4,5}
print(type(a))#<class 'set'>
print(len(a))#  3
print(1 in a)# True
#求差集 -
print(a-b)#{1}
#求交集 &
print(a&b)#{2,3}
#求合集 |
print(a|b)#{1,2,3,4,5}
#定义空集合
set()
c=set()
print(type(c))#<class 'set'>