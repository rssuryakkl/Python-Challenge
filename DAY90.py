#Hii all This is DAY90(02-02-2024) Today's Topic is Write a program to print the following pattern.

def facct(n):
    num=65
    for i in range(0,n):
        for j in range(0,i+1):
            ch=chr(num)
            print(ch,end=' ')
            num=num+1
        print()
n=5
facct(n)
            
        
































