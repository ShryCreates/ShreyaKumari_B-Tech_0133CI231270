from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

class Developer(Employee):
    __salary = 80000
    def work(self):
        print("Developer is coding")

    def get_salary(self):
        print(f"Developer Salary: {self.__salary}")

class Manager(Employee):
    __salary = 100000
    def work(self):
        print("Manager is managing")

    def get_salary(self):
        print(f"Manager Salary: {self.__salary}")

d=Developer()
d.work()
d.get_salary()
m=Manager()
m.work()
m.get_salary()
