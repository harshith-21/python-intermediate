import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + self.y)
        
    # def __sub__():
    # def __mul__():
    # def __div__():

    # def __str__(): # also does the same job
    def __repr__(self):
        return f"Vector is ({self.x},{self.y})"
    
    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __call__(self):
        print("hello, i was called")

v1 = Vector(10, 20)
v2 = Vector(20, 30)

v3 = v1 + v2

print("Vector3 is (", v3.x, v3.y, ")" )

print(v3)

# print(int(len(v3)))

# __call__
v3()