import time

#클래스 객체
number = [10, 20, 30]
# print(dir(number))

class Person(object):
    total = 0

    def __init__(self, name, age): # 생성자 오버로딩
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

p = Person('Kim', 27)
print(p.name, p.age)
print(p.getAge())
print(p.total)

