from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):

    @property
    @abstractmethod
    def firstName(self):
        pass

    @property
    @abstractmethod
    def secondName(self):
        pass

    @property
    @abstractmethod
    def salary(self):
        pass
    
    @property
    def base_salary(self):
        pass
    
    @property
    @abstractmethod
    def experience(self):
        pass

    @abstractmethod
    def updateSalary(self):
        pass

    def __str__(self):
        return f"{self.firstName} {self.secondName}, manager:{managers.secondName},\
experience:{self.experience}"
    

    

class Developer(Employee):
    def __init__(self, firstName, secondName, salary, experience, managers):
        self.firstName = firstName
        self.secondName = secondName
        self.salary = salary
        self.base_salary = salary
        self.experience = experience
        self.managers = managers
    def updateSalary(self):
        if (self.experience > 2):
            self.salary += 200
        if (self.experience > 5):
            self.salary = self.base_salary*1.2 + 500

class Designer(Employee):
    def __init__(self, firstName, secondName, salary, experience, managers, effectiveness):    
        self.firstName = firstName
        self.secondName = secondName
        self.salary = salary
        self.experience = experience
        self.managers = managers
        self.effectiveness = effectiveness
    def updateSalary(self):
        if (self.experience > 2):
            self.salary += 200
        if (self.experience > 5):
            self.salary = self.base_salary*1.2 + 500
        self.salary = self.base_salary * self.effectiveness

class Manager(Employee):
    def __init__(self, firstName, secondName, salary, experience, managers, devs, designers):    
        self.firstName = firstName
        self.secondName = secondName
        self.salary = salary
        self.experience = experience
        self.managers = managers
        self.devs = devs
        self.designers = designers

        def updateSalary(self):
            if (self.experience > 2):
                self.salary += 200
            if (self.experience > 5):
                self.salary = self.base_salary*1.2 + 500

            if (len(self.devs) + len(self.designers) > 5):
                self.salary += 200
            if (len(self.devs) + len(self.designers) > 10):
                self.salary += 300
            if (len(self.devs) > len(self.designers)):
                self.salary *= 1.1
        

class Department():
    def __init__(self, managers, staff):
        self.managers = managers
        self.staff = staff

    def give_salary(self):
        for worker in staff:
            print(f"{worker.firstName} {worker.secondName}: got salary {worker.salary}")
                
                

    

