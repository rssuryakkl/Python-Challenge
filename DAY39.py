#hii all this is DAY39(13.12.2023) Today's topic ic patten

#Expect output
'''
A
A B 
A B C 
A B C D 
A B C D E
'''
# Input
for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print()
