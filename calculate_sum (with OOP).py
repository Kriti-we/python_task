# class aerith:
#     m=0
#     n=0
#     def __init__(self,m,n) -> None:
#         self.m=m
#         self.n=n
#     def sum(self):
#         ans=self.m+self.n
#         print("Sum of",self.m,"&",self.n,"is",ans)
#     def sub(self):
#         ans=self.m-self.n
#         print("Substraction of",self.m,"&",self.n,"is",ans)
#     def mul(self):
#         ans=self.m*self.n
#         print("Multiplication of",self.m,"&",self.n,"is",ans)
#     def div(self):
#         ans=self.m/self.n
#         print(self.m,"divide",self.n,"is",ans)
# a=aerith(18,9)
# a.sum()
# a.sub()
# a.mul()
# a.div()

class cal1:
    
    def setdata(self, a, b, c):
        s = a + b +c
        return s


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

obj = cal1()
s = obj.setdata(a, b, c )
print("Sum is:", s)

