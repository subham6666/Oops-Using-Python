#We will create MultiLevel inheritance

class A():
    def test(self):
        return ("This is A")
class B(A):
    def test1(self):
        return ("This is B")
class C(B):
    def test2(self):
        return ("This is C")

#Now we will create object for class C and try to acess Class A & B functions.
obj = C()
print(obj.test())  #(Acess element of Class A)
print(obj.test1()) #(Acess element of Class B)



