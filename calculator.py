def add(n1,n2):
	return n1+n2
def subtract(n1,n2):
	return n1-n2
def multiply(n1,n2):
	return n1*n2
def divide(n1,n2):
	return n1/n2
def power(n1,n2):
	return n1**n2
def calculator(n1,operator,n2):
	if operator=="+":
		return add(n1,n2)
	if operator=="-":
		return subtract(n1,n2)
	if operator=="*":
		return multiply(n1,n2)
	if operator=="/":
		return divide(n1,n2)
	if operator=="**":
		return power(n1,n2)
	else:
		print("INVALID!!!")
n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))
operator=input("\nEnter any operator\n +\n -\n *\n /\n **\n")
result=calculator(n1,operator,n2)
print("Result=",result)
