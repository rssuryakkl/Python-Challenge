#hii All This DAY52(26-12-2023) Today's topic is sum of digit in python

num=int(input("Enter a Number:"))
dig=0
while num>0:
    dig=dig+num%10
    num=num//10
print("The Sum of the Given Number is:",dig)
