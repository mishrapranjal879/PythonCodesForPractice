# OOPs introduction----
# 1.-- Class in python--

class ClassName:
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    def method_name(self):
        print("This is a method")



# 2---

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object
s1 = Student("Pranjal", 20)

# Calling the method
s1.display()

# 3---

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount("Pranjal", 5000)
acc.deposit(2000)
acc.show_balance()
