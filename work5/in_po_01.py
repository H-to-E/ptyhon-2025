class Car:
    def __init__(self,speed):
        self.speed=speed
    def get_speed(self):
        return f'현재 속도:{self.speed}'
class Sport(Car):
    def __init__(self,speed,Turbo=False):
        super().__init__(speed)
        self.Turbo=Turbo

    def get_speed(self):
        if self.Turbo==True:
            return f'현재 속도:{self.speed}(터보 ON)'
        else:
            return f'현재 속도:{self.speed}(터보 OFF)'
car1=Car(80)
print(car1.get_speed())

sport1=Sport(80,False)
print(sport1.get_speed())

sport2=Sport(150,True)
print(sport2.get_speed())            