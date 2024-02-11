# Hii all This is DAY99(11-02-2024) Today's Topic is Write a program to create a list of numbers in the range 1 to 20. Then delete all the numbers from the list that are divisible by 3.

num = [ ]
for x in range(1, 21):
    num.append(x)
print("The list of numbers from 1 to 20 =" , num)
for index, i in enumerate(num):
    if(i % 3 == 0):
        del num[index]
print("The list after deleting numbers" , num) 
