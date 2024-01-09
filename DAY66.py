#Hii all This is DAY66(09-12-2024) Today's Topic is a simple Python program to print a pyramid pattern


'''
Exceperted output:
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
'''

for i in range(0,7):
    for j in range(0,7-i):
        print(end=" ")
    for j in range(0,i+1):
        print("* ",end="")
    print()

