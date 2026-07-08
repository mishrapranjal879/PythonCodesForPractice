# Ques.-1. Student Class (Classes and Objects)

# Create a class Student with the following attributes:

# name
# roll_no
# marks

class Student:
    # Constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to display student details
    def display(self):
        print("----- Student Details -----")
        print("Name     :", self.name)
        print("Roll No. :", self.roll_no)
        print("Marks    :", self.marks)

    # Method to check pass/fail
    def is_pass(self):
        if self.marks >= 40:
            print("Result   : Pass")
        else:
            print("Result   : Fail")


# Creating objects
student1 = Student("Pranjal", 101, 85)
student2 = Student("Rahul", 102, 35)

# Display details and result
student1.display()
student1.is_pass()

print()

student2.display()
student2.is_pass()

# Ques.2--
# Bank Account (Encapsulation)

# Create a class BankAccount with:

# account_holder
# balance

# Add methods:

# deposit(amount)
# withdraw(amount)
# check_balance()

# Condition:

# Do not allow withdrawal if the balance is insufficient.

class BankAccount:

    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance      # Private attribute

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    # Check Balance Method
    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")


# Create Object
account1 = BankAccount("Pranjal Mishra", 10000)

# Check Initial Balance
account1.check_balance()

# Deposit Money
account1.deposit(5000)
account1.check_balance()

# Withdraw Money
account1.withdraw(3000)
account1.check_balance()

# Try to Withdraw More Than Balance
account1.withdraw(15000)
account1.check_balance()

# Ques.3---
#  Employee Salary (Constructor and Methods)

# Create a class Employee with:

# name
# basic_salary

# Add methods:

# Calculate HRA = 20% of basic salary.
# Calculate DA = 10% of basic salary.
# Calculate total salary.

class Employee:

    # Constructor
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    # Calculate HRA
    def calculate_hra(self):
        return self.basic_salary * 0.20

    # Calculate DA
    def calculate_da(self):
        return self.basic_salary * 0.10

    # Calculate Total Salary
    def calculate_total_salary(self):
        hra = self.calculate_hra()
        da = self.calculate_da()
        total = self.basic_salary + hra + da
        return total

    # Display Employee Details
    def display(self):
        print("------ Employee Details ------")
        print("Employee Name :", self.name)
        print("Basic Salary  : ₹", self.basic_salary)
        print("HRA (20%)     : ₹", self.calculate_hra())
        print("DA (10%)      : ₹", self.calculate_da())
        print("Total Salary  : ₹", self.calculate_total_salary())


# Create Employee Objects
emp1 = Employee("Pranjal Mishra", 50000)
emp2 = Employee("Rahul Sharma", 30000)

# Display Details
emp1.display()

print()

emp2.display()

