#hii all This is DAY55(29-12-2023) Today's topic is Find the min ,max value in list without using min(),max()

num=[35,4,66,78,2,79] #list
temp=num[0]#Now temp value is 0

i=1 #starting value
while(i<len(num)):#len mean till end of values  i<len(num) is start to end
    if temp > num[i]:#temp 0>35 true now temp is 35
        temp=num[i]#temp 35
    i=i+1 #now 4    again while loop
print("The Minnimum value in the list is:",temp)

# Find the max value in list without using max()
num=[35,4,66,78,2,79] #list
temp=num[0]#Now temp value is 0

i=1 #starting value
while(i<len(num)):#len mean till end of values  i<len(num) is start to end
    if temp < num[i]:#temp 0<35 true now temp is 35
        temp=num[i]#temp 35
    i=i+1 #now 4    again while loop
print("The Maximum value in the list is:",temp)
           
    
