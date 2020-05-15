"""
多继承案例

子类可以直接拥有父类的属性和方法，私有属性和方法除外
"""


class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print("I am swimming... ...")


class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("I am flying")


class Person():
    def __init__(self, name):
        self.name = name

    def workd(self):
        print("working")


class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


s = SuperMan("yueyue")
s.swim()
s.fly()
s.workd()


# 菱形继承问题

class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


#构造函数例子

class Person():
    # 对Person 类进行实例化的时候
    # 姓名要确定
    # 年龄要确定
    # 地址要确定
    def __init__(self):
        self.name = "NoName"
        self.age = 18
        self.address = "StudenHome"
        print("In init func")

# 实例化一个人
p= Person()