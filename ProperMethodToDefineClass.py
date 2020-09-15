#We defined two more methods age and __str__. 
#The latter is once again a special method that is called by Python when the object has to be represented as a string (e.g. when has to be printed). 
#If the __str__ method isn't defined the print command shows the type of object and its address in memory. 
#We can see that in order to call a method we use the same syntax for attributes (instance_name.instance _method).

class Person:
    def __init__(a, name, surname, year_of_birth):
        a.name = name
        a.surname = surname
        a.year_of_birth = year_of_birth
    
    def age(a, current_year):
        return current_year - a.year_of_birth
    
    def __str__(a):
        return "%s %s was born in %d ." % (a.name, a.surname, a.year_of_birth)
    
alec = Person("Alec", "Baldwin", 1958)
print(alec)
print(alec.age(2014))