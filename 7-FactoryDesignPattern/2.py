from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """INTERFACE METHOD"""

# p1 = IPerson()
# p1.person_method()

#> run this and see error

class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("iam a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher name"

    def person_method(self):
        print("iam a teacher")



# p1 = Student()
# p1.person_method()

# p2 = Teacher()
# p2.person_method()


#> you can directly: if else statemnt to build one or other but thats not facory parttwren


#this is the intended way
class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("invalid type")
        return -1
    
if __name__ == "__main__":
    choice = input("Choose a type of person: ")
    person = PersonFactory.build_person(choice)
    if person :
        person.person_method()


