import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plotgraph():
     x= float(xentry.get())
     y= float(yentry.get())
     xdata.append(x)
     ydata.append(y)
     ax.clear()
     ax.plot(xdata,ydata,marker = 'o',linestyle='-')
     canvas.draw()

root = tk.Tk()
root.title("Dynamic Line Graph")

xdata=[]
ydata=[]

xlabel=tk.Label(root,text="Enter x cordinate:")
xlabel.pack()
xentry=tk.Entry(root)
xentry.pack()

ylabel=tk.Label(root,text="Enter y cordinate:")
ylabel.pack()
yentry=tk.Entry(root)
yentry.pack()

plotbutton= tk.Button(root,text="Plot",command=plotgraph)
plotbutton.pack()

fig = Figure(figsize=(5,4),dpi=100)
ax= fig.add_subplot(111)

canvas=FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack()

root.mainloop()