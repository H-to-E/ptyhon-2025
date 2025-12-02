import os
from tkinter import *
from tkinter import filedialog

base_dir=os.path.dirname(__file__)




def count_stats(filename):
    file=os.path.join(base_dir,filename)
    files=open(file,"r")
    upper_cnt=0
    lower_cnt=0
    space_cnt=0
    for line in files:
        for c in line:
            if c.isupper() :
                upper_cnt +=1
            elif c.islower() :
                lower_cnt +=1
        space_cnt += line.count(' ')
    return f'스페이스:{space_cnt},대문자:{upper_cnt},소문자:{lower_cnt}'
def select_file():
    filename=filedialog.askopenfilename()
    l1.config(text=f'선택된 파일:{filename}')
    cnt=count_stats(filename)
    l2.config(text=cnt)


root=Tk()
root.title('문제5')
root.geometry('520x220')

Label(root,text='텍스트 파일을 선택하여 스페이스,대문자,소문자 개수를 세어보세요').pack()

b1=Button(root,text='파일선택',command=select_file).pack()

l1=Label(root,text='선택된 파일:(없음)')
l1.pack()

l2=Label(root,text='스페이스:0,대문자:0,소문자:0')
l2.pack()

root.mainloop()


