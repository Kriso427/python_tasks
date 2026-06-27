class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says: Woof!")

dog_name=input("What is your dogs name?")
my_dog = Dog(dog_name)
my_dog.bark()
