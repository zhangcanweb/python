# 列表和元组都属于序列（列表可以修改，元组不可以）
# 一个序列可以包含另一个序列
one=['jack',22]
two=['rose',20]
people=[one,two]
print(people)
# 1.通用序列操作（索引）受用负数时从右找寻元素，-1代表最后一个元素、
greeting='hello'
print(greeting[0])#'h'
print(greeting[-1])#'o'
