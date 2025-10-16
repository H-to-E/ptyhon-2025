class Car():
    def __init__(self,speed=0,gear=0,color="white"):
        self.__speed=speed
        self.__gear=gear
        self.__color=color

    def setcolor(self,color):
        self.__color=color
    def setgear(self,gear):
        self.__gear=gear
    def setspeed(self,speed):
        self.__speed = speed
    
myCar =Car()
myCar.setgear(3)
myCar.setspeed(100)

print(myCar)

print("속도:",myCar._Car__speed)
print("기어:",myCar._Car__gear)
print("색상:",myCar._Car__color)