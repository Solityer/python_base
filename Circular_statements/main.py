##循环语句

#while循环
num = 1
while num <= 10:
    print(num)
    num += 1
#1.计算1到100的和
result1 = 0
sum1 = 1
while sum1 <= 100:
    result1 += sum1
    sum1 += 1
print(result1)
#2.计算5的阶乘
result2 = 1
sum2 = 1
while sum2 <= 5:
    result2 *= sum2
    sum2 += 1
print(result2)
#3.求 1! + 2! + 3! + 4! + 5!
result3 = 0  #最终结果
sum3 = 1
while sum3 <= 5:
    pos = 1
    num3 = 1
    while pos <= sum3:
        num3 *= pos
        pos += 1
    result3 += num3
    sum3 += 1
print(result3)


#for循环
'''
for 循环变量 in 可迭代对象:
    循环体
可迭代对象: 特殊的变量,内部包含了许多其他的值
'''
#1.打印1到10
for i in range(1, 11):
    #range是一个内置函数:range(begin,end)==>>【begin,end） 前闭后开
    print(i)
#2.打印 2, 4, 6, 8, 10
for i in range(2,12,2):
    #range第三个参数: 表示"步长",默认值为1
    print(i)
#3.反向打印输出
for i in range(10,0,-1):
    #range第三个参数: 表示"步长",默认值为1
    #使用shift+F6可以针对变量进行重命名,会智能的分析代码,自动把所有需要修改的名字统一替换掉
    print(i)


#continue 表示结束这次循环, 进入下次循环
#模拟吃包子. 吃第3个包子的时候吃出了一只虫
for i in range(1, 6):
    if i == 3:
        continue
    print(f"吃完第 {i} 个包子")

#break
#输入若干个数字, 求平均值. 使用 "分号" 作为结尾.(不知道有多少个数字)
thesum = 0 #加和的结果
count = 0 #表示有几个数字
while True:
    num = input("请输入一个数字(分号表示输入结束):")
    if num == ';':
        break;
    num = float(num)
    thesum += num
    count += 1
print(f'平均值为:{thesum}')