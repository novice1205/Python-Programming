# class Employee:
#     raiseamount = 1000
#     def __init__(self,name,dept,salary):
#         self.name = name
#         self.dept = dept
#         self.salary = salary
#     def applyraise(self):
#         self.salary += self.raiseamount
#         print("The salary is raised")
#     def showsalary(self):
#         print("The Salary of the employee is = " + str(self.salary))


# emp1 = Employee("A","HR",10000)
# emp1.showsalary()
# emp1.applyraise()
# emp1.showsalary()

class Book:
    def __init__(self,title,author,no_of_copies):
        self.title = title
        self.author = author
        self.no_of_copies = no_of_copies
    def buybooks(self,no_of_books):
        self.no_of_books = no_of_books
        self.no_of_copies -= self.no_of_books
        if(self.no_of_copies <= 0):
            print("Out of Stock")
    def showcopies(self):
        print("The number of copies left is = " + str(self.no_of_copies))

book1 = Book("Hello World!","Sumukha",15)
book2 = Book("Pointers in C","Sumukha N Sureban",9)

book1.showcopies()
book1.buybooks(5)
book1.showcopies()

book2.showcopies()
book2.buybooks(5)
book2.showcopies()