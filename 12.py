'''
属性案例

'''

# 创建student类，描述学生
# 学生具有Student.name属性
# 但name格式并不统一
# 可以用增加一个函数，然后自动调用的方法，这个不是很好
import math


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #     如果不想修改代码
        self.setName(name)

    # 介绍一下自己
    def intro(self):
        print("Hi , my name is {0}".format(self.name))

    #  事姓名全部大写
    def setName(self, name):
        self.name = name.upper()


s1 = Student("liu  ying", 19)

s2 = Student("bali yang", 20)

s1.intro()

s2.intro()


# property案例 比上面的更好
# 定义一个Person类，具有name,age属性
# 对于任意输入姓名，我们希望都用大写方式保存
# 年龄，我们希望内部统一用整数保存
# x = property(fget,fset,fdel,doc)

class Person():
    def fget(self):
        return self._name
        return self._age

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name进行操作")


class Person1():
    def fget(self):
        return self._age

    def fset(self, age):
        self._age = int(age)

    def fdel(self):
        self._age = "NoAge"

    age = property(fget, fset, fdel, "对age进行操作")


P = Person()
P.name = "wang"
P1 = Person1()
P1.age = 11.3

print(P.name)
print(P1.age)


# __call__ 举例

class A():
    '''
    __call__魔法方法： 实例被当作函数调用
    '''

    def __init__(self):
        print("构造函数调用")

    def __call__(self):
        print("__call__ 魔法方法调动")

    def __str__(self):
        return  "图灵学院"


a = A()

a()  # 实例当作函数调用，类中必须要有__call__方法函数
print(a) #__str__:当对象被当作字符串的时候调用

#__getattr__举例

class B():
    name ='NoName'
    age = 18
    def __getattr__(self,name):
        print("没有找到")
b = B()
print(b.name)
print(b.aad)  #如果没有getattr方法会报 TypeError

# __setattr__ 案例：
class Person3():
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        # 下面语句会导致问题，死循环
        # self.name = value
        # 此种情况,为了避免死循环,规定统一调用父类魔法函数
        super().__setattr__(name, value)

p3=Person3()
p3.age  ="wangh"