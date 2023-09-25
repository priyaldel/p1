import math
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return math.pi * (self.r**2)
    def perimeter(self):
        return 2*math.pi*self.r
r=float(input("enter radius: "))
c1=Circle(r)
area=c1.area()
perimeter = c1.perimeter()
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
