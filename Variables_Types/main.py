#变量和类型

avg = (67.5 + 89.0 + 12.9 + 32.2) / 4
# ** 在 Python 中表示乘方运算. ** 2 即为求平方.
total = (67.5 - avg) ** 2 + (89.0 - avg) ** 2 + (12.9 - avg) ** 2 + (32.2 - avg) ** 2
result = total / 3
print(result)

#使用变量#
first = 10
end = first
print(end)
first = 20
print(first)

#变量类型#
a = 10
print(type(a))
b = 0.5
print(type(b))
c = 'solity'
print(type(c))
d = "solity"
print(type(d))
e = 'my name is "solity"'
print(type(e))
f = '''my 'name' is "solity"'''
print(type(f))
print(f)

print(len(f))

#字符串拼接
a1 = 'hello'
a2 = 'world'
print(a1 + a2)

b1 = True
b2 = False
print(type(b1))
print(type(b2))

#动态类型
c1:int = 10  #冒号后面对变量进行类型申明,但变量类型在后面依然会随着语法赋值进行改变
print(type(c1))
c2:float = 0.5
print(type(c2))