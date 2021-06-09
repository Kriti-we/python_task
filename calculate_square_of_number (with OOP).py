class cal4:
    
    def setdata(self, a):
        s = a ** a
        return s


a = int(input("Enter first number:"))

obj = cal4()
s = obj.setdata(a)
print("Sum is:", s)

