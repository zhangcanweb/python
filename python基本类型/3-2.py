#数字 int(整数) float(浮点数)
#混合计算 整数混合运算(+.-.*./)浮点数都是浮点数（特殊的是除法整数除整数是浮点数）
print(type(1+1))#int
print(type(1+1.0))#<class 'float'>
print(type(1+1.1))#<class 'float'>
print(type(1-1))#int
print(type(1-1.0))#<class 'float'>
print(type(1-1.1))#<class 'float'>
print(type(1*1))#int
print(type(1*1.0))#<class 'float'>
print(type(1*1.1))#<class 'float'>
print(type(1/1))#<class 'float'>
print(type(1/1.0))#<class 'float'>
print(type(1/1.1))#<class 'float'>

#特殊
print(type(1//1))#<class 'int'>  结果是1
print(1/2)#除法
print(1//2)#整除保留整数部分所以（//）类型是int
