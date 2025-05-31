##学生管理系统
import sys
def menu():
    print('0.推出程序')
    print('1.新增学生')
    print('2.新增学生')
    print('3.显示所有学生')
    print('4.删除学生')
    choice = input('请输入您的选择:')
    return choice

def insert():
    print("[新增学生] 开始!")
    studentId = input("请输入学生的学号: ")
    name = input("请输入学生的姓名: ")
    gender = input("请输入学生的性别: ")
    if gender not in ('男', '女'):
        print("性别不符合要求! 新增学生失败!")
        return
    className = input("请输入学生的班级: ")
    # 使用一个字典表示学生信息
    student = {
        'studentId': studentId,
        'name': name,
        'gender': gender,
        'className': className
    }
    # 把字典添加到学生列表中
    global students
    students.append(student)
    print("[新增学生] 完毕!")

def show():
    print("[显示学生] 开始!")
    for s in students:
        print(f"[ {s['studentId']}]\t {s['name']}\t {s['gender']}\t {s['className']}")
        print(f"[显示学生] 完毕! 共显示了 {len(students)} 条记录!")
def find():
    print("[查找学生] 开始!")
    name = input("请输入要查找的同学姓名: ")
    count = 0
    for s in students:
        if name == s['name']:
            print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
        count += 1
        print(f"[查找学生] 完毕! 共查找到 {count} 条记录!")
def delete():
    print("[删除学生] 开始!")
    studentId = input("请输入要删除的同学学号: ")
    count = 0
    for s in students:
        if studentId == s['studentId']:
            print(f"删除 {s['name']} 同学的信息!")
    students.remove(s)
    count += 1
    print(f"[删除学生] 完毕! 共删除 {count} 条记录!")

# 使用列表表示所有的学生
students = []
def main():
    print('+--------------------------+')
    print('| 欢迎来带学生管理系统! |')
    print('+--------------------------+')
while True:
    choice = menu()
    if choice == '0':
        #退出程序
        sys.exit(0)
    elif choice == '1':
        #新增学生
        insert()
    elif choice == '2':
        #显示所有学生
        show()
    elif choice == '3':
        #查找学生
        find()
    elif choice == '4':
        #删除学生
        delete()
    else:
        print('您的输入有误! 请重新输入!')
main()