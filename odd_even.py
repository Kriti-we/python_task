a=int(input("enter a number:"))
if a < 100:
    b = a % 2
    if b > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")
else:
    print("given number is not less then 100 opps sorry!!")
