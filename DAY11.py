#hii all this is DAY11(08.11.2023) today we  are going to see a topic on for loop

for i in range(2,20,2):
    print(i)

for i in range(2,20,2):
    print(i,end='\t')

#nested structure loop

a=1
while(a<=6):
    for i in range(1,a):
        print(i,end='\t')
    print(end='\n')
    a=a+1
