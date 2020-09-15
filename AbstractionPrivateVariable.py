#(Abstraction of Private Variables using __VariableName ***here name,surname,yearofbirth are all private variables***):-

class Person:
    def __init__(self, name, surname, year_of_birth):
        self.__name = name
        self.__surname = surname
        self.__year_of_birth = year_of_birth
    
    def age(self, current_year):
        return current_year - self.__year_of_birth
    
    def __str__(self):
        return "%s %s and was born %d." \
                % (self.__name, self.__surname, self.__year_of_birth)
    
alec = Person("Alec", "Baldwin", 1958)
##print(alec.__name)#(Here if we try to acess the private variable __name using same notion like public/protected then we can't acess it is private)
#So in order to know how each variable is stored internally we can use in built function like __dict__

print(alec.__dict__)

#now we can acess private element by using following method:
print(alec._Person__name)

