class Shape:
    def __init__(self,width,height):
        self.width=width
        self.height=height
class Triangle(Shape):
    def __init__(self,width,height):
        super().__init__(width,height)
    def calculate(self):
        s= self.width*self.height/2
        print('삼각형의 밑변:',self.width)
        print('삼각형의 높이:',self.height)
        print('삼각형의 넓이:',s)

t=Triangle(4,6)
t.calculate()
