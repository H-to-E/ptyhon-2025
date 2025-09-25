from tkinter import *

root= Tk()

photo=PhotoImage(file="chapter8/dog2.gif")
w=Label(root,image=photo,justify="left").pack(side="right")

message="i don't see nobody but you\nboy you got me hooked on to something\nwho could say that so us coming\ntell me do you feel the love\nspend the summer of life time with me\ntake me to the place of your dream"
w1=Label(root,padx=10,text=message).pack(side="left")
root.mainloop()