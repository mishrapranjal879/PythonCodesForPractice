# 4. Animal Sounds (Inheritance)

# Create a parent class Animal with a method:

# Parent Class
class Animal:

    # Parent method
    def sound(self):
        print("Animals make different sounds.")


# Child Class Dog
class Dog(Animal):

    # Overriding the parent method
    def sound(self):
        print("Dog says: Bark")


# Child Class Cat
class Cat(Animal):

    # Overriding the parent method
    def sound(self):
        print("Cat says: Meow")


# Create Objects
animal = Animal()
dog = Dog()
cat = Cat()

# Call Methods
animal.sound()
dog.sound()
cat.sound()

# 5. Shape Area (Polymorphism)

# Create a base class Shape with a method:

import math

# Base Class
class Shape:

    # Parent Method
    def area(self):
        print("Area cannot be calculated for a generic shape.")


# Child Class - Rectangle
class Rectangle(Shape):

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Overriding area() method
    def area(self):
        return self.length * self.width


# Child Class - Circle
class Circle(Shape):

    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Overriding area() method
    def area(self):
        return math.pi * self.radius * self.radius


# Create Objects
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Display Areas
print("Area of Rectangle =", rectangle.area())
print("Area of Circle =", round(circle.area(), 2))