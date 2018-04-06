#字符串运算
#字符串拼接(+)
print('hello,'+'world')
#乘法运算（*）
print('hello'*2)#hellohello
#字符串索引从0开始，负数从右开始查找
print('hello world'[2])#'l'
print('hello world'[-3])#'r'
#截取字符串 str[起始索引:截取终点索引+1]
print('hello world'[0:3])#hel
print('hello world'[0:-2])#hello wor

#！！！！！！！！截取world  [起始索引：空]表示从起始索引值截取去尾部
print('hello world'[6:11])
print('hello world'[6:])


#总结 str[a:b]
#a为空则a此时代表索引0 b为空则代表截取到尾部