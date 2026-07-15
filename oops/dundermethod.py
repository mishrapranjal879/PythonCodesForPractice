# Dunder / Magic Methods--
# Dunder methods are special methods in python that define 
# object behavior for built-in operations.
# (e.g.,__init__,__str__).(They are prefixed with double underscores)

class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} is your name and your marks are {self.marks}"


obj = Students("Pranjal",95)

print(obj)

class Shopping:
    def __init__(self,items):
        self.items = items

    def __len__(self):
        return len(self.items)  
        
obj = Shopping(['apple','milk',"bread"])
obj2 = Shopping(["apple","banana"])

print(len(obj2))

        
