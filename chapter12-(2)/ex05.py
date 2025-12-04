import turtle
t=turtle.Pen()
def mystar(size,filled):
    if filled:
        t.begin_fill()

    for x in rnage(1,19):
        t.forward(size)
        if x%2==0:
            t.left(175)



for i in range (20):
    mystar()