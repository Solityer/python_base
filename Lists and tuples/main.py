##列表和元组

#用一个变量表示很多个数据
#列表是可变的:创建好了之后,随时能改
#元组是不可变的:创建好了之后改不了,要是想改，只能丢弃旧的,搞个新的

#创建列表
#1.直接使用字面值来创建
#[]就表示一个空的列表
a = []
print(type(a))
#2.使用list()来创建
b = list()
print(type(b))
#3.可以在创建列表的时候,在[]中指定列表的初始值，元素之间使用 , 分割
c = [1,2,3,4]
print(c)
d = [1, 'hello', True, [4,5,6]]
print(d)
print(d[2]) #下标方式访问列表元素，从0开始计算
d[2] = False #使用下标修改列表元素
print(d)
print(len(d))  #len函数获取列表长度
print(d[-1])  #下标可以写成负数,-1表示倒数第1个


##列表的切片操作
e = [1,2,3,4,5,6,7,8,9]

#使用 [ : ] 的方式进行切片操作
print(e[1:4])  #取到下标1到下标4的元素(包含下标1的元素,不包含下标4的元素)
print(e[2:]) # 省略后边界, 表示获取到列表末尾
print(e[:-1])  # 省略前边界, 表示从列表开头获取
print(e[:])  # 省略两个边界, 表示获取到整个列表.

#还可以指定 "步长" , 也就是 "每访问一个元素后, 下标自增几步
print(e[::1])
print(e[::2])
print(e[::3])
print(e[::5])

#指定的步长还可以是负数, 此时是从后往前进行取元素. 表示 "每访问一个元素之后, 下标自减几步
print(e[::-1])
print(e[::-2])
print(e[::-3])
print(e[::-5])

##遍历列表元素
alist = [1, 2, 3, 4]
#最简单的办法就是使用 for 循环
print(f'////////')
for elem in alist:  #elem代表了列表里的每一个元素
    print(elem)
#也可以使用 for 按照范围生成下标, 按下标访问
print(f'////////')
for i in range(0,len(alist)):
    print(alist[i])
#还可以使用 while 循环. 手动控制下标的变化
print(f'////////')
i = 0
while i < len(alist):
    print(alist[i])
    i += 1

##列表的插入操作

#新增元素
#使用 append 方法, 向列表末尾插入一个元素(尾插)
list1 = [1,2,3,4,5]
list1.append(6)
list1.append('hello')
print(list1)
#使用 insert 方法, 向任意位置插入一个元素
list2 = [1,2,3,4,5]
list2.insert(0, 'hello')  #在0号位前面加上hello
print(list2)

#查找元素
#使用 in 操作符, 判定元素是否在列表中存在. 返回值是布尔类型.
list3 = [1, 2, 3, 4]
print(2 in list3)
print(10 in list3)
#使用 index 方法, 查找元素在列表中的下标. 返回值是一个整数. 如果元素不存在, 则会抛出异常.
list4 = [1, 2, 3, 4]
print(list4.index(2))
#print(list4.index(10)) #没有元素10,抛异常

#删除元素
#使用 pop 方法删除最末尾元素
list5 = [1, 2, 3, 4]
list5.pop()
print(list5)
# #pop也能按照下标来删除元素
list6 = [1, 2, 3, 4]
list6.pop(2)
print(list6)
#使用 remove 方法, 按照值删除元素
list7 = [1, 2, 3, 4]
list7.remove(2)
print(list7)

##连接列表
#使用 + 能够把两个列表拼接在一起(此处的 + 结果会生成一个新的列表. 而不会影响到旧列表的内容)
list8 = [1, 2, 3, 4]
list9 = [5, 6, 7]
print(list8 + list9)
#使用 extend 方法, 相当于把一个列表拼接到另一个列表的后面
#a.extend(b),是把b中的内容拼接到a的末尾. 不会修改b, 但是会修改a
list10 = [1, 2, 3, 4]
list11 = [5, 6, 7]
list10.extend(list11)
print(list10)
print(list11)


##元组
#创建元组
a1 = ()
print(type(a1))
b1 = tuple()
print(type(b1))
#创建元组时,可以指定初始值
c1 = (1,2,3,4)
print(c1)

#当进行多元赋值的时候,其本质上是按照元组的方式来进行的
def getpoint():
    x = 10
    y = 20
    return x,y
x,y = getpoint()