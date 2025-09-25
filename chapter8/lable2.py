from tkinter import *

root = Tk()

Label(root, text="Times Font and red.", fg="red", font="Times 32 bold italic").pack()
Label(root, text="Helvetica and green", fg="blue", bg="yellow", font="Helvetica 32 bold italic").pack()

root.mainloop()