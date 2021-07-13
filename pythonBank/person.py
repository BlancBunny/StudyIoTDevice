class Person:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

class Man(Person):
    gender = 'male'

class Korean(Person):
    nationality = 'Korea'

class KoreanMan(Man, Korean): # 다중 상속
    pass


