#Hii All This is DAY79(22-01-2024) Today's Topic is Write a program that reverse a list using a loop
#initialize list
myList = ['apple', 'banana', 'cherry', 'mango','rs','Good']
#store reversed list in this
reversedList = []
#reverse list using for loop
for i in range(len(myList)) :
    reversedList.append(myList[len(myList) - i - 1])
print(f'Original List : {myList}')
print(f'Reversed List : {reversedList}')
