name=[]
n=int(input("Enter the number of students:"))
for i in range(1,n+1):
	print("Enter The Name",i)
	item=str(input())
	name.append(item)
print(name)
name.sort()
print("Alphabetic Order Names:",name)

