class Book:
    def __init__(self,title,author,borrowed=False):
        self.title= title
        self.author = author
        self.borrowed = borrowed

    def borrow(self):
        if self.borrowed == False:
            self.borrowed = True
            print(self.title,'이(가) 대출되었습니다')
        else:
            print(self.title,'은(는) 이미 대출 중입니다')

    def return_book(self):
        if self.borrowed == True:
            self.borrowed = False
            print(self.title,'이(가) 반납되었습니다')
        else:
            print(self.title,'은(는) 대출되지 않은 상태입니다')

b1= Book('파이썬프로그래밍','홍길동')
b1.return_book()
b1.borrow()
b1.return_book()
