class Person():
    # name 是公有的成员
    name = " liu mang"
    # __age就是私有成员
    __age = 19

p =Person()

# name是公有变量
print(p.name)

# __age是私有变量
# 注意报错信息
# print(p.__age)

#name mangling 技术
print(Person.__dict__)
print(p._Person_age)

#Python的私有不是真私有，是一种成为name mangling的改名策略可以使用对象._classname_attributename访问


