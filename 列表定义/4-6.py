#字典定义{key:value}（和json很像）
a={'name':'zhangcan','age':21,'sex':True}
print(type(a))#<class 'dict'>
#访问元素
print(a['name'])#'zhangcan'
#!dict中不能有重复的key
#value的类型str int float list set dict key类型不能是可变的值（list类型) 

#定义空dict
b={}