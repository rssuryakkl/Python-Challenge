#hii all this is DAY45(19-12-2023) today's topic is pattern

# Python  code to demonstrate star pattern
def patt(n):		
	for i in range(0, n): # outer loop to handle number of rows , n in this case		
		for j in range(0, i+1): # inner loop to handle number of columns , values changing acc. to outer loop			
			print("* ",end="") # printing stars	
		print("\r")# ending line after each row
n = int(input("Enter a Number:"))
patt(n)
