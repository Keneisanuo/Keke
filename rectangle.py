class Rectangle():
    def f(self,b,l):
        self.b=b
        self.l=l
    def area(self):
        return self.b*self.l
    a=int(input("enter the length of the rectangle: "))
    b=int(input("enter the breadth of the rectangle: "))
    obj=Rectangle(a,b)
    print("area of rectangle: ",obj.area())
    print()
