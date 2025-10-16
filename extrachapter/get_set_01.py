class Friend:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.__age=age

    def getname(self):
        return self.__name
    def getage(self):
        return self.__age

    def setname(self,name):
        self.__name=name
    def setage(self,age):
        if age >=0:
            self._age=age
        else:
            print("나이는 음수가 될 수 없습니다")
    def introduce(self):
        print(f"안녕하세요! 저는 {self._age}살 {self._name}입니다.")


x=Friend("홍길동",20)
x.introduce()