class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def speak(self):
        return "멍멍!"
class Cat(Animal):
    def speak(self):
        return '야옹!'
animallist=[Dog('dof'),Dog('doh'),Cat('caf')]

for a in animallist:
    print(a.name+':'+a.speak())