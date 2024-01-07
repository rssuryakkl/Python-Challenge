#Hii All This is DAY63(06-01-2024) today's Topic is FIBONACCI SERIES
a=int(input("Enter a Number:"))
x=0
y=1
print(x)
print(y)
for i in range(0,a):
    print(x+y)
    temp=x
    x=y 
    y=temp+y
