#Now we will abstract methods as public,protected and private:

class test():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def publictest(self):
        return "This is a public method"
    def _protectedtest(self):
        return "This is protected method"
    def __privatetest(self):
        return "This is Private method"

xyz = test(1,2)

print(xyz.publictest())
print(xyz._protectedtest())
print(xyz._test__privatetest())


