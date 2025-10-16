import tkinter as tk
root = tk.Tk()

timer =0
def startTimer():
    if running:
        global timer
        timer+=1
        timeText.comfigure(text=str(timer))
    root.after(10,startTimer)
def start():
    global running
    running-=True
def stop():
    global running
    running=False   
running = False
timer = 0

timeText=tk.Label(root,text="0",font=('Helvetica',80))
timeText.pack()

startButton=tk.Button(root,text='시작',bg='yellow',command=start)
startButton.pack(fill-tk.BOTH)

stopButton = tk.Button(root,twxt='스톱',bg='yellow',command=stop)
stopButton.pack(fill=tk.BOTH)

startTimer()
root=mainloop()
