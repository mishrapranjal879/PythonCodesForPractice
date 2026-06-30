# List Practiceset 
# Question 1 ---(sum and average of list)

a = [10, 20,30,40,50]
sum = 0

for i in a:
    sum= sum + i

print(f"sum of your list numbers is{sum}")
print(f"average of your list are {sum/len(a)}")

# Question 2---(maximum element with index)


a = [1, 45,23,89,45,90,12,36,82]

max = a[0]
index = [0]

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        index = i

print(f"your maximum element is {max} at index {index}")

