class Student():
    name = 'dashi'
    age = 25

    #注意say的写法，参数有一个self

    def say(self):
        self.name = 'yixiu'
        self.sge = 10
        print("my name is {0}".format(self.name)) #format 其实就是format()后面的内容，填入大括号中（可以按位置，或者按变量）
        print(id(self.name))
        print("my age is {0}".format(self.sge))

    def sayAgai(s): #self 并不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名代替

        print("my name is {0}".format(s.name))
        print(id(s.name))
        print("my age is {0}".format(s.sge))

dayi = Student()
dayi.say()
dayi.sayAgai()