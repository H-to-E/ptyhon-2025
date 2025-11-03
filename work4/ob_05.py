class Car:
    def __init__(self,model,odometer=0):
        self.model = model
        self.odometer=odometer
    def drive(self,km):
        self.odometer+=km
    def info(self):
        return "모델:"+str(self.model)+",주행거리:"+str(self.odometer)+"km"

c= Car('BMW')
c.drive(50)
c.drive(70)
c.info()
