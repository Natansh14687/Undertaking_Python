class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def getLength(self):
        return self.__length
    def setLength(self,length):
        return self.__length
    
    def getWidth(self):
        return self.__width
    def setWidth(self,width):
        return self.__width

    def area(self):
        return self.__length*self.__width
    def perimeter(self):
        return 2*(self.__length+self.__width)
    
obj = Rectangle(4,5)
print(obj.area())
print(obj.perimeter())
