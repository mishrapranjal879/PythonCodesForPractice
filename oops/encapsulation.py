# Encapsulation--(Encapsulation means bundling data (attributes) and methods into one unit (class).)

class Animal:
    name = "Lion"

def speak(self):
    print("hello i will roar")

obj = Animal()

print(obj.name)

obj.name = "Zebra"
print(obj.name)