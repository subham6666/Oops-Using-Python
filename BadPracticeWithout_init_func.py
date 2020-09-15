# It is possible to create a class without the __init__ method, but this is not a recommended style because classes should describe homogeneous entities.

class Person:
  
    def set_name(self, name):
        self.name = name
        
    def set_surname(self, surname):
        self.surname = surname
        
    def set_year_of_birth(self, year_of_birth):
        self.year_of_birth = year_of_birth
        
    def age(self, current_year):
        return current_year - self.year_of_birth
    
    def __str__(self):
        return "%s %s was born in %d ." \
                % (self.name, self.surname, self.year_of_birth)

president = Person()
#The following line will give error as we have not set any attributes 
##print(president.name)

#Correct Way of Doing things is 
president.set_name('John')
president.set_surname('Doe')
president.set_year_of_birth(1940)
print('Mr', president.name, president.surname,
      'is the president, and he is very old. He is',
      president.age(2014))

