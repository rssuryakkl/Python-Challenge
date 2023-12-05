#hii all this is DAY31(05-12-2023) today we are  going to see a topic on Sets

hi=89,90,45,23
print(hi) #this is tuple

hi=89,90,45,23
print(list(hi)) #this is list

#Creating Set using List or Tuple
MyList=[2,4,6,8,10]
MySet=set(MyList)
print(MySet)

my=[2,4,6,8,10]
print(set(my))

#Set Operations
#Union: It includes all elements from two or more sets
set_A={2,4,6,8}
set_B={'A', 'B', 'C', 'D'}
set_c=set_A|set_B
print(set_c)

set_A={2,4,6,8}
set_B={'A', 'B', 'C', 'D',2,4} #and uninon operator skips the duplicated values
set_c=set_A|set_B
print(set_c)

#(ii) Intersection: It includes the common elements in two sets
set_A={2,4,6,8}
set_B={'A', 'B', 'C', 'D',2,4}
set_c=set_A&set_B
print(set_c)

#(iii) Difference
set_A={2,4,6,8}
set_B={'A', 'B', 'C', 'D',2,4}
set_c=set_A - set_B
print(set_c)

#(iv) Symmetric difference
set_A={2,4,6,8}
set_B={'A', 'B', 'C', 'D',2,4}
set_c=set_A ^ set_B
print(set_c)



