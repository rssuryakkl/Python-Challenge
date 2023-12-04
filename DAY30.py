#hiii all This is DAY30(04-12-2023) today topic is tuple Update and Delete Tuple
#Update and Delete Tuple

Tup1 = (2,4,6,8,10)
Tup2 = (1,3,5,7,9)
Tup3 = Tup1 + Tup2
print(Tup3)

#Tuple Assignment
(a, b, c) = (34, 90, 76)
print(a)
print(b)
print(c)
# expression are evaluated before assignment
(x, y, z, p) = (2**2, 5/3+4, 15%2, 34>65)
print(x,y,z,p)

#Nested Tuples
nest=(("surya",67,"under 18"),("anbu",68,"above 18"),("selvi",69,"under 18"),("nandha",66,"above 18"))
for i in nest:
    print(i)


Tup1 = (2,4,6,8,10)
print("The elements of Tup1 is ", Tup1)
del Tup1
print (Tup1)


















