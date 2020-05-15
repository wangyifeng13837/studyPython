'''
构造函数概念
'''


class Dog():
    # __init 就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作就是进行初始化，所以得名
    def __init__(self):
        print(" I am init in dog")


# 实例化的时候，括号内的参数需要跟构造函数参数匹配
kaka = Dog()


# 继承中的构造函数

class Anmial():
    def __init__(self):
        print(" Animal")


class PaXingAni(Anmial):
    def __init__(self):
        print(" paXing DonWu ")


class Dog1(PaXingAni):
    def __init__(self):
        print(" I am init in dog")


# 实例化的时候，自动化调用了Dog1的构造函数
# 因为找到了构造函数，则不在查找父类的构造函数
kaka = Dog1()


# 猫没有写构造函数
class Cat(PaXingAni):
    pass


# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
# 在PaXingAni中查找到了构造函数，则停止向上查找
anni = Cat()


print("=="*20)


# 继承中的构造函数-2

class Anmial1():
    def __init__(self):
        print(" Animal")


class PaXingAni1(Anmial1):
    def __init__(self,name):
        print(" paXing DonWu {0}".format(name))


class Dog2(PaXingAni1):
    def __init__(self):
        print(" I am init in dog")

class Cat1(PaXingAni1):
    pass
#实例化Dog2时，查找到Dog2的构造函数，参数匹配，不报错
d=Dog2()


# 此时，由于Cat2没有构造函数，则向上查找
#因为PaXingAni1的构造函数需要2个参数，实例化时候给了一个会报错
c= Cat1()


