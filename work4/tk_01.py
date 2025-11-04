from tkinter import *

class Book:
    def __init__(self,title,author,borrowed=False):
        self.title= title
        self.author = author
        self.borrowed = borrowed

    def borrow_book(self):
        if self.borrowed == False:
            self.borrowed = True
            return self.title+'이(가) 대출되었습니다'
        else:
            return self.title+'은(는) 이미 대출 중입니다'

    def return_book(self):
        if self.borrowed == True:
            self.borrowed = False
            return self.title+'이(가) 반납되었습니다'
        else:
            return self.title+'은(는) 대출되지 않은 상태입니다'
    

root= Tk()
root.title('도서 대출 관리 시스템')

Label(root,text='도서 대출 관리 시스템').pack()

frame1=Frame(root)
frame1.pack()

frame2=Frame(root)
frame2.pack()

frame3=Frame(root)
frame3.pack()



Label(frame1,text='제목:').pack(side=LEFT)
name= Entry(frame1)
name.pack(side=LEFT)
Label(frame2,text='저자:').pack(side=LEFT)
author=Entry(frame2)
author.pack(side=LEFT)

book = None
b_n = name.get()
b_a = author.get()

rlabel= Label(root)
rlabel.pack()

def borrow():
    global book
    b_n = name.get()
    b_a = author.get()

    if book == None:
        book= Book(b_n,b_a)
        te=book.borrow_book()
        rlabel.config(text=te)
    else:
        te=book.borrow_book()
        rlabel.config(text=te)
def retrunbook():
    global book

    te=book.return_book()
    rlabel.config(text=te)

b_B= Button(frame3,text="대출",command=borrow)
b_B.pack(side=LEFT)
r_B= Button(frame3,text="반납",command=retrunbook)
r_B.pack(side=LEFT)

root.mainloop()
