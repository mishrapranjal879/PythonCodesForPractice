# Question 1----While Loop (print each digit (Reverse order)

# a = 145

# while a > 0:
#     print(a % 10)
#     a = a // 10


 # Question 2 ---(Sum of digits)

# a = int(input("please tell your number"))

# s = 0

# while a > 0:
#     s = a + a % 10
#     a = a // 10

# print(f"Your digits sum is {s}")


# Question 3 ----(reverse a number)

# a = int(input("please tell your number"))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(f"your number revers{rev}")

# Question 4---(Palindrome check)

# a = int(input("please tell your number"))

# copy = a

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if rev == copy:
#     print("yes your number is palindrome")

# else:
#     print("sorry your number is not palindrome")

# Question 5---(Automorphic Number)

a = 25
dup = a

square = a **2 

count = 0

while a > 0:
    count = count + 1
    a = a // 10

extract = square % (10**count)

if extract == dup:
    print("your number is automorphic")

else:
    print("sorry not an automorphic number")
