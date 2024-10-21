a=[]
n=int(input("Enter the Number of Elements in the list:"))
for x in range(0,n):
	elements=input("Enter Elements "+str(x+1)+ ":")
	a.append(elements)
max1=len(a[0])
temp=a[0]
for i in a:
	if(len(i)>max1):
		max1=len(i)
		temp=i
print("The Word with Largest Length is:")
print(temp)
