class Student:
    college_name = "PESU"
    def __init__(self,name,age,sem):
        self.name = name
        self.age = age
        self.sem = sem
        print("College name is"+str(self.college_name))
        print("College name is"+str(Student.college_name))
    def show(self):
        print("The Student" + self.name + "is studying in " + self.college_name)
        print("The Student" + Student.college_name + "is studying in "  + Student.college_name)


s1 = Student("A",18,1)
s2 = Student("B",19,5)

print(Student.college_name)
print(id(s1.college_name))
print(id(Student.college_name))
print(id(s1.college_name))

Student.college_name = "PESIT"

print(id(s1.college_name))
print(id(Student.college_name))
print(id(s1.college_name))

s1.college_name ="PES"
s1.show()
