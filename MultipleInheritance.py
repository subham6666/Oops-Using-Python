#Multiple Inheritance

class A():
   
    def test():
        return "This is from class A"

class B():

   def test():
        return "This is from class B"
    
    
class C(A,B):
    
    obj = A()
    obj1 = B()
    print(obj.test)
    print(obj1.test)
    




