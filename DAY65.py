#hii All This is DAY65(08-01-2024) Today's  Pattern of abc,,,

n = 5
alph = 65
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()


'''
output format:

      A 
     A B 
    A B C 
   A B C D 
  A B C D E 
'''
