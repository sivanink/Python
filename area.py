a=int(input("Enter side 1:"))
b=int(input("Enter side 2:"))
c=int(input("Enter side 3:"))
s=(a+b+c)/2
print("Semi perimeter of triangle=",s)
r=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area=",r)
