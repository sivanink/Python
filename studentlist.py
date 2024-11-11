student={}
ls=[]
n=int(input("Enter The Number Of Students:"))
for i in range(0,n):
	name=input("Enter The Name:")
	age=input("Enter The Age:")
	grade=input("Enter The Grade:")
	student[name]=age,grade
print(student)
