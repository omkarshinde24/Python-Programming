class circle :
    def __init__(self):
        a = int(input("enter the radius of the circle "))
        self.a = a 

    def area(self):
        print(f"the area of the cicle is {self.a**2*3.14}")

    def circumference(self):
        print(f"the circumference of the circle is{ 2*3.14*self.a}")

c1 = circle()
c1.area()
c1.circumference()