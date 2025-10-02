from tkinter import *

def keypress(event):
    print('키가 눌렸습니다',event.keysym)

root=Tk()
root.geometry('300x200')

root.bind('<Key>',keypress)
root.focus_set()

root.mainloop()

