class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        self.sort = age
    def __str__(self):
        return f"Name is {self.Name} and age is {str(self.Age)}"
class Book:
    def __init__(self,title,author,year):
        self.Title = title
        self.Author = author
        self.Year = year
        self.sort = year
    def __str__(self):
        return f"Title is  {self.Title} and author is {self.Author} and year is {str(self.Year)}"
class Car:
    def __init__(self,make,model,year):
        self.Make = make
        self.Model = model
        self.Year = year
        self.sort = year
    def __str__(self):
        return f"Make is {self.Make} and model is {self.Model} and year is {str(self.Year)}"
        
people = [Person("Alice",32), Person("Bob",28), Person("Catlin",24),Person("Draco",20)]
print(people)
book = [Book("Data Science and Analytics","Parth Raheja",2023),Book("Web Dev","Varun Kothari",2022),Book("Let's do MBA Guys","Sumukha N Sureban",2021),Book("Light Weight Baby!","Vashist Bardhan._27",2019)]
cars = [Car("Maruti","800",2000),Car("Audi","R8",2021),Car("Tata","Harrier",2023)]

def custom_sort(objects):
    sorted_objects = sorted(objects, key=lambda o:o.sort)
    return sorted_objects
sorted_books = custom_sort(book)
for i in sorted_books:
    print(i)