#Access Specifier
#Public Access Specifier
# class Employee:
#     def __init__(self,name,project,salary):
#         self.name = name
#         self.project = project
#         self.salary = salary
#     def display(self):
#         print("Employee "+self.name+" works on "+self.project+" project for "+str(self.salary)+" salary.")
# e = Employee("Sumukha","MBA",100000)
# e.display()
# #Modification Outside the class.
# e.project = "MBA GUY"
# print("Employee "+e.name+" works on "+e.project+" project for "+str(e.salary)+" salary.")

#Protected Access Specifier(Single _)
# class Employee:
#     def __init__(self,name,project,salary):
#         self.name = name
#         self._project = project
#         self._salary = salary
#     def display(self):
#         print("Employee "+self.name+" works on "+self._project+" project for "+str(self._salary)+" salary.")
# e = Employee("Sumukha","MBA",100000)
# e.display()
# # Modify the protected member outside the class
# e._project = "Only MBA Guys"
# print("Employee "+e.name+" works on "+e._project+" project for "+str(e._salary)+" salary.")

#Private Access Modifier
class Employee:
    def __init__(self,name,project,salary):
        self.name = name
        self._project = project
        self.__salary = salary
    def display(self):
        print("Employee "+self.name+" works on "+self._project+" project for "+str(self.__salary)+" salary.")
    def update_salary(self,salary):
        self.__salary  = salary
e = Employee("Sumukha","MBA",100000)
# e.display()
# # Access through name mangling
# print("Employee "+e.name+" works on "+e._project+" project for "+str(e._Employee__salary)+" salary.")
#Modification outside the class
e._Employee__salary = 150000
print("Employee "+e.name+" works on "+e._project+" project for "+str(e._Employee__salary)+" salary.")

e.update_salary(200000)
e.display()