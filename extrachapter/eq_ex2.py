class Student:
    def __init__(self,stu_id,name):
        self.name=name
        self.stu_id=stu_id
    def __eq__(self,other):
        if isinstance(other,Student):
            return self.stu_id == other.stu_id
        return False

s1= Student('202501','김민수')
s2= Student('202502','이수정')
s3= Student('202503','박지훈')
s4= Student('202501','홍길동')

student=[s1,s2,s3]

print(s1 in student)
print(s2 in student)
print(s3 in student)
print(s4 in student)