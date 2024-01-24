
#Hii all This is DAY81(24-01-2024) Today's Topics is Write a program that creates a list of numbers from 1 to 50 that are either divisible by 3 or divisible by 6.

n = [ ]
s = [ ]
for x in range(1, 51):
    n.append(x)
    for x in range(1, 51):
        if(x%3 == 0) or (x % 6 == 0):
            s.append(x)
print("The numbers divisible by 3 or 6 is :", s)
