#组之元组
#用()定义
#元素访问
a=(1,2,'hello',True)
b=(3,False)
print(a[1])
print(a[1:3])
print(a+b)
print(a*3)



#！！！！！特例  元组只有一个元素 定义元组的括号会被识别为运算符（）
print(type((1)))#<class 'int'>
print(type(('hello')))#<class 'str'>
print(type((True)))#(class 'bool')
print(type([1]))#<class 'list'>
#表示一个元组   (1,)
print(type((1,)))#<class 'tuple'>
#表示空元组   ()
print(type(()))#<class 'tuple'>
