class Dog():
    def __init__(self,name,age,trick):
        self.name=name
        self.age=age
        self.trick = trick

    def bark(self): 
        print(f'{self.name}가 짖고 있습니다!')   

    def calldog(self):
        print(f'이름:{self.name},나이:{self.age}살')

    def show_tricks(self):
        print(f'{self.name}의 이름은 {self.trick}입니다')

a= Dog('바둑이',3,'뒹굴기')
a.bark()
a.calldog()
a.show_tricks()

b= Dog('멍멍이',5,'먹기')
b.bark()
b.calldog()
b.show_tricks()