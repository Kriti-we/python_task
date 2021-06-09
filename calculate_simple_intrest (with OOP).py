class cal3:
    
    def setdata(self,p,n,r,y):
        FV = P * (((1 + ((r/100.0)/n)) ** (n*y)))

        return FV

P = int(input("Enter starting principle please. "))
n = int(input("Enter number of compounding periods per year. "))
r = float(input("Enter annual interest rate. e.g. 15 for 15% "))
y = int(input("Enter the amount of years. "))

obj = cal3()
FV = obj.setdata(p,n,r,y)

print ("The final amount after", y, "years is", FV)
