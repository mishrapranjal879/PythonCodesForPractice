# Inheritance---(inheritance is the mechanism by which a class(child) can use the properties and methods of another class (parent))

class Animal:  # parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"your name is {self.name} and your age is {self.age}")   


class Human(Animal):  # child class , sub class
    def __init__(self, name, age,number,group):
        super().__init__(name, age)  
        self.number = number
        self.group = group
    
    

obj = Animal("lion",12)
obj2 = Human("Pranjal",22,9651201703,"A+")


obj2.info()

class Robots(Human):
    def __init__(self, name, age, number, group,address):
        super().__init__(name, age, number, group)
        self.address = address
        




        