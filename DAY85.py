#Hii All This is DAY85(28-01-2024) Today's Topic is Python program to interchange first and last elements in a list

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping 
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# iser input
newList = list(input())

print(swapList(newList))
