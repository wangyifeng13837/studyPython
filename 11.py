'''
issubclass案例 检测一个类是否是另一个类的子类
'''


class A():
    pass


class B(A):
    pass


class C():
    pass


print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(B, object))


# isinstance  检查一个对象是否是一个类的实例

class A1():
    pass


a = A1()
print((isinstance(a, A1)))

# hasattr  检测一个对象是否由成员xxx

class A2():
    name ="NoName"

a1= A2()

print(hasattr(a1,"name"))

# help 案例
# 我想知道setattr的具体用法
help(setattr)
