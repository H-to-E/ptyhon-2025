class Friend:
    def __init__(self,name=None,age=0):
        self.name=name
        self.age=age

x=Friend("홍길동",20)
x.age=-5
print(x.age)