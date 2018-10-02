from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    @staticmethod
    def isAdult(age): 
        return age > 18
  
person1 = Person('Saurabh', 23) 
person2 = Person.fromBirthYear('Saurabh', 1995) 
  
print (person1.age)
#23 
print (person2.age)
#23 
print (Person.isAdult(17)) 
#False