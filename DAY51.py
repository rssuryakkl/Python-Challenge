#Hii all This is DAY51(25-12-2023) Today's topic is REVERSE THE STRING
#DAY51(25-12-2023)

#reverse the string 
hi=input("Enter a String:")
rev=hi[::-1]
print(rev)

#reverse the integer
kk=int(input("Enter a integer:"))
rev=0
while(kk>0):
    rev=rev*10+kk%10
    kk=kk//10
print(rev)

