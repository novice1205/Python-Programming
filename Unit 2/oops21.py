# Simulate a library loan system which has book(author title category availability), 
# member(name,contact), loan(aggregates book and members with borrow, take)
# library class which aggregates books  and members and provide functionalities issuing and returning books

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def return_book(self,book):
        self.books.append()


class Book:
    def __init__(self,title,category,availability):
        self.title = title
        self.category = category
        self.availibility = availability

class Member:
    def __init__(self,name,contact)
        self.name = name
        self.contact = contact

class Loan:
    def