#hii all this is DAY28(02-12-2023) today we are  going to discuss about list function
#Other important list funcion
#copy ( )
listmy=[78,33,23,99,45]
x=listmy.copy()
print(x)  #ans:[78, 33, 23, 99, 45]

#count()
listmy=[78,33,23,99,45,33]
x=listmy.count(33)
print(x)          #ans:2

#index()
listmy=[78,33,23,99,45]
x=listmy.index(33)
print(x)          #ans:1

#reverse()
listmy=[78,33,23,99,45]
x=listmy.reverse()
print(x)          #ans:[45, 99, 23, 33, 78]    but displayed answer is NONE so i displayed as using function of copy
x=listmy.copy()
print(x)         #ans:[45, 99, 23, 33, 78]


#sort()
listmy=[78,33,23,99,45]
x=listmy.sort()
print(x)          #ans:[23, 33, 45, 78, 99]  #same reason NONE for this  because its is sorted but displayed anser is NONE Actual ans is [23, 33, 45, 78, 99]
x=listmy.copy()
print(x)          #ans:[23, 33, 45, 78, 99]

#max()
listmy=[78,33,23,99,45]
print(max(listmy))          #ans:99

#min()
listmy=[78,33,23,99,45]
print(min(listmy))          #ans:23

#sum
listmy=[78,33,23,99,45]
print(sum(listmy))          #ans:278







