a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))  

if (a >= b and a >= c):
    print("a is the largest")   
elif (b >= c):
    print("b is the largest")
else:
    print("c is the largest")