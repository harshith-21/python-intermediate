from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """INTERFACE METHOD"""

p1 = IPerson()
p1.person_method()

#> run this and see error