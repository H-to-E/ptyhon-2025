class Course:
    def __init__(self,name,scores=[]):
        self.name=name
        self.scores=scores
    def add_score(self,s):
        self.scores.append(s)
    def avg(self):
        return sum(self.scores)/len(self.scores)
    def info(self):
        self.avg=Course.avg(self)
        return "과목:"+str(self.name)+",평균:"+str(self.avg)

c= Course('파이썬')
c.add_score(80)
c.add_score(90)
c.avg()
c.info()

