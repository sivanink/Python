def power(base,exponent):
	if exponent==0:
		return 1
	elif exponent==1:
		return base
	else:
		return base*power(base,exponent-1)
base=float(input("ENTER THE BASE:"))
exponent=int(input("ENTER THE EXPONENT:"))
result=power(base,exponent)
print(base,"raised to the power of",exponent,"is",result)
	
