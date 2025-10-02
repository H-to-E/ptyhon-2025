class Student():
    gradelist=[]
    def __init__(self,name,grade):
        self.name=name
        self.gradelist.append(grade)

    def add_score(self,grade):
        print(f'{self.name}의 성적 {grade}점이 추가되었습니다')
        self.gradelist.append(grade)

    def cal_avg(self):
        return sum(self.gradelist)/len(self.gradelist)

    
a= Student('kim',90)
a.add_score(85)
a.add_score(78)
avg = a.cal_avg()

print(f'{a.name}의 평균 성적:{avg:.2f}')