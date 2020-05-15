'''
构造函数的调用顺序 -1
如果子类没有写构造函数，则自动向上查找，直到找到为止

'''

class A():
    def __init__(self):
        print("A")

class B():
    def __init__(self):
        print("B")
'''
class B():
    def __init__(self,name):
        name = 'aa' 
        print("B")
      

 此时，会出现参数结构不对应错误
'''
class C(B):
    print("haha")

# 此时，首先查找C的构造函数,
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到位置

c=C()


class A1():
    def __init__(self):
        print("A1")


class B1():
    def __init__(self,name):
        print(name)
        print("B1")


class C1(B1):
    # C中想扩展B的构造函数
    # 即调用B的构造函数后再添加一些功能
    # 有两种方法实现
    '''
     第一种时通过父类名调用
    def __init__(self,name):
        B1.__init__(self,name)
        print("这是C中附加的功能")
    '''
    # 第二种方法使用super调用

    def __init__(self,name):
        super(C1,self).__init__(name)
        print("这是C中附加的功能")

c = C1("liusha")