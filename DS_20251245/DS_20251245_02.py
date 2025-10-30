from tkinter import *


def draw_image():

    global img  # 전역 변수로 선언 (함수 종료 후에도 참조 유지)
    canvas.delete("all")
    img = PhotoImage(file="DS_20251245/image4.png")

    canvas.create_image(20, 20, anchor=NW, image=img)
def draw_rec():
    canvas.delete("all")
    canvas.create_rectangle(100,100,200,200,fill='red')
def draw_cir():
    canvas.delete("all")
    canvas.create_oval(100,100,200,200,fill='blue')
def delall():
    canvas.delete("all")

root = Tk()
root.title('중간고사 7번')
root.geometry("420x440")
choice=IntVar()

canvas=Canvas(root,width=400,height=320,bg="white")
canvas.pack()

buframe= Frame(root)
buframe.pack()


Button(buframe,text='사각형',command=draw_rec).pack(side=LEFT,padx=10)
Button(buframe,text='원',command=draw_cir).pack(side=LEFT,padx=10)
Button(buframe,text='그림',command=draw_image).pack(side=LEFT,padx=10)
Button(buframe,text='지우기',command=delall).pack(side=LEFT,padx=10)

Label(root,text="버튼을 눌러 도형을 선택하세요").pack()


root.mainloop()
