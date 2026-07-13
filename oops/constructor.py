# constructor---
# constructor is a method that runs autometically whenever we call the class.And the constructor will target the location of that object.

# def factory(material,zips,pockets):
#     pass
# factory() 

class Factory:
    def __init__(self,material,zips,pockets):
         self.material = material
         self.zips = zips
         self.pockets = pockets

    def showdetails(self):
         print(self.material,self.zips,self.pockets)




reebok = Factory("Leather",3,3)  
campus = Factory("nylon",2,2)
print(reebok.material)
print(campus.material)  

campus.showdetails()
                  
            
