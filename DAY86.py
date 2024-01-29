#Hii all This is DAY86(29-01-2024) Today's topic is Python Program to Check Armstrong Number
# Python program to determine whether
# the number is Armstrong number or not
# Function to calculate x raised to 
# the power y
def power(x, y):
	if y == 0:
		return 1
	if y % 2 == 0:
		return power(x, y // 2) * power(x, y // 2)	
	return x * power(x, y // 2) * power(x, y // 2)
# Function to calculate order of the number
def order(x):
	# Variable to store of the number
	n = 0
	while (x != 0):
		n = n + 1
		x = x // 10	
	return n
# Function to check whether the given 
# number is Armstrong number or not
def isArmstrong(x):	
	n = order(x)
	temp = x
	sum1 = 0
	while (temp != 0):
		r = temp % 10
		sum1 = sum1 + power(r, n)
		temp = temp // 10
	return (sum1 == x)
x = int(input("Enter a number to check whether number is arm or Not:"))
print(isArmstrong(x))

