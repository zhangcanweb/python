#变量定义  变量名称只能由数字，字母，下划线组成
a=1

#变量分为值类型和引用类型，值类型（int，str，tuple）不可变类型，引用类型（list,set,dict）可变类型
a=1
b=a
a=3
print(b)#1

x=[1,2,3]
y=x
x[0]=25
print(y)#[25,2,3]