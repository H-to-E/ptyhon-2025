#--init-- use
class Counter:
    def __init__(self):
        self.count=0
    def inctrment(self):
        self.count +=1
    def get(self):
        return self.count

a=Counter()
b=Counter()

a.inctrment()
a.inctrment()
b.inctrment()

print(a.get())
print(b.get())