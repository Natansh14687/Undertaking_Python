# encapsulation : binding together of data and the method.
# state or field of class should be private.
# but should have public methods.

class Person:
    def __init__(self,name,car):
        self.name=name
        self.car=car

    def gatName(self):
        return self.__name
    
    def setName(self,name):
        self.__name=name

    def getCar(self):
        return self.__car
    
    def setCar(self,car):
        self.__car=car