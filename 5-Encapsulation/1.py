class Person:

    def __init__(self, name, age, gender):

        # __{variable name} means its private
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property # we can use that variable without this @ but this makes it a property
    def Name(self):
        return self.__name
    
    #py does not have method overloading so we have to decorate like this
    @Name.setter
    def Name(self,value):
        if value == "Bob":
            self.__name = "Default name"
        else:
            self.__name = value

    
p1 = Person('mik', 21, 'm')
print("name: ",p1.Name)

p1.Name = "hehe"
print("name: ",p1.Name)

p1.Name = "Bob"
print("name: ",p1.Name)
