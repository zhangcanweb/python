#组也叫做序列包括 str list tuple 

#索引叫做序列号
a=[1,2,3]
print(a[0])

#序列截取 叫做序列切片
a[1:2]

# in 序列逻辑运算符
print(1 in a)#True
# not in 序列逻辑运算符
print(4 not in a)#True

#测量序列长度函数 len()
print(len(a))# 3

#求序列最大值函数max()和序列最小值函数min()
print(max([1,22]))# 22
print(min([1,2,33]))# 1
#print(max([1,2,'hello']))#  TypeError: '>' not supported between instances of 'str' and 'int'
print(max('hello world'))#  w
print(min('hello world'))#  ''
print(min('helloworld')) # d
print(max('hello world123'))# w
print(min('hello world123'))# ''
print(max('helloworld123'))#  w
print(min('helloworld123')) # 1

#字母比较实质 是字母scell码比较
print(ord('w'))#119
print(ord(' '))#32