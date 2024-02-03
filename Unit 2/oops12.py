#Access Specifiers and Inheritance

#Protected Access Specifier
# class A:
#     def __init__(self,a):
#         self._a = a
# class B(A):
#     def __init__(self,a):
#         super().__init__(a)
#     def display(self):
#         print("The value in B is "+ str(self._a))
#     def update_val(self,x):
#         self._a = x
# b=B(10)
# b.display()
# b.update_val(20)
# b.display()
# b.update_val("Hello")
# b.display()

#Private Access Specifier and Inheritance
# class A:
#     def __init__(self,x):
#         self.__x = x
# class B(A):
#     def __init__(self,x):
#         super().__init__(x)
#     def display(self):
#         print("The value of inside B is "+ str(self.__x))
# b = B(100)
# b.display()