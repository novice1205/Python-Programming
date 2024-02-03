#Static and Class methods
#Class Methods

# class MyClass:
#     v=10
#     @classmethod
#     def f(cls,x):
#         cls.v +=x
# print(MyClass.v)

# class Animal:
#     def __init__(self,breed):
#         self.breed = breed
#     @classmethod
#     def create_from_breed(cls,breed):
#         b = cls(breed)
#         return b
# a = Animal("dog")
# print(a.breed)
# b = Animal.create_from_breed("cat")
# print(type(a))
# print(type(b))
# print(a.breed)
# print(b.breed)
#Write a program that creates an emp who has dept and sal. 
#Write a method that calculates the total number of employees in the company. 

class Employee:
    total_employees = 0
    def __init__(self, department, salary):
        self.department = department
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

emp1 = Employee("IT", 60000)
emp2 = Employee("HR", 50000)
emp3 = Employee("Finance", 70000)
emp4 = Employee("CEO", 7000000)
emp5 = Employee("CFO", 700000)

total_employees = Employee.get_total_employees()
print(f"Total number of employees in the company: {total_employees}")
