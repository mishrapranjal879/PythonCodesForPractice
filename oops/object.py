#  Object----

class Factory:
    a = "hello i am a attribute"

    def hello():
        print("hello i am a method")

obj = Factory()# obj becomes an object who can access anything inside the class till now.
obj2 = Factory()

print(obj.a)
obj2.hello()