#Cases
#snake_case = uses _ for spaces
#cammelCase = uses no spaces and 1st letter is lower case then rest upper case 1st letter of each word
#PascalCase = uses no spaces a upper case 1st letter of each word
#Kebab-Case = uses - for spaces

# select multiply lines then press Crt+/ to to comment in/out

print("This is data notes")
# print() is used to show outputs in the terminal

print("this is a string")
print("1234")
# both are string if it has "" it is a string with characters 8 and 9 are strings

print(1234)
#this is an interger- a whole number value

print("12.34")
#this is a floating point. it is a mathematical value

print(None)
#this is none - it is empty or has no value null/undefines

print(True)
print(False)
# these are a boolean, boolean can be true or false

print("hello world".upper())
# .upper() prints the string in capital

print(len("hello"))
# this prints the number of characters in a string

print("hello"[1])
# will return e becuase it starts from 0 and 0 is h

print("hello"[-1])
# will return o as -1 will give the last character


#activity 1

print("Activity 1")

print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")

#Activity 2

print("HELLO".lower())
#lower()	Converts a string into lower case

print("hi my name is HAssan".capitalize())
#capitalize()	Converts the first character to upper case and lower case any other

print("hi my name is hassan".count("a"))
#count()	Returns the number of times a specified value occurs in a string

print("138964327".find("6"))
#find()	Searches the string for a specified value and returns the position of where it was found

print("hi my name is hassan".replace("hassan","Mr Naik"))
#replace()	Returns a string where a specified value is replaced with a specified value

print("hi my name is hassan".strip("hi "))
#strip()	Returns a trimmed version of the string

#activity 3

print("hi my name is hassan".title())
#title()	Converts the first character of each word to upper case

print("138964327".isnumeric())
#isnumeric()	Returns True if all characters in the string are numeric

number_str = '1 2 3 4'
int_list = list(map(int,number_str.split()))
print(int_list)
#print(type(int_list()))
# converts string into a intiger

print(type(int("1234")))
#print(int("1234"))

