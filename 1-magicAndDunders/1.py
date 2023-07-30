class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object " + self.name + " is being distroyted")

p = Person("harshi", 21)



