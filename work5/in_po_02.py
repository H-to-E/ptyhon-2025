class Vehicles:
    pass
class Car(Vehicles):
    def drive(self):
        return '승용차가 화물을 운송중입니다'
class Truck(Vehicles):
    def drive(self):
        return '트럭이 화물을 운송중입니다'


Vehicles=[Truck(),Car(),Truck()]

for i in Vehicles:
    print(i.drive())