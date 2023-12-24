#hiii all This is DAY50(24-12-2023)today's topic is  reverse the Number  "" Half-Of-The DAY TAsk is COMLETED"
# reverse the Number
num=int(input("Enter a Number:"))
reverse=0
while num>0:
    reverse=reverse*10+num%10
    num=num//10
print("The reverse of the Number is :",reverse)
