#记住大分类（框架记住，遇到就查，慢慢就记住了）：
#1.算数运算符：+  -  *   /   //  （整除） % （余数）   2**5（2的5次方）
#2.赋值运算符 =   +=  -=    *=  /=   %=   **=   //=
#3.关系运算符 ==   !=   >   <   >=   <=
#4.逻辑运算符 and , or , not
#5.成员运算符 in , not in
#6.身份运算符 is ,  is not
#7.位运算符  &  |  ^  ~  <<  >>

#关系运算符比较数字之间正常比较   字符串之间转化成ascll码比较
'a'>'b'#False
'abc'>'abd'#False   字符串含有多个元素时从第一个元素开始逐一比较
[1,2,3]<[2,3,4]#比较规则和字符串相同

#逻辑运算符操纵bool类型
True and True #True
False or True #True
not True#False

#int float 只要不是0 都表示True
not 0.1 #False  
#str不是空就是True
#str1 and str2#str1和str2都为True 返回str2   当其中一个为False 就返回那一个
#str1 or str2#谁为True返回谁 当都为True 返回第一个 都为False 返回第二个
#list不是空就是True


#成员运算符 在dict中运用是 是判断 变量是否是dict中的key值


#身份运算符实际比较的是变量内存地址
1 is 1.0 #False
1==1.0 #True
{1,2,3} is {2,1,3}#False
{1,2,3}=={2,1,3}#True 无序列表 内容与顺序无关
(1,2,3)is (2,1,3)#WFalse
(1,2,3)==(2,1,3)#False



# == 判断变量值是否相等，
# is 判断变量身份（内存id ord()函数）是否相等， 
# isinstance 判断变量类型是否相等
a='hello'
print(isinstance(a,str))#True
isinstance(a,(str,int,list))#True
isinstance(a,(int,list))#False

#位运算符 & 按位与
#| 按位或
#^ 按位异或
#~ 按位取反
#<< 左移动
#>> 右移动
#把数字当做二进制进行计算