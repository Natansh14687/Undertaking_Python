# Access Modifiers
# Two Types : 1. Public,  2. Private
# In other programming there is also protected type but it is not in python.

class Cricket:
    def __init__(self,player1,player2,fight):
        self.player1=player1
        self.player2=player2
        self.__fight=fight

    def play(self):
        print(self.__fight)
        print("I am copy cricket champion")

cric = Cricket("MS Dhoni","Virat kohli","Dhoni")
print(cric.player1) # This is public variable
# here that __fighter will give error if we wanted to access here.
# Private : can't access outside the class  to make it private double underscore like this self.__fight=fight nut we can access it inside the class

