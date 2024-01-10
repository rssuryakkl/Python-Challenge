#Hii all this is DAY67(10-01-2024) Today's topic is pattern
rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

'''
Experted Output:
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5 



'''
