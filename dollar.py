string=input("ENTER A STRING:")
first_char=string[0]
new_string=first_char+string[1:].replace(first_char,'$')
print(new_string)
