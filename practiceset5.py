# 1. Sum of Numbers

# Write a function sum_numbers(n) that uses a loop to calculate the sum of numbers from 1 to n.

def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


num = int(input("Enter a number: "))
result = sum_numbers(num)
print("Sum =", result)

# 2. Multiplication Table

# Write a function table(num) that prints the multiplication table of a given number from 1 to 10 using a loop.

def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


number = int(input("Enter a number: "))
table(number)

# Count Vowels

# Write a function count_vowels(text) that uses a loop to count the number of vowels (a, e, i, o, u) in a string.

def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count


text = input("Enter a string: ")
result = count_vowels(text)
print("Number of vowels =", result)

# 4. Find the Largest Number

# Write a function largest(numbers) that takes a list of numbers and uses a loop to return the largest number.

def largest(numbers):
    largest_num = numbers[0]

    for num in numbers:
        if num > largest_num:
            largest_num = num

    return largest_num


numbers = [12, 45, 7, 89, 23]
result = largest(numbers)
print("Largest number =", result)

# 5. Prime Number Checker

# Write a function is_prime(num) that uses a loop to check whether a number is prime or not.

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")