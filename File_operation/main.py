##文件操作

#打开文件
f1 = open('d:/CODE/python_base/File_operation/test.txt','r')
print(f1)
print(type(f1))

#关闭文件
f1.close()


#打开文件的上限个数
# flist = []
# count = 0
# while True:
#     f = open('d:/CODE/python_base/File_operation/test.txt', 'r')
#     flist.append(f)
#     count += 1
#     print(f'打开文件的个数: {count}')


#写文件
#使用 'w' 一旦打开文件成功, 就会清空文件原有的数据
f2 = open('d:/CODE/python_base/File_operation/test.txt','w')
f2.write('hello\n')
f2.close()
#使用 'a' 实现 "追加写", 此时原有内容不变, 写入的内容会存在于之前文件内容的末尾
f3 = open('d:/CODE/python_base/File_operation/test.txt','a')
f3.write('world')
f3.close()

##读文件
#读文件内容需要使用 'r' 的方式打开文件
f4 = open('d:/CODE/python_base/File_operation/test1.txt', 'r', encoding = 'utf8')
#参数表示 "一次读取几个字符"
result1 = f4.read(2)
print(result1)
f4.close()

#按行读取
f5 = open('d:/CODE/python_base/File_operation/test1.txt', 'r', encoding = 'utf8')
for line in f5:
    print(f'line = {line}',end='')
print('\n')
f5.close()
#使用 readlines 直接把文件整个内容读取出来, 返回一个列表. 每个元素即为一行.
f6 = open('d:/CODE/python_base/File_operation/test1.txt', 'r', encoding = 'utf8')
lines = f6.readlines()
print(lines)
f6.close()

##上下文管理器
#打开文件之后, 是容易忘记关闭的. Python 提供了 上下文管理器 , 来帮助程序猿自动关闭文件.
#使用 with 语句打开文件.
#当 with 内部的代码块执行完毕后, 就会自动调用关闭方法
with open('d:/CODE/python_base/File_operation/test1.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    print(lines)