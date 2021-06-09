class cal6():
    
    def __init__(self,breadth,length):
        self.length=length
    def area(self):
        return self.length*self.length
a=int(input("Enter length of rectangle: "))

obj=cal6(a)
print("Area of rectangle:",obj.area())
 
print()

