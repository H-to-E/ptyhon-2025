class Person():
    def __init__(self,name,code):
        self.name=name
        self.code=code
class Student(Person):
    def __init__(self,name,code,lesson,rate):
        super().__init__(name,code)
        self.lesson=lesson
        self.rate=rate
    def get_info(self):
        print(f"이름:{self.name}\n주민번호:{self.code}\n수강과목:{self.lesson}\n평점:{self.rate}")

class Teacher(Person):
    def __init__(self,name,code,teach,salary):
        super().__init__(name,code)
        self.teach=teach
        self.salary=salary
    def get_info(self):
        print(f"이름:{self.name}\n주민번호:{self.code}\n강의과목:{self.teach}\n월급:{self.salary}")

    
k= Student('홍길동','12345678','[자료구조]',0)
k.get_info()
h=Teacher('김철수','123456790','[Ptyhon]',3000000)
h.get_info()