#类
##创建Dog类
class Dog:
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        self.color = "red"  #给属性指定默认值

    def update_color(self, new_color):
        my_dog.color = new_color
    def read_color(self):
        print("My dog's color is " + self.color + ".")

    def increment_age(self, age):
        """将年龄数增加指定的年份"""
        my_dog.age += age
    def read_age(self):
        print("My dog is " + str(my_dog.age) + " years old.")

my_dog = Dog('solity', 6)
print("My dog's name is " + my_dog.name.title() + ".")
my_dog.read_age()
my_dog.read_color()

##创建多个实例
your_dog = Dog('lucy', 3)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")

#修改属性的值 三种方法
#1.直接修改属性的值
my_dog = Dog('john', 6)
# my_dog.color = "yellow"  #通过实例直接访问
# my_dog.read_color()
#2.通过方法修改属性的值
'''def update_color(self,new_color):
    my_dog.color = new_color
    #将该函数写入到类中'''
my_dog.update_color("blue")
my_dog.read_color()
#3.通过方法对属性的值进行递增
my_dog.increment_age(1)
my_dog.read_age()

##继承
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):  #制造商 型号 生产年份
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  #汽车的里程

    def get_descriptive_name(self):  #指出我们拥有的是一辆什么样的车
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):  #读取汽车的里程表
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  #增加里程数
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car has a gas tank!")

class battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        #电动车没有油箱
        '''重写父类的方法，在子类中重新将父类中的某个函数重写即可'''
        print("This car doesn't need a gas tank!")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性,在初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = battery()

##导入类
import car
your_tesla = car.Car('tesla', 'model s', 2016)
my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
your_tesla.fill_gas_tank()
my_tesla.battery.fill_gas_tank()


##标准库的初使用
from random import randint
print(randint(1,6))  #将两个整数作为参数，随机返回一个位于这两个整数之间(含)的整数

from random import choice
player = ['charles','martina','michael','florence','eli']
print(choice(player))