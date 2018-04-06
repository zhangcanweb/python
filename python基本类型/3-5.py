#布尔类型 True False(首字母都要大写)
#数字转化为布尔类型用bool()函数
#!!!在数字中除了数字0转化为False其他都为True
print(bool(1))#True
print(bool(-1))#True
print(bool(0))#False


#！！！！！！！！其他数组类型中转布尔类型有值就是True 空值就是False
print(bool('a'))#True
print(bool(''))#False
print(bool([1,2]))#True
print(bool([]))#False
print(bool({1,2}))#True
print(bool({}))#False
#! bool(None)为False