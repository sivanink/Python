def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		result=factorial(n-1)
		return n*result
n=int(input("Enter A Number:"))
print("Factorial is",factorial(n))
