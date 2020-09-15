#Having a __Init__ function to initialise the concept

class Car():
    
    def __init__(subham,Engine,Interior):
        subham.Engine = Engine
        subham.Interior = Interior
        
#object Creation passing the parameter
Audi = Car("Luxorious","Ulra")
Tata = Car("Economy","Jugad")

#Acessing the element of the class
print(Audi.Engine)
print(Tata.Interior)
      
