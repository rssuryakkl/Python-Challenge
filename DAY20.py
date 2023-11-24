# hii all This is DAY20(24-11-2023) today we are discuss about String Operators

#(i) Concatenation (+)
hiii=input("Enter a String:")
hiiii=input("Enter a joined to be:")
print(hiii+hiiii)

#(ii) Append (+ =)
a="surya"
a+=" rs"
print(a)
print("Joined Words are :",a)

#(iii) Repeating (*)
str1="hii surya "
print(str1*4)

#(iv) String slicing
str2="SURYA HI HOW ARE YOU"
print(str2[0])
print(str2[4])#single value denotes a call value or pick value
print(str2[0:4])#0to 4 value want ro print but slicing takes last value as n-1
print(str2[0:21])
print(str2[:3])
print(str2[3:])

#example:
j="COMPUTER"
index=0
for i in j:
    print(j[:index+1])
    index+=1
    
