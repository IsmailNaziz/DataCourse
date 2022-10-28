from abstract_entity import Entity

class EmployeeManager(object):

    def run(self):
        pass

class Employee(Entity):

    def __init__(self):
        self.employee_ID = None
        self.pole_ID = None
        self.salary = None
