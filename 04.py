class Teacher():
    name = 'luban'
    age = 26

    def say(self):
        self.name = 'ximing'
        self.sge = 49
        print("my name is {0}".format(self.name))
        print("my age is {s}".format(s=self.sge))  # format两种用法，效果一样

    def sayAgain():  # 没有使用self参数 用类名来调用
        print(__class__.name)
        print(__class__.age)  # 可以通过__class__访问类的成员，不可以访问say方法内的
        print("Hello,nice to meet you !")


t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()

'''
关于self的案例
'''


class A():
    name = " liuying"
    age = 18

    def __init__(self):  # 构造函数__init__
        self.name = 'wudi'
        self.age = 102

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = " bbbb"
    age = 20

a = A() #此时，系统会默认把a作为第一个参数传入函数
a.say()

#此时，self被a替换
A.say(a)

#同样可以把A作为参数传入
A.say(A)

#此时，传入的时类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

#以上代码，利用了鸭子模型