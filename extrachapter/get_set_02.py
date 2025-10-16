class Friend:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.__age=age

    def getage(self):
        return self.__age

    def setage(self,age):
        if age >=0:
            self._age=age
        else:
            print("나이는 음수가 될 수 없습니다")

x=Friend("홍길동",20)
x.setage(-5)
