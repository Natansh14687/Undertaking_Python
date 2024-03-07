# class Point:
#     def __init__(self,x,y,z):
#         self.x=x**2
#         self.y=y**2
#         self.z=z**2
#     def sqSum(self):
#         print(self.x+self.y+self.z)

class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
        print(self.x**2 + self.y**2 + self.z**2)
        
pt1=Point(1,2,3)
pt1.sqSum()