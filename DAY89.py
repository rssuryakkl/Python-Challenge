#Hiii all This is DAY89(01-02-2024) Today's topics Find length of a string in python

# Python code to demonstrate string length 
# using while loop.

# Returns length of string
def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

str = input("Enter a String:")
print(findLen(str))
