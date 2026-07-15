# Polymorphism--
# Polymorphism allows different classes to define methods with the name but differnt behaviors. In python , it is typically achieved through method overriding.

class Animal:
    name = "lion"
    def speak(self):
        print("hello i roar")

class Bird:
    name = "sparrow"

    def speak(self):
        print("hello i am say something")


    
obj = Animal()
obj2 = Bird()

obj.speak()
obj2.speak()

# Types of polymorphism--

# Method overloading
# Method overriding
