#Hii all This DAY54(28-12-2023) Today's Topic is Remove duplicate elements from a list in python

listt=[5,4,3,2,1,2,5,7]
output=[]
for value in listt:
    if value not in output:
        output.append(value)
print(listt)
print("After removed a duplicated values from the list:",output)
