# Abstraction ---
# Abstraction 8is used to simplifying complex system by focusing on essential features and hiding unnecessary details.
# its is used to definr a common interface for different sub calsses.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("hello i make a woof sound")
    def hello(self):
        print(" i am a dog and i woof")

obj = Dog()  
