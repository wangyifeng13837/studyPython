'''
继承的语法
在python中，任何类都有一个共同的父类叫object
'''


class Person():
    name = "NoName"
    age = 0
    __scorce = 0  # 考试成绩是秘密，只要自己知道
    _petname = "sec"  # 小名，是保护的，子类可以用但是不能公用

    def sleep(self):
        print("Sleeping ... ...")

    def work(self):
        print("make some money")


class Teacher(Person):
    teacher_id= "9527"
    name ="DaNa"  #子类中定义的成员和父类如果相同，则优先使用子类成员
    def make_test(self):
       print("testing")
    # 子类扩充父类功能案例
    # 人有工作的函数，老师也有工作的函数，但老师的工作是讲课
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        Person.work(self) # 可以使用 父类名.父类成员 的格式来调用父类成员
        super().work()  # 使用super().父类成员的格式来调用
        # 以上两种方法功能相同
        self.make_test()
        print(" I need to study")

t = Teacher()
print(t.name)
# 可以访问受保护的，不可以访问私有的
print(t._petname)
print("*"*20)
t.work()
