##代码案例1: 日期计算器

import datetime
date1 = datetime.datetime(year=2012, month=2, day=14)
date2 = datetime.datetime(year=2022, month=7, day=12)
print(date2 - date1)


##代码案例2: 单词逆序
def reverseWords(s:str):
    tokens = s.split()  #按照空格将字符串s切分成若干份
    tokens.reverse()  #逆序
    return ' '.join(tokens)
print(reverseWords('I am a student.'))


##代码案例3: 旋转字符串
#题目: 给定两个字符串,s和goal。如果在若干次旋转操作之后，s能变成goal，那么返回true。
# s的旋转操作就是将s最左边的字符移动到最右边.例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea'
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s+s)  #goal是否在s+s拼接的字符串里面
print(rotateString('abcde', 'cdeab'))



##代码案例4: 统计字符串前缀的字符串数目
def countPrefixes(words:list, s:str):
    res = 0  #符合要求字符串个数
    for word in words:
        if s.startswith(word):
            res += 1
    return res
print(countPrefixes(["a","b","c","ab","bc","abc"], "abc"))


##代码示例5: 文件查找工具
#指定一个待搜索路径, 同时指定一个待搜索的关键字.在待搜索路径中查找是否文件名中包含这个关键字.
#使用 os.walk 即可实现目录的递归遍历.
#os.walk 返回一个三元组, 分别是 当前路径,  当前路径下包含的目录名(多个), 当前路径下包含的文件名(多个)
import os
inputPath = input('请输入待搜索路径: ')
pattern = input('请输入待搜索关键词: ')
for dirpath, dirnames, filenames in os.walk(inputPath):
    for f in filenames:
        if pattern in f:
            print(f'{dirpath}/{f}')


##二维码生气器(qrcode)
import qrcode
img = qrcode.make('孤月月真帅')
img.save('qrocde.png')


##操作excel
import xlrd
#1.打开xlsx文件
xlsx = xlrd.open_workbook('D:/CODE/python_base/Code_samples/test.xlsx')
#2.获取到指定的标签页
table = xlsx.sheet_by_index(0)
#3.获取到表格中的行数
nrows = table.nrows
print(f'nrows = {nrows}')
#4.进行循环统计操作
count = 0
total = 0
for i in range(1, nrows):
    #拿到当前的班级id
    classId = table.cell_value(i, 1) #第i+1行第2列
    if classId == 101:
        total += table.cell_value(i, 2)
        count += 1
print(f'平均分: {total / count}')