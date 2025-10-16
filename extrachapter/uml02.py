class Animal():
    def __init__(self,age:int,gender:str):
        self.age=age
        self.gender=gender
    def isMammal(self) -> None:
        print('이 동물이 포유류 인지 확인합니다')

    def introduce(self,name:str):
        print(f'이름:{name},나이:{self.age},성별:{self.gender}')

    
class Duck(Animal):
    def __init__(self,age:int,gender:str,beakcolor:str="Yellow"):
        super().__init__(age,gender)
        self.beakcolor=beakcolor

    def swim(self):
        print('첨벙첨벙')
    def quak(self):
        print('꽥꽥')

class Fish(Animal):
    def __init__(self,age:int,gender:int,sizeInft:int):
        super().__init__(age,gender)
        self.sizeInft=sizeInft
    def swim(self):
        print('물고기가 헤엄치고 있습니다')


duck=Duck(2,'male')
fish=Fish(5,'female',3)

duck.introduce('오리')
duck.swim()
duck.quak()

fish.introduce('물고기')
fish.swim()
