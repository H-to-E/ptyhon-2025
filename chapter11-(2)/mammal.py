class Mammal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        print('포유류:',self.name,self.age)

class Person(Mammal):
    def __init__(self,name,age,job):
        super().__init__(age,name)
        self.job=job
    def get_info(self):
        print('사람',self.name,self.age,self.job)

m= Mammal('동물',30)
k=Person('KIm',30,'Engineer')
m.get_info()
k.get_info()