class User():
    def __init__(self,id:int,name:str):
        self.__id=id
        self.__name=name

    def getTodo(self):
        return f'return todo method'

    def write(self,write:str):
        print(f'{self.__name}이(가) 글 작성;{write}')

class Student(User):
    def __init__(self,id:int,name:str):
        super().__init__(id,name)

    def study(self):
        print('f{self.__name} is studying')


class Teacher(User):
    def __init__(self,id:int,name:str):
        super().__init__(id,name)

    def teach(self):
        print('f{self.__name} is teaching')
