#Abstraction(Protected using an _,Here name,surname,yearofbirth are all protected variable)
class Person:
    def __init__(self, name, surname, year_of_birth):
        self._name = name
        self._surname = surname
        self._year_of_birth = year_of_birth
    
    def age(self, current_year):
        return current_year - self._year_of_birth
    def __str__(self):
        return "%s %s and was born %d." \
                % (self._name, self._surname, self._year_of_birth)
    
alec = Person("Alec", "Baldwin", 1958)
print(alec)
print(alec._surname) #(here we are accessing the protected variable using object._variable name)



