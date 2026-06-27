class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says: Woof!")

my_dog = Dog("Rex")
my_dog.bark()