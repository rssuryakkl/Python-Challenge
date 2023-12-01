#Hii all This is DAY27(01-12-2023) today 's topiic is list range
for i in range(2,21,2):
    print("Multiply by 2:",i)

#Creating a list with series of value
series = list(range(2,11))
print(series)

series = list(range(2,21,2))
print(series)

hi = []
for i in range(1,11):
    s=i**2
    hi.append(s)
    print(hi)

#List comprehensions

squ=[x**2 for x in range(1,11)]
print(squ)

#Other important list funcion
MyList=['Thilothamma', 'Tharani', 'Anitha','SaiSree', 'Lavanya']
x=MyList.reverse()
print(x)
ct=MyList.index('Tharani')
print(ct)
tt=MyList.copy()
print(tt)
MyList=['Thilothamma', 'Tharani', 'Anitha','SaiSree', 'Lavanya']
ct=MyList.index('Tharani')
print(ct)









