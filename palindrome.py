def is_palindrome(n):
	str1=str(n)
	reversed_str=str1[::-1]
	return str1==reversed_str
n=str(input("Enter the number or string:"))
if is_palindrome(n):
	print("Is Palindrome!!")
else:
	print("Nor Palindrome!!")
