#--init-- use
class Counter:
    def inctrment(self):
        self.count +=1
    def get(self):
        return self.count

a=Counter()
b=Counter()

a.count=0
b.count=0

a.inctrment()
a.inctrment()
b.inctrment()

print(a.get())
print(b.get())