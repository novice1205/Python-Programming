#Static and Class methods
#Static Methods

# class MyClass:
#     v=10
#     def __init__(self,val):
#         self.val = val
#     @staticmethod
#     def f(a,b):
#         return a+b
# MyClass(10)
# print(MyClass.f(10,20))
# print(type(MyClass.f))

class Maths:
    @staticmethod
    def is_even(x):
        return x%2 == 0

    @staticmethod
    def pow(x,y):
        return x**y

    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def fact(x):
        if x==0:
            return 1
        else:
            return x * Maths.fact(x-1)

print(Maths.pow(2,5))
print(Maths.is_even(20))
print(Maths.add(10,20))
print(Maths.fact(5))