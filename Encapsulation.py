#Encapsulation
class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
        
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
        
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))
        
class Body:
    def __init__(self, size):
        self.size = size
        
    def __str__(self):
        return "Body:\n \tSize: " + self.size

class car():
    def __init__(self, tyres, engine, body):n
        self.tyres = tyres
        self.engine = engine
        self.body = body
        
    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body)
    
t = Tyres('Pirelli', True, 2.0) #(Here we are creating object of Tyres)
e = Engine('Diesel', 3) #(Here we are creating object of Engines)
b = Body('Medium') #(Here we are creating object of Body)

#now i want to create a object of class c and pass t,e,b as parametrs for class C

c = car(t,e,b) #(This is passing the objects in encapsulated form where we don't care about the implementation of other class)
print(c)

