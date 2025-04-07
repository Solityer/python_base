#注释的使用

# 这是一行注释.
"""
这是文档字符串
这是文档字符串
"""

#输出到控制台
a = 10
print(a)
#希望打印出"a=10"这样的内容
print(f"a = {a}") #格式化字符串f-string, 此处f代表format
#把数字和字符串混在一起
print(f"a = {a + 10}")

#从控制台输入
num = input("请输入一个整数:")
print(type(num))  #input的返回值是string类型
print(f'您输入的数字是{num}')
#如果对输入的数据进行算术运算
a1 = input("请输入第一个整数:")
a2 = input("请输入第二个整数:")
print(f'a1 + a2 = {a1 + a2}')  #拼接
a1 = int(a1)  #输入的变量进行类型转换
a2 = int(a2)
print(f'a1 + a2 = {a1 + a2}')

##输入四个整数,求四个小数的平均值
b = input("请输入第一个整数:")
c = input("请输入第二个整数:")
d = input("请输入第三个整数:")
e = input("请输入第四个整数:")
b = float(b)
c = float(c)
d = float(d)
e = float(e)
avg = (b + c + d + e) / 4
print(f'平均值是{avg}')