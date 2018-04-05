class car() :
    def __init__(self, color,price):
        self.color = color
        self.price=price
    def cars(self):
            return self.color,self.price
        
col=(input("enter color:"))
pr=int(input("enter price:"))
obj=car(col,pr)
print("the car color and price is: ",obj.cars())

        
