#Class Polymorphism
# class India:
#     def capital(self):
#         print("The capital is Delhi")
# class USA:
#     def capital(self):
#         print("The capital is Washington")
# class Australia:
#     def capital(self):
#         print("The capital is Sydney")
# class Singapore:
#     def capital(self):
#         print("The capital is Singapore")
#Duck Typing
# i=India()
# u=USA()
# a=Australia()
# s=Singapore()
# for x in [i,u,a,s]:
#     x.capital()


# Method Overriding:
# class Animal:
#     def make_sound(self):
#         print("Generic Sound")
# class Cat:
#     def make_sound(self):
#         print("Meow")
# class Dog:
#     def make_sound(self):
#         print("Woof")
# class Lion:
#     def make_sound(self):
#         print("Roar")
# a=Animal()
# c=Cat()
# d=Dog()
# l=Lion()
# for i in (a,c,d,l):
#     i.make_sound()