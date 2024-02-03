class Student:
    def __init__(self,name,rank,sem):
        self.name = name
        self.rank = rank
        self.sem = sem
    def display(self):
        print("Student "+self.name+" has got a "+str(self.rank)+" rank in " + str(self.sem) + " semester.")
s1 = Student("Sumukha",1,6)
s2 = Student("Varun",2,3)
s3 = Student("Parth",2,1)
s4 = Student("Samiksha",1,4)

for i in [s1,s2,s3,s4]:
    i.display()