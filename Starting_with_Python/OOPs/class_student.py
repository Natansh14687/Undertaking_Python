# Object Property
class Student :
    def __init__(self,enrlId,subject,hobby):    # first parameter is always self.
        self.enrlId = enrlId
        self.subject = subject
        self.hobby = hobby
# def __init__(self,help,nothing,hee): #inside the python only last init will be valid other ones will be rejected
# so we define single init method in class 
# self is representing future objects like get and store 

per1 =Student(123,"Python","Dancing")
print(per1.enrlId)
print(per1.subject)
print(per1.hobby)
print()
store = Student(456,"DSA","Singing")
print(store.enrlId)
print(store.subject)
print(store.hobby)
print()
per1.hobby = "Singing"
print(per1.hobby)
print()
# Class Property
class Person : 
    country = "India" # This is class property outside the init scope
    def __init__(self,name,age):
        self.name=name
        self.age=age

per1 = Person("Natansh",20)
print(per1.name, Person.country)
print()

class Car:
    def __init__(self,brand,color,make):
        self.brand=brand
        self.color=color
        self.make=make
    def accelerate(self):
        print(self.brand + " car is accelerating")

car1 = Car("Bughatti","Black",2019)
car1.accelerate()