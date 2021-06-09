a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a >= b:
    if a>c:
        largest=a
    else:
        largest=c
    
else:
    if b >= c:
        largest=b
    else:
        largest=c
print("largest number from given number is", largest)
