##顺序语句
#默认情况下, Python 的代码执行顺序是按照从上到下的顺序, 依次执行的
print("1")
print("2")
print("3")

##条件语句
choice = input("输入 1 表示认真学习, 输入 2 表示躺平摆烂: ")
if choice == "1":
    print("你会找到好工作!")
elif choice == "2":
    print("你可能毕业就失业了!")
else:
    print("你的输入有误!")

#缩进和代码块
a = input("请输入第一个整数: ")
b = input("请输入第二个整数: ")
if a == "1":
    if b == "2":
        print("hello")
    print("world")
print("python")

'''联系'''
#1.输入一个整数, 判定是否是奇数
a1 = int(input("请输入一个整数:"))  #必须加int,进行类型转换
if a1 % 2 == 0:
    print("偶数")
else:
    print("奇数")
#2.输入一个整数, 判定是正数还是负数
a2 = int(input("请输入一个整数:"))
if a2 > 0:
    print("正数")
elif a2 < 0:
    print("负数")
else:
    print("0")

# pass表示空语句, 并不会对程序的执行有任何影响, 只是占个位置, 保持Python语法格式符合要求
a3 = int(input("请输入一个整数:"))
if a3 != 1:
    pass
else:
    print("hello")