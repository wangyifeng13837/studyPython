class A():
    name = "a ha"
    age = 18
'''
此案例说明
类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下指向同一个变量
'''
# 此时，A称为类实例
print(A.name)
print(A.age)

print('*'*20)

# id可以鉴别一个变量是否和另一个变量是同一个变量
print(id(A.name))
print(id(A.age))

print('*'*20)

a = A()
print(a.name)
print(a.age)

print('*'*20)
print(id(a.name))
print(id(a.age))
# 以上的name和age指向同一个地址
print('*'*20)
# 通过赋值改变了id值
a.name = 'wangyifeng'
a.age = 31
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print('*'*20)

# 查看A内的所有属性
print(A.__dict__)
b = A() #实例化未赋值时与类的实例时指向同一个地址 等同于a实例未被赋值时
print(b.__dict__)
print(a.__dict__)




