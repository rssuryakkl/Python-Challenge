#Hiii all this is DAY12(09.11.2023) We are going to see a topic on Python Nested for Loops Practice Exercises

a=6
for i in range(a+1):
    for j in range(i):
        print(i,end='\t')
    print(" ")

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')

rows = 6
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
