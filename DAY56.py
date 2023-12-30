#HI all This is DAY56(30-12-2023) Today's Topic is Print the unique elements from the list 


list=[23,55,10,20,10,23,143]
unique=[]
for val in list:
    if list.count(val)==1:#counting values from the list
        unique.append(val)
print(unique)
