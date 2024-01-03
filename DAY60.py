#Hii all this is DAY60(03-01-2024) Today's Topic is Find HCF and GCD

num1=int(input("Enter a Num1:"))
num2=int(input("Enter a Num2:"))

if num1<num2:
    small=num1
else:
    small=num2

i=1
hcf=0
while(i<small):
    if num1%i ==0 and num2%i==0:
        hcf=i
    i=i+1
print(hcf)
