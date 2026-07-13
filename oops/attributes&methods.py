class Animal:
    gender = "Male" # calss attribute

    def __init__(self,name,age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    def info(self): # instance method
        print("this is a method") 

    @classmethod 
    def clmethod(cls): # class method 
        print(f"{cls.gender} is your gender")
    
    @staticmethod
    def hello():
        print("hello i am a static method ")

           
         
obj = Animal("lion",12) 

obj.info()

obj.clmethod()

obj.hello()

# Make a student rejistration system ask for name,age,number,blood group

class Registration:
    def __init__(self,name,age,number,blood):
        self.name = name
        self.age = age
        self.number = number
        self.blood = blood

    def info(self):
        print(f"hello your name is {self.name}\n your age is {self.age}\n your number is {self.number}\n your blood group is {self.blood}")

student1 = Registration("Pranjal",22,9651201703,"A+") 
student2 = Registration("Siddhant",23,9651204008,"B+") 
student3 = Registration("Ketan",21,9651201778,"O+") 


student1.info()        


