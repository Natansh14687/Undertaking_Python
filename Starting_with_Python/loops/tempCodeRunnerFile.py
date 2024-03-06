class Point:
    def __init__(self,x,y,z):
        self.x=x**2
        self.y=y**2
        self.z=z**2
    def sqSum(self):
        print(self.x+self.y+self.z)