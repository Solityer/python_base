##函数

#定义一个求和函数
def clacSum(begin,end):
    thesum = 0
    for i in range(begin,end+1):
        thesum += i
    print(thesum)
#调用函数
#求1-100的和
clacSum(1,100)
#求300-400的和
clacSum(300,400)

#如果只是定义,而不去调用,则函数体内的代码并不会执行
def test():
    print('hello')
    print('hello')
    print('hello')
test() #调用

#函数的参数
def add(a,b):
    return a + b
print(add(10,20))
print(add(1.5,2.5))
print(add('Hello','World'))


#函数的返回值
def clacSum1(begin,end):
    thesum1 = 0
    for i in range(begin,end+1):
        thesum1 += i
    return thesum1
result = clacSum1(1,100)
print(result)

def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True
print(isOdd(19))  #函数的链式调用
print(isOdd(add(1,2)))

#写一个返回平面上的点
def getPoint():
    x = 10
    y = 20
    return x,y
a1,b1 = getPoint() #把x赋值给a,把y赋值给b
print(a1,b1)
_,b2 = getPoint() #虽然返回了多个函数值,但只想要其中一部分的值,可以用‘_’来进行占位

#变量的作用域
x1 = 10
def test1():
    x = 20
    print(f'函数内部{x}')
test1()
print(f'函数外部{x1}')

def test2():
    print(f'x = {x1}')  #函数内部没有x变量,会尝试读取全局变量(上一级作用域)

#使用函数将全局变量x1修改为20
print(f'未修改前,全局变量x1={x1}')
def test3():
    global x1  #gloabl让函数里面知道x1是全局变量
    x1 = 20
test3()
print(f'修改后,全局变量x1={x1}')
#只有函数才会影响作用域

#函数的嵌套调用
def a():
    num1 = 10
    print("函数 a")
def b():
    num2 = 20
    print("函数 b")
    a()
def c():
    num3 = 30
    print("函数 c")
    b()
def d():
    num4 = 40
    print("函数 d")
    c()
d()

#函数的递归
def factor(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factor(num - 1)
print(factor(5))

#函数形参的默认值
def add1(x, y, debug = False):  #False为形参的默认值
    if debug:
        print(f'x={x},y={y}')
    return x + y
result = add1(10,20)
print(result)
print(add1(10,20,True))

#函数的关键字参数
def test1(x,y):
    print(f'x = {x}')
    print(f'y = {y}')
test1(10,20)
test1(y = 10, x = 20)