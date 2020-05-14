
'''
定义一个学生类，用来形容学生

'''

# 定义一个空的类

class Studens():
    # 一个空类，pass代表直接跳过
    # 次相互pass必须有
    pass

# 定义一个对象
mingyue = Studens()

# 再定义一个类，用来描述学习python的学生

class PythonStudents():

    # 用None给不确定的值赋值
    name = None
    age = 18
    course ='Python'

    # 用函数表示动作或功能
    # 需要注意
    # 1.def doHomeworkde 缩进层级
    # 2.
    def doHomework(self):
        print("do Homework")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudents()

print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进参数
yueyue.doHomework()
print("happy11")