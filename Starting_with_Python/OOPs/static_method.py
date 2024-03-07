# Static methods 
class Person : 
    country = "India"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod # does not has access to class and object instances
    def massBunking():
        print("Isme kya hi mja hai")

    @classmethod #decorator : just a recomendation or aditional info or we can say sifarish like consider it as a class method not instance or normal method.
    def gaming(cls): #cls is default parameter for class method it's just a naming convention, we can set other name also 
        print("I live in country : ", cls.country)
        print("Humko bas khelne mai mja aata hai !")

Person.gaming() #can be call by class directly no need to define object or we can also define object.
per = Person("Natansh",100)
per.gaming()

Person.massBunking()
per = Person.massBunking()
print(per)