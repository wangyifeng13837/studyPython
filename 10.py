'''

Mixin案例
'''


class Person():
    name = "liuna"
    age = 18

    def eat(self):
        print("eating ....")

    def drink(self):
        print("drinking ...")

    def sleep(self):
        print("sleep ....")


class Teacher(Person):
    def work(self):
        print("work ....")


class Student(Person):
    def study(self):
        print("study.....")

class Tutor(Teacher,Student):
    pass

t= Tutor()

print(Tutor.__mro__)

print(t.__dict__)

print(Tutor.__dict__)


print("=="*20)

class TeacherMixin():
    def work(self):
        print("working ......")

class StudentMixin():
    def study(self):
        print("studying ......")

class TutorM(Person,TeacherMixin,StudentMixin):
    pass

t1= TutorM()
print(TutorM.__mro__)

print(t1.__dict__)

print(TutorM.__dict__)