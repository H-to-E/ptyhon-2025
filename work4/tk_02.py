from tkinter import *

class Book:
    def __init__(self,title,author,borrowed=False):
        self.title= title
        self.author = author
        self.borrowed = borrowed

    def borrow_book(self):
        if self not in borrowed_books:
            borrowed_books.append(self)
            Book.update_borrowed_list(self)
            return self.title+' 이(가) 대출되었습니다','blue'
        else:
            Book.update_borrowed_list(self)
            return self.title+' 은(는) 이미 대출중 입니다','red'

    def return_book(self):
        if self in borrowed_books:
            borrowed_books.remove(self)
            Book.update_borrowed_list(self)
            return self.title+' 이(가) 반납되었습니다','green'
        else:
            return self.title+' 은(는) 대출되지 않은 상태입니다','red'
    def __eq__(self,other):
        if isinstance(other,Book):
            return self.author== other.author and self.title == other.title
        else: return  False

    def update_borrowed_list(self):
        books_str = ", ".join([f"{b.title}({b.author})" for b in borrowed_books])
        blist.config(text=f"대출 현황: {books_str}")



        

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
    global b_n 
    global b_a 
    b_n = name.get() 
    b_a = author.get() 
    book= Book(b_n,b_a)
    if not b_a or not b_n:
        rlabel.config(text='제목이나 저자가 비어있습니다',fg='red')
    else:
        te,tc=book.borrow_book()
        rlabel.config(text=te,fg=tc)
def retrunbook():
    global book
    global b_n 
    global b_a 
    b_n = name.get() 
    b_a = author.get() 
    book= Book(b_n,b_a)
    te,tc=book.return_book()
    rlabel.config(text=te,fg=tc)

b_B= Button(frame3,text="대출",command=borrow)
b_B.pack(side=LEFT,padx=20)
r_B= Button(frame3,text="반납",command=retrunbook)
r_B.pack(side=LEFT,padx=20)

borrowed_books= []
blist= Label(root,text="없음")
blist.pack()

root.mainloop()
