class Car():
    def __init__(self,speed=0,gear=0,color=None ):
        self.__speed=speed
        self.__gear=gear
        self.__color=color

    def setcolor(self,color):
        self.__color=color
    def setgear(self,gear):
        self.__gear=gear
    def setspeed(self,speed):
        self.__speed = speed
    def __str__(self):
        return f'속도:{self.__speed}\n기어:{self.__gear}\n색상:{self.__color}'


myCar =Car()
myCar.setgear(3)
myCar.setspeed(100)
myCar.setcolor("red")

print(myCar)