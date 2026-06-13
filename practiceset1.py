# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a>b:
#     print(f"{a} is greater than {b}")

# elif b>a:
#     print(f"{b} is greater than {b}")

# else:
#     print(f"{a} is equal to {b}")
        

# # Question 2------

# gen = (input("please tell your gender in Chracter(m,f) : - "))

# if gen == 'm':
#     print("hello sir how are you ")

# else:
#     print("hello mam how are you") 

# Question 3-----(case sensitive letters)

# gen = (input("please tell your gender in Chracter(m,f) : - "))

# if gen == 'm' or gen == 'M':
#     print("hello sir how are you ")

# elif gen == "F" or gen == "f":
#     print("hello mam how are you") 

# else:
#     print("Wrong input only provide m or f") 

# Question 4-------(Even or odd check)

# a = int(input("please tell your number:- "))

# if a % 2 == 0:
#     print("your number is even")

# else:
#     print("your number is odd ")


# Question 5------(Voting Eligibility)
# name = input("Enter your name:- ")
# age = int(input("Please tell me your age:- "))

# if age >=18:
#     print(f"Hello {name} eligible to vote")

# else:
#     print(f"Hello {name} sorry you can vote after {18 - age} years")    


# Question 6-------(Day numbers to day name)

# a = int(input("Please tell your day(1-7):- "))

# if a == 1:
#     print("Monday it is")

# elif a == 2:
#     print("Tuesday it is")

# elif a == 3:
#     print("Wensday it is")

# elif a == 4:
#     print("Thursday it is")

# elif a == 5:
#     print("Friday it is")

# elif a == 6:
#     print("Saturday it is")

# elif a == 7:
#     print("Sunday it is") 

# else:
#     print("Sorry your input is wrong")

# Question 7------(Greatest of three number)

# a = int(input("Please tell yuor numbers : - "))
# b = int(input("Please tell yuor numbers : - "))
# c = int(input("Please tell yuor numbers : - "))

# if a == b and b == c:
#     print("all the numbers are equal")

# elif a == b or b == c or c == a:
#     print("any two numbers are equal")

# elif a > b and a > c:
#     print(f"{a} is the greatest number")

# elif b > a and b > c:
#     print(f"{b} is the greatest number")

# else:
#     print(f"{c} is the greatest number")
                

# Question 8----(Leap year checker )

# year = int(input("please tell your year :- "))

# if year % 100 == 0 and year % 400 == 0:
#     print("its a leap year")

# elif year % 100 !=0 and year % 4 == 0:
#     print("its a leap year") 

# else:
#     print("its not a leap year") 

# Question 9-------(Shop discount calculator)

# bill = int(input("please tell your total amount : - "))

# if bill >= 1000 and bill <= 4999:
#     print(f" you got a discount of 10% your final amount is {(bill * 90)/100} ")

# elif bill >= 5000:
#     print(f" you got a discount of 20% your final amount is {(bill * 80)/100} ")

# else:
#     print("sorry no discount for you")


# Question 10-------(Vowel and consonent)

char = input("please tell your Alphabet :- ")

if char in "aeiouAEIOU":
    print("its a vowel")

else:
    print("its a consonent")





    
