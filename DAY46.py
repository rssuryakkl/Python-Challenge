#Hii all This is DAY6(20.12.2023) Today's Topic is demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	k = n - 1 	# number of spaces
	for i in range(0, n):	# outer loop to handle number of rows		
		for j in range(0, k):	# inner loop to handle number spaces , # values changing acc. to requirement
			print(end=" ")	
		k = k - 1	# decrementing k after each loop		
		for j in range(0, i+1):# inner loop to handle number of columns , # values changing acc. to outer loop			
			print("* ", end="")# printing stars		
		print("\r")# ending line after each row

# Driver Code
n =int(input("Enter a Number:"))
triangle(n)
