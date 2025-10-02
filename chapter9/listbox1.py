from tkinter import *

root =Tk()

lb=Listbox(root,height=4)

lb.pack()
lb.insert(END,'python')
lb.insert(END,'c')
lb.insert(END,'jave')
lb.insert(END,'swift')

root.mainloop()


