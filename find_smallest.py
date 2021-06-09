a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if (a <= b) and (a <= c):
    smallest=a
elif (b <= a) and (b <= c):
    smallest=b
else:
    smallest=c 
print("largest number from given number is", smallest)