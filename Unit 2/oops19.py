class University:
    def __init__(self,name):
        self.name = name
        self.departments = []
    def add_department(self,department):
        self.departments.append(department)


class Department:
    def __init__(self,name):
        self.name = name
        self.professors = []
    def add_professor(self,professor):
        self.professors.append(professor)


class Professor:
    def __init__(self,name):
        self.name = name
        self.courses = []
    def add_course(self,course):
        self.courses.append(course)

class Course:
    def __init__(self,name):
        self.name = name

uni = University("PESU")

d1 = Department("CA")
d2 = Department("CSE")
d3 = Department("FOMC")
d4 = Department("ME")

p1 = Professor("ABC")
p2 = Professor("PQR")
p3 = Professor("XYZ")
p4 = Professor("LMN")

c1 = Course("Programming with Python")
c2 = Course("Software Engineering")
c3 = Course("Data Analysis")
c4 = Course("Machine Learning")
c5 = Course("Business Analytics")
c6 = Course("Thermo Dynamics")

uni.add_department(d1)
uni.add_department(d2)
uni.add_department(d3)
uni.add_department(d4)

d1.add_professor(p1)
d2.add_professor(p2)
d3.add_professor(p3)
d4.add_professor(p4)

p1.add_course(c1)
p2.add_course(c1)

p1.add_course(c2)

p3.add_course(c4)
p3.add_course(c5)

p4.add_course(c5)
p4.add_course(c6)
p2.add_course(c5)
p2.add_course(c6)

print(uni.name)

# for d in uni.departments:
#     print(d.name)

# for d in uni.departments:
#     print(f"The Professor in {d.name}")
#     for p in d.professors:
#         print(p.name)

# for d in uni.departments:
#     print(f"The Department is {d.name}")
#     for p in d.professors:
#         print(f"The Professor is {p.name}")
#         for c in p.courses:
#             print("The Course is",c.name)
#     print("\n")

# for p in uni.departments[3].professors:
#     for c in p.courses:
#         print(c.name)

