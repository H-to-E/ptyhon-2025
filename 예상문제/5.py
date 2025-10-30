from tkinter import *

# Student 클래스 정의
class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.stu_id == other.stu_id
        return False

    def __repr__(self):
        return f"Student(ID: {self.stu_id}, Name: {self.name})"

# 학생 리스트 초기화
students = [Student('20251010', 'ㅏ')]

# 학생 객체 생성 후 리스트에 추가하는 함수
def print_fields():
    stu_id = e1.get()
    name = e2.get()
    student = Student(stu_id, name)
    
    if student in students:
        Label(root,text="환영합니다").grid(row=3, column=0, sticky=W, pady=4)
    else:
        Label(root,text="등록되지 않은 학생입니다").grid(row=3, column=0, sticky=W, pady=4)

# GUI 설정
root = Tk()
root.title('중간고사 5번')

# 라벨과 엔트리 위젯 설정
Label(root, text='아이디').grid(row=0)
Label(root, text='이름').grid(row=1)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# 버튼 설정
Button(root, text='등록', command=print_fields).grid(row=2, column=0, sticky=W, pady=4)
Button(root, text='종료', command=root.quit).grid(row=2, column=1, sticky=W, pady=4)

root.mainloop()
