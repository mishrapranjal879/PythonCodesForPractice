# question 1----- (print hello world n times)
# n = int(input("please tell me how many times you want to print:-"))

# for i in range(n):
#     print(f"{i+1} : hello world")

# question 2 ----(print numbers 1 to n)

# n = int(input(" till where you want your numbers :-"))

# for i in range(1,n+1):
#     print(i)

# # question 3---(print number n to 1)

# n = int(input(" till where you want your numbers :-"))

# for i in range(n,0,-1):
#     print(i)

# Question 4----(sm of natural numbers (1 to n))

n = int(input("till where you want your sum :-"))

s= 0

for i in range(1,n+1):
    s = s + i

print(f"your sum is {s}")    
