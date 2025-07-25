
import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return f"animal:{self.name}:{self.age}"

class Cat(Animal):
    def speak(self):
        return "meow"

    def __str__(self):
        return f"cat:{self.name}:{self.age}"

class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def speak(self):
        return "hello"

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def age_diff(self, other):
        return abs(self.age - other.age)

    def __str__(self):
        return f"person:{self.name}:{self.age}"

class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            return "i have homework"
        elif r < 0.5:
            return "i need sleep"
        elif r < 0.75:
            return "i should eat"
        else:
            return "i am watching tv"

    def __str__(self):
        return f"student:{self.name}:{self.age}:{self.major}"



class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        p1s = self.parent1.rid if self.parent1 else None
        p2s = self.parent2.rid if self.parent2 else None
        p1o = other.parent1.rid if other.parent1 else None
        p2o = other.parent2.rid if other.parent2 else None
        return ({p1s, p2s} == {p1o, p2o})

    def __str__(self):
        return "rabbit:" + self.get_rid()
