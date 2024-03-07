# code Re-use and Relationship -> parent child (hierarichal)
# dna test in programming is inheritance.
# cat isA animal   here animal is parent and cat is child.

class Animal :
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()