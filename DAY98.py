#Hii all This is DAY98(10-02-2024) Today's Topic is Write a program that creates a list of numbers from 1 to 50 that are either divisible by 3 or divisible by 6.
a=[]
b=[]
for i in range(1,51):
    a.append(i)
    if(i%3==0) or (i%6==0):
        b.append(i)
print("The Number Divisible by 3 and 6:",b) 
    
