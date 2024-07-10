
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("I am Cat. My name is ", self.name , ".I am ", self.age ,"years old")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
          print("I am Dog. My name is ", self.name , ".I am ", self.age ,"years old")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Dodo", 2.5)
dog1 = Dog("Tyson", 8)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()

