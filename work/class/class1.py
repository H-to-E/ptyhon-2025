class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self): 
        print(f'{self.name}가 짖고 있습니다!')   

    def calldog(self):
        print(f'이름:{self.name},나이:{self.age}살')

a= Dog('바둑이',3)
a.bark()
a.calldog()

b= Dog('멍멍이',5)
b.bark()
b.calldog()