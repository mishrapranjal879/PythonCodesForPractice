# Function in python---(it is a block of code)

# def Greet(): # defining a function
#     print("hello greetings from sheriyans")

# Greet()  # this is calling the function

# # Parameters and Arguments---

# def addition(a,b):

#     print(a + b)

# addition(12,76) (keyword arguments)



def palindrome(x):
    rev = 0
    copy = x

    while x >0:
        rev =( rev * 10) + (x % 10)
        x = x // 10

    if rev == copy:
        return True
    
    else:
        return False

print(palindrome(121))
print(palindrome(454))

