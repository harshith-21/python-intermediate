from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """implement in child class"""
    
    @abstractstaticmethod
    def print_department():
        """implement in child class"""

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accouting Department: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Deparment: {self.employees}")

class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("parent department")
        print(f"Parent Deparment base employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")

dept1 = Accounting(200)
dept2 = Development(170)

Parent_dept = ParentDepartment(30)
Parent_dept.add(dept1)
Parent_dept.add(dept2)

Parent_dept.print_department()
    