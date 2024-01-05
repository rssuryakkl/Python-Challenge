#Hii all This is DAY62(05-01-2023) Today's Topic is Split the odd and even number from the List

list1=[1,2,3,4,5,6,7,8,9,10]
odd=[]
even=[]
for val in list1:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print("Whole List:",list1)
print("Odd list:",odd)
print("Even list:",even)
