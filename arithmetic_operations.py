a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("1.Sum")
print("2.Difference")
print("3.Multiplication")
print("4.Division")
print("5.Exponent")
print("6.FloorDivision")
print("7.Modulus")
c=int(input("Select choice:"))
if c==1:
	d=a+b
	print("Sum=",d)
elif c==2:
	d=a-b
	print("Difference=",d)
elif c==3:
	d=a*b
	print("Multiplication=",d)
elif c==4:
	d=a/b
	print("Division=",d)
elif c==5:
	d=a**b
	print("Exponent=",d)
elif c==6:
	d=a//b
	print("Floor Division=",d)
elif c==7:
	d=a%b
	print("Modulus=",d)
else:
	print("Wrong Choice!!!!")
	
	


	
	




