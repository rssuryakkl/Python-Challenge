#Hii all This is DAY76(19-01-2024) Today's Topic is Python Program to Swap Two Variables

# Python program to swap two variables


# To take inputs from the user
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
