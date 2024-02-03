#Multiple Inheritance
class A:
    def __int__(self,val):
        self.val = val
    def write(self):
        print("The value in Class A " + str(self.val))

class B:
    def __init__(self,val):
        self.val = val
    def write(self):
        print("The value in Class B " + str(self.val))

class C(A,B):
    def __init__(self,v1,v2):
        super().__init__(v1)
        self.val = v2

c = C(10,20)
c.write()
print(C.mro())
