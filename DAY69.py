#Hii all This is DAY69(12-01-2024) Today's Topic is Write a Python code to find the L.C.M. of two numbers.

num1=int(input("Enter a Number1:"))
num2=int(input("Enter a Number2:"))

if num1>num2:
    greater=num1
else:
    greater=num2
while True:
    if greater %num1==0 and greater%num2==0:
        lcm=greater
        break
    greater+=1
print("The L.C.M is",lcm)
