from tkinter import *
class Book:
    def __init__(self,title,author,borrowed=False):
        self.title= title
        self.author = author
        self.borrowed = borrowed

    def borrow(self):
        if self.borrowed == False:
            self.borrowed = True
            Label(root,text=f'{self.title}이(가) 대출되었습니다',fg='blue').pack()
        else:
            Label(root,text=f'{self.title}은(는) 이미 대출 중입니다',fg='blue').pack()

    def return_book(self):
        if self.borrowed == True:
            self.borrowed = False
            Label(root,text=f'{self.title}이(가) 반납되었습니다',fg='green').pack()
        else:
            Label(root,text=f'{self.title}은(는) 대출되지 않은 상태입니다',fg='green').pack()

    
root=Tk()
root.title('도서 대출 관리 시스템')
Label(root,text='도서 대출 관리 시스템').pack()




frame1= Frame(root)
frame1.pack()
frame2= Frame(root)
frame2.pack()
frame3= Frame(root)
frame3.pack()



Label(frame1,text='제목').pack(side=LEFT)
e1=Entry(frame1)
e1.pack(side=LEFT)
Label(frame2,text='저자').pack(side=LEFT)
e2=Entry(frame2)
e2.pack(side=LEFT)

A=None
def book_borrow():
    global A
    name= e1.get()
    author = e2.get()
    
    if A is None:
        A= Book(name,author)
    else:
        k=A.borrow()
def book_return():
    global A
    k= A.return_book()
Button(frame3,text='대출',command=book_borrow).pack(side=LEFT,padx=20)
Button(frame3,text='반납',command=book_return).pack(side=LEFT,padx=20)

root.mainloop()
