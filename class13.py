# Exception Handling---
# Exception Handling is a way to handle errors gracefully so that your program doesn't crash when an unexpected error occurs.

# Why use Exception Handling?
# Prevents the program from stopping unexpectedly.
# Displays meaningful error messages.
# Allows the rest of the program to continue running.

a = int(input("provide your numbers : -"))
b = int(input("provide your numbers : -"))

print(a/b)

print(a+b)

# 1. Try---

a = int(input("provide your numbers : -"))
b = int(input("provide your numbers : -"))

try:
    print(a/b)

except Exception as err:
    print(f"sorry an error occured as {err}")

else:
    print("there was no error")

finally:
    print("I will execute no matter what")
print(a+b)


