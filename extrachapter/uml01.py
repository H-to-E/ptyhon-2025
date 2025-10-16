class Rectangle():
    def __init__(self,height:int,width:int):
        self.height=height
        self.width=width
    def getArea(self):
        return self.height*self.width
    def resize(self,height:int,width:int):
        self.height=height
        self.width=width
    

a= Rectangle(20,30)
print(a.getArea())

a.resize(45,50)
print(a.getArea())